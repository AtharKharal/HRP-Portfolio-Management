# File: hrp/hrp.py
import numpy as np
import pandas as pd
from .distance import correl_dist
from .clustering import perform_clustering, get_quasi_diag
from .allocation import get_recursive_bisection


def hrp_allocation(returns, method='single'):
    """Compute HRP allocation."""
    corr = returns.corr()
    dist = correl_dist(corr)
    dist_vec = dist.values[np.triu_indices(dist.shape[0], k=1)]
    linkage = perform_clustering(dist_vec, method=method)
    sort_ix = get_quasi_diag(linkage)
    cov = returns.cov()
    hrp = get_recursive_bisection(cov, list(returns.columns[sort_ix]))
    return hrp

