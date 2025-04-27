# File: hrp/allocation.py
import numpy as np
import pandas as pd


def get_cluster_var(cov, items):
    """Compute cluster variance."""
    cov_ = cov.loc[items, items]
    w_ = get_ivp(cov_).reshape(-1, 1)
    return (w_.T @ cov_.values @ w_)[0, 0]


def get_ivp(cov):
    """Compute inverse-variance portfolio."""
    ivp = 1. / np.diag(cov)
    ivp /= ivp.sum()
    return ivp


def get_recursive_bisection(cov, sort_ix):
    """Compute HRP weights."""
    w = pd.Series(1, index=sort_ix)
    clusters = [sort_ix]
    while len(clusters) > 0:
        clusters = [cluster[i:j] for cluster in clusters
                    for i, j in ((0, len(cluster) // 2), (len(cluster) // 2, len(cluster))) if len(cluster) > 1]
        for cluster in clusters:
            c_items_0 = cluster[:len(cluster) // 2]
            c_items_1 = cluster[len(cluster) // 2:]
            var_0 = get_cluster_var(cov, c_items_0)
            var_1 = get_cluster_var(cov, c_items_1)
            alpha = 1 - var_0 / (var_0 + var_1)
            w[c_items_0] *= alpha
            w[c_items_1] *= 1 - alpha
    return w


