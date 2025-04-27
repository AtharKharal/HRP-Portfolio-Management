
# File: run_hrp.py
import pandas as pd
from hrp.hrp import hrp_allocation

# Example: Load return data
# Replace this with your actual return matrix (e.g., stock daily returns)
data = pd.read_csv('returns.csv', index_col=0, parse_dates=True)

# Compute HRP weights
weights = hrp_allocation(data)
print("\nHRP Portfolio Weights:\n", weights)

# Normalize to ensure full investment
weights /= weights.sum()
print("\nNormalized HRP Portfolio Weights:\n", weights)
