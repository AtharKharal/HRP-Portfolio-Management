# File: hrp/clustering.py
import scipy.cluster.hierarchy as sch


def perform_clustering(dist_matrix, method='single'):
    """Perform hierarchical clustering."""
    linkage = sch.linkage(dist_matrix, method=method)
    return linkage


def get_quasi_diag(linkage):
    """Get order of clustered items."""
    link = linkage.astype(int)
    sort_ix = pd.Series([link[-1, 0], link[-1, 1]])
    num_items = link[-1, 3]
    while sort_ix.max() >= num_items:
        sort_ix.index = range(0, sort_ix.shape[0] * 2, 2)
        df0 = sort_ix[sort_ix >= num_items]
        i = df0.index
        j = df0.values - num_items
        sort_ix[i] = link[j, 0]
        df1 = pd.Series(link[j, 1], index=i + 1)
        sort_ix = pd.concat([sort_ix, df1])
        sort_ix = sort_ix.sort_index()
    return sort_ix.tolist()


