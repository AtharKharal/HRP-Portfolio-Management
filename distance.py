# File: hrp/distance.py
import numpy as np

def correl_dist(corr):
    """Compute distance matrix from correlation matrix."""
    return np.sqrt(0.5 * (1 - corr))
