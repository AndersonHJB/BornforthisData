
# -*- coding: utf-8 -*-
# Task 3: Logistic Regression — compare custom vectorizer vs CountVectorizer
import time
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics import precision_recall_fscore_support, accuracy_score

import sentiment_utils as sutils

TRAIN_FILE = "movie_reviews_train.txt"
DEV_FILE   = "movie_reviews_dev.txt"

train_X, train_y = sutils.generate_tuples_from_file(TRAIN_FILE)
dev_X,   dev_y   = sutils.generate_tuples_from_file(DEV_FILE)

vocab = sutils.create_index(train_X, min_freq=1)

def vectorize_custom(X_tok, binary=False):
    feats = sutils.featurize(vocab, X_tok, binary=binary)  # list of dicts
    dv = DictVectorizer(sparse=True)
    X = dv.fit_transform(feats)
    return X, dv

def vectorize_countvectorizer(X_tok, binary=False):
    # join tokens back to strings
    docs = [" ".join(toks) for toks in X_tok]
    cv = CountVectorizer(binary=binary)
    X = cv.fit_transform(docs)
    return X, cv

def train_eval_lr(percent: int, use_cv: bool, binary: bool, run_id: int = 1):
    sub_X, sub_y = sutils.take_percent(train_X, train_y, percent, shuffle=True, seed=run_id)

    if use_cv:
        Xtr, vec = vectorize_countvectorizer(sub_X, binary=binary)
        Xdv, _   = vectorize_countvectorizer(dev_X, binary=binary)  # fit on train ONLY
        # Refit vec on train and transform dev with same vocab
        vec = CountVectorizer(binary=binary, vocabulary=vec.vocabulary_)
        Xtr = vec.fit_transform([" ".join(t) for t in sub_X])  # counts align
        Xdv = vec.transform([" ".join(t) for t in dev_X])
        vocab_size = len(vec.vocabulary_)
    else:
        Xtr, vec = vectorize_custom(sub_X, binary=binary)
        # Align DictVectorizer vocabulary by refitting with fixed feature_names_
        feats_dev = sutils.featurize(vocab, dev_X, binary=binary)
        dv = DictVectorizer(sparse=True)
        Xtr = dv.fit_transform(sutils.featurize(vocab, sub_X, binary=binary))
        Xdv = dv.transform(feats_dev)
        vocab_size = len(dv.feature_names_)

    clf = LogisticRegression(max_iter=1000, n_jobs=None)  # solver auto
    clf.fit(Xtr, sub_y)

    probs = clf.predict_proba(Xdv)[:,1]
    preds = (probs >= 0.5).astype(int).tolist()

    prec, rec, f1, acc = sutils.get_prfa(dev_y, preds, verbose=False)
    return prec, rec, f1, acc, vocab_size

def runtime_and_vocab():
    # Time custom vectorizer
    t0 = time.time()
    Xcust, dv = vectorize_custom(train_X, binary=False)
    t1 = time.time()
    cust_time = t1 - t0
    cust_vocab = len(dv.feature_names_)

    # Time CountVectorizer
    t0 = time.time()
    Xcv, cv = vectorize_countvectorizer(train_X, binary=False)
    t1 = time.time()
    cv_time = t1 - t0
    cv_vocab = len(cv.vocabulary_)

    # Sparsity (%) of zeros
    def sparsity(X):
        nnz = X.nnz
        total = X.shape[0] * X.shape[1]
        return 100.0 * (1.0 - nnz/total)

    print(f"[Custom]    vocab={cust_vocab}  time={cust_time:.4f}s  sparsity={sparsity(Xcust):.2f}%")
    print(f"[CountVect] vocab={cv_vocab}  time={cv_time:.4f}s  sparsity={sparsity(Xcv):.2f}%")

def plot_best_combo(run_id: int, percents=None):
    if percents is None:
        percents = [10, 20, 40, 60, 80, 100]

    # Evaluate 4 combos at 100% to pick best F1
    combos = [
        ('custom-multinomial', False, False),
        ('cv-multinomial',     True,  False),
        ('custom-binarized',   False, True),
        ('cv-binarized',       True,  True),
    ]
    f1s = []
    for name, use_cv, binary in combos:
        _,_,f1,_,_ = train_eval_lr(100, use_cv, binary, run_id=run_id)
        f1s.append((f1, name, use_cv, binary))
    f1s.sort(reverse=True)
    best = f1s[0]
    _, best_name, use_cv, binary = best
    print("Best LR setting (by F1 @100%):", best_name)

    title = f"Logistic Regression ({best_name}) — Run {run_id}"
    sutils.create_training_graph(
        metrics_fun=lambda p: train_eval_lr(p, use_cv=use_cv, binary=binary, run_id=run_id)[:4],
        percents=percents,
        title=title,
        savepath=f"LogReg_{best_name.replace(' ','_')}_run{run_id}.png"
    )

if __name__ == "__main__":
    runtime_and_vocab()
    for run in (1,2,3):
        plot_best_combo(run_id=run)
