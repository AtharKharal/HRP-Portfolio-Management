# Theoretical Foundations

## Mathematical Formulation

1. **Distance Matrix Construction**:
   Given the correlation matrix \( \mathbf{R} \), compute the distance matrix \( \mathbf{D} \):
   \[
   D_{i,j} = \sqrt{0.5 \cdot (1 - R_{i,j})}
   \]

2. **Hierarchical Clustering**:
   Apply an agglomerative clustering algorithm (e.g., single linkage) to \( \mathbf{D} \).

3. **Quasi-Diagonalization**:
   Reorder the covariance matrix \( \mathbf{\Sigma} \).

4. **Recursive Bisection and Allocation**:
   Allocate weights \( w \) such that:
   \[
   w_i = \frac{1}{\sigma_i} \Big/ \sum_{j \in \text{cluster}} \frac{1}{\sigma_j}
   \]
   where \( \sigma_i \) is the standard deviation of asset \( i \).
([hudsonthames.org](https://hudsonthames.org/an-introduction-to-the-hierarchical-risk-parity-algorithm/?utm_source=chatgpt.com))
