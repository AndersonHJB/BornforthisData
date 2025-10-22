
# -*- coding: utf-8 -*-
# FIRST: ensure this filename is sentiment_utils.py

"""
CS 4120 — HW4 — Fall 2025
Utility functions reused across Task 2–5.
"""

from collections import defaultdict, Counter
from typing import Callable, Iterable, List, Sequence, Tuple, Dict, Any, Optional

import math
import random
import time

import nltk
from nltk.tokenize import word_tokenize

import numpy as np
import matplotlib.pyplot as plt

# Optional: silent downloads if not already present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    # newer NLTK expects punkt_tab
    try:
        nltk.download('punkt_tab')
    except Exception:
        pass


# ------------------------
# DATA LOADING
# ------------------------

def generate_tuples_from_file(training_file_path: str) -> Tuple[List[List[str]], List[int]]:
    """
    Read TSV file lines of the form:   <id> \\t <raw_text> \\t <label(0/1)>
    Returns:
        X: List[List[str]]  tokenized documents
        y: List[int]        labels 0/1
    """
    X, y = [], []
    with open(training_file_path, "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            cols = line.split("\t")
            if len(cols) != 3:
                continue
            _, text, lab = cols
            if lab not in {"0", "1"}:
                continue
            X.append(word_tokenize(text))
            y.append(int(lab))
    return X, y


# ------------------------
# METRICS
# ------------------------

def _safe_div(a: float, b: float) -> float:
    return (a / b) if b != 0 else 0.0

def get_prfa(gold: Sequence[int], pred: Sequence[int], verbose: bool = False) -> Tuple[float, float, float, float]:
    """
    Compute precision/recall/f1/accuracy for binary labels where positive class=1.
    Returns values in [0,1].
    """
    tp = sum(1 for g, p in zip(gold, pred) if g == 1 and p == 1)
    fp = sum(1 for g, p in zip(gold, pred) if g == 0 and p == 1)
    fn = sum(1 for g, p in zip(gold, pred) if g == 1 and p == 0)
    tn = sum(1 for g, p in zip(gold, pred) if g == 0 and p == 0)
    prec = _safe_div(tp, tp + fp)
    rec  = _safe_div(tp, tp + fn)
    f1   = _safe_div(2 * prec * rec, prec + rec) if (prec + rec) != 0 else 0.0
    acc  = _safe_div(tp + tn, tp + tn + fp + fn)
    if verbose:
        print(f"Precision={prec:.4f} Recall={rec:.4f} F1={f1:.4f} Acc={acc:.4f} (TP={tp} FP={fp} FN={fn} TN={tn})")
    return prec, rec, f1, acc


# ------------------------
# VOCAB & FEATURIZATION
# ------------------------

def create_index(all_train_data_X: List[List[str]], min_freq: int = 1) -> List[str]:
    """
    Build vocabulary list from tokenized training texts (>= min_freq occurrences).
    Returns a deterministic, sorted vocabulary list.
    """
    ctr = Counter()
    for toks in all_train_data_X:
        ctr.update(t.lower() for t in toks)
    vocab = [w for w, c in ctr.items() if c >= min_freq]
    vocab.sort()
    return vocab


def featurize(vocab: List[str], data_X: List[List[str]], binary: bool = False, verbose: bool = False) -> List[Dict[str, int]]:
    """
    Produce a list of sparse feature dicts per example suitable for:
    - NLTK NaiveBayesClassifier (dict[str, int/bool])
    - sklearn DictVectorizer (as counts or binary flags)

    Returns: List[Dict[token, value]]
    """
    vocab_set = set(vocab)
    feats: List[Dict[str, int]] = []
    for i, toks in enumerate(data_X):
        c = Counter(t.lower() for t in toks if t.lower() in vocab_set)
        if binary:
            for k in list(c.keys()):
                c[k] = 1
        feats.append(dict(c))
        if verbose and (i+1) % 1000 == 0:
            print(f"Featurized {i+1} examples")
    return feats


# ------------------------
# PLOTTING
# ------------------------

def create_training_graph(
    metrics_fun: Callable[[int], Tuple[float, float, float, float]],
    percents: Sequence[int],
    title: str,
    savepath: Optional[str] = None,
    verbose: bool = False
) -> Dict[str, List[float]]:
    """
    Calls metrics_fun(perc) for each percentage and plots P/R/F1/Acc vs % train used.
    metrics_fun should *train+evaluate* a model using perc% of available training data
    and return (precision, recall, f1, accuracy) on the dev set.

    Returns the collected curves.
    """
    P, R, F1, A = [], [], [], []
    for p in percents:
        if verbose:
            print(f"==> Running percentage={p}%")
        pr, rc, f1, acc = metrics_fun(p)
        P.append(pr); R.append(rc); F1.append(f1); A.append(acc)

    plt.figure(figsize=(7,5))
    plt.plot(percents, P, marker='o', label='Precision')
    plt.plot(percents, R, marker='o', label='Recall')
    plt.plot(percents, F1, marker='o', label='F1')
    plt.plot(percents, A, marker='o', label='Accuracy')
    plt.xlabel('Training Data (%)')
    plt.ylabel('Score')
    plt.ylim(0.0, 1.0)
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    if savepath:
        plt.savefig(savepath, bbox_inches='tight', dpi=140)
    plt.close()
    return {'precision': P, 'recall': R, 'f1': F1, 'accuracy': A}


# ------------------------
# HELPER: deterministic subsampling
# ------------------------

def take_percent(X: Sequence[Any], y: Sequence[int], pct: int, shuffle: bool = True, seed: int = 0) -> Tuple[List[Any], List[int]]:
    """
    Return first pct% of (X,y) after optional deterministic shuffle.
    Ensures at least 1 example if pct>0.
    """
    assert 0 < pct <= 100
    idx = list(range(len(X)))
    if shuffle:
        rnd = random.Random(seed)
        rnd.shuffle(idx)
    k = max(1, int(len(idx) * (pct/100.0)))
    sel = idx[:k]
    Xs = [X[i] for i in sel]
    ys = [y[i] for i in sel]
    return Xs, ys
