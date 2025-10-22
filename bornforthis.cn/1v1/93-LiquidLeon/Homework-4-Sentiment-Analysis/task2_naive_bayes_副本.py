
# -*- coding: utf-8 -*-
# Task 2: Naive Bayes with NLTK — Approach A (explicit word_feats per assignment skeleton)
import nltk
from nltk.classify import NaiveBayesClassifier

from collections import Counter
import matplotlib.pyplot as plt

import sentiment_utils as sutils

TRAIN_FILE = "movie_reviews_train.txt"
DEV_FILE   = "movie_reviews_dev.txt"

# Load tokenized data
train_X, train_y = sutils.generate_tuples_from_file(TRAIN_FILE)
dev_X,   dev_y   = sutils.generate_tuples_from_file(DEV_FILE)

# (Optional) build a vocab from training set; you may use it to filter features if desired
vocab = set(sutils.create_index(train_X, min_freq=1))

# === Assignment-style feature function ===
def word_feats(tokens, binary: bool = False, use_train_vocab: bool = True) -> dict:
    """
    将一篇文档（分词列表）转为 NB 可用的特征字典。
    参数:
        tokens: List[str] 该样本的分词序列
        binary: True -> 二值特征; False -> 多项式（计数）特征
        use_train_vocab: 若为 True，则仅保留出现在训练词表中的词（避免引入未见词）
    返回:
        dict[str, int]  特征名->特征值
    """
    if use_train_vocab:
        cnt = Counter(t.lower() for t in tokens if t.lower() in vocab)
    else:
        cnt = Counter(t.lower() for t in tokens)
    if binary:
        return {w: 1 for w in cnt.keys()}
    else:
        return dict(cnt)

def build_instances(X_tok, y, binary: bool, use_train_vocab: bool = True):
    feats = [word_feats(toks, binary=binary, use_train_vocab=use_train_vocab) for toks in X_tok]
    return list(zip(feats, y))

def train_eval_nb(percent: int, binary: bool, seed: int = 0, use_train_vocab: bool = True):
    # sample percent% of training data deterministically
    sub_X, sub_y = sutils.take_percent(train_X, train_y, percent, shuffle=True, seed=seed)
    train_set = build_instances(sub_X, sub_y, binary=binary, use_train_vocab=use_train_vocab)
    dev_set   = build_instances(dev_X, dev_y, binary=binary, use_train_vocab=use_train_vocab)

    # Train NB
    clf = NaiveBayesClassifier.train(train_set)

    # Predict on dev
    preds = [clf.classify(feats) for feats, _ in dev_set]
    preds = [int(p) for p in preds]

    # Metrics
    prec, rec, f1, acc = sutils.get_prfa(dev_y, preds, verbose=False)
    return prec, rec, f1, acc

def plot_runs(binary: bool, run_id: int, percents=None, save_as=None, use_train_vocab: bool = True):
    if percents is None:
        percents = [10, 20, 40, 60, 80, 100]
    title = f"Naive Bayes ({'Binarized' if binary else 'Multinomial'}) — Run {run_id}"
    curves = sutils.create_training_graph(
        metrics_fun=lambda p: train_eval_nb(p, binary=binary, seed=run_id, use_train_vocab=use_train_vocab),
        percents=percents,
        title=title,
        savepath=save_as
    )
    return curves

if __name__ == "__main__":
    # Produce both variants and save graphs (three runs each)
    for run in (1,2,3):
        plot_runs(binary=False, run_id=run, save_as=f"Naive_Bayes_multinomial_run{run}.png")
        plot_runs(binary=True,  run_id=run, save_as=f"Naive_Bayes_binarized_run{run}.png")

    # Quick comparison on full dev set
    _,_,f1_bin,_   = train_eval_nb(100, binary=True,  seed=1)
    _,_,f1_multi,_ = train_eval_nb(100, binary=False, seed=1)
    print(f"Final F1 (binarized)  : {f1_bin:.4f}")
    print(f"Final F1 (multinomial): {f1_multi:.4f}")
