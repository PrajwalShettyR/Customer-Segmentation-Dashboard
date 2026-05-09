from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA


def find_wcss(X):

    wcss = []

    for i in range(1, 11):

        kmeans = KMeans(
            n_clusters=i,
            random_state=42
        )

        kmeans.fit(X)

        wcss.append(kmeans.inertia_)

    return wcss


def apply_kmeans(X, k):

    model = KMeans(
        n_clusters=k,
        random_state=42
    )

    labels = model.fit_predict(X)

    return model, labels


def apply_hierarchical(X, k):

    model = AgglomerativeClustering(
        n_clusters=k
    )

    labels = model.fit_predict(X)

    return labels


def apply_pca(X):

    pca = PCA(n_components=2)

    transformed = pca.fit_transform(X)

    return transformed  