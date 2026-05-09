import matplotlib.pyplot as plt
import seaborn as sns


def plot_elbow(wcss):

    fig, ax = plt.subplots()

    ax.plot(
        range(1, 11),
        wcss,
        marker='o'
    )

    ax.set_title('Elbow Method')

    ax.set_xlabel('Number of Clusters')

    ax.set_ylabel('WCSS')

    return fig


def plot_clusters(pca_data, labels):

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.scatterplot(
        x=pca_data[:, 0],
        y=pca_data[:, 1],
        hue=labels,
        palette='Set2',
        s=100,
        ax=ax
    )

    ax.set_title('Customer Segments')

    return fig