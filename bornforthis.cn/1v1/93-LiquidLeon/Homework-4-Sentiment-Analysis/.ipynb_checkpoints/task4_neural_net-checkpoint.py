
# -*- coding: utf-8 -*-
# Task 4: Feedforward Neural Network on BoW
import numpy as np
import sentiment_utils as sutils

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

TRAIN_FILE = "movie_reviews_train.txt"
DEV_FILE   = "movie_reviews_dev.txt"

train_X, train_y = sutils.generate_tuples_from_file(TRAIN_FILE)
dev_X,   dev_y   = sutils.generate_tuples_from_file(DEV_FILE)

vocab = sutils.create_index(train_X, min_freq=1)

def vectorize(use_cv: bool, binary: bool, sub_X=None):
    if sub_X is None:
        sub_X = train_X
    if use_cv:
        docs_train = [" ".join(t) for t in sub_X]
        vec = CountVectorizer(binary=binary, vocabulary=None)
        Xtr = vec.fit_transform(docs_train)
        vec = CountVectorizer(binary=binary, vocabulary=vec.vocabulary_)
        Xdv = vec.transform([" ".join(t) for t in dev_X])
        return Xtr, Xdv, vec
    else:
        feats_tr = sutils.featurize(vocab, sub_X, binary=binary)
        feats_dv = sutils.featurize(vocab, dev_X, binary=binary)
        dv = DictVectorizer(sparse=True)
        Xtr = dv.fit_transform(feats_tr)
        Xdv = dv.transform(feats_dv)
        return Xtr, Xdv, dv

def build_model(input_dim: int, hidden_units: int = 128, hidden_layers: int = 1, dropout: float = 0.2):
    model = Sequential()
    # First hidden
    model.add(Dense(hidden_units, activation='relu', input_shape=(input_dim,)))
    if dropout > 0:
        model.add(Dropout(dropout))
    for _ in range(hidden_layers - 1):
        model.add(Dense(hidden_units, activation='relu'))
        if dropout > 0:
            model.add(Dropout(dropout))
    # Output
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=SGD(learning_rate=0.05, momentum=0.9), metrics=['accuracy'])
    return model

def train_eval_nn(percent: int, use_cv: bool, binary: bool, epochs: int, batch_size: int, run_id: int = 1):
    sub_X, sub_y = sutils.take_percent(train_X, train_y, percent, shuffle=True, seed=run_id)
    Xtr, Xdv, vec = vectorize(use_cv=use_cv, binary=binary, sub_X=sub_X)

    input_dim = Xtr.shape[1]
    model = build_model(input_dim=input_dim, hidden_units=128, hidden_layers=1, dropout=0.2)
    # Keras expects dense arrays; convert sparse to dense if tiny, else to csr then toarray() carefully
    Xtr_arr = Xtr.astype('float32').toarray()
    Xdv_arr = Xdv.astype('float32').toarray()
    ytr = np.array(sub_y, dtype='float32')

    model.fit(Xtr_arr, ytr, epochs=epochs, batch_size=batch_size, verbose=0)
    # Evaluate & predict
    dev_probs = model.predict(Xdv_arr, verbose=0).reshape(-1)
    preds = (dev_probs >= 0.5).astype(int).tolist()
    prec, rec, f1, acc = sutils.get_prfa(dev_y, preds, verbose=False)
    return prec, rec, f1, acc, model.count_params()

def plot_runs_nn(use_cv: bool, binary: bool, epochs: int, batch_size: int, run_id: int, percents=None):
    if percents is None:
        percents = [10, 20, 40, 60, 80, 100]
    title = f"Neural Net ({'CountVectorizer' if use_cv else 'Custom'} | {'Binarized' if binary else 'Multinomial'}) — Run {run_id}"
    sutils.create_training_graph(
        metrics_fun=lambda p: train_eval_nn(p, use_cv=use_cv, binary=binary, epochs=epochs, batch_size=batch_size, run_id=run_id)[:4],
        percents=percents,
        title=title,
        savepath=f"NeuralNet_{'cv' if use_cv else 'custom'}_{'bin' if binary else 'multi'}_run{run_id}.png"
    )

if __name__ == "__main__":
    # Example default: multinomial with CountVectorizer
    epochs = 8
    batch = 32
    # Report parameter count once @100%
    _,_,f1,_, params = train_eval_nn(100, use_cv=True, binary=False, epochs=epochs, batch_size=batch, run_id=1)
    print(f"Model trainable parameters: {params}")
    print(f"F1 (epochs={epochs}) multinomial: {f1:.4f}")

    for run in (1,2,3):
        plot_runs_nn(use_cv=True, binary=False, epochs=epochs, batch_size=batch, run_id=run)
