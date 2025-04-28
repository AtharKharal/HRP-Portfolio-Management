# Implementation Details

## Code Structure

- **`hrp/distance.py`**: Computes the distance matrix from the correlation matrix.
- **`hrp/clustering.py`**: Performs hierarchical clustering.
- **`hrp/quasi_diag.py`**: Reorders the covariance matrix.
- **`hrp/recursive_bisection.py`**: Implements recursive bisection.
- **`run_hrp.py`**: Main script to run HRP.

## Usage Example

```python
from hrp import run_hrp

# Load returns data
returns = load_returns('returns.csv')

# Compute correlation and covariance matrices
corr = returns.corr()
cov = returns.cov()

# Run HRP algorithm
weights = run_hrp(cov, corr)

print(weights)
```
