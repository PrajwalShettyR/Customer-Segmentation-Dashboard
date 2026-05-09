import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

from src.preprocessing import preprocess_data

from src.clustering import (
    find_wcss,
    apply_kmeans,
    apply_hierarchical,
    apply_pca
)

from src.insights import generate_insights


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title='Customer Segmentation Dashboard',
    page_icon='📊',
    layout='wide'
)


# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Main Background */
.main {
    background-color: #0f1117;
    padding-top: 20px;
}

/* Titles */
h1 {
    color: white;
    margin-bottom: 20px;
}

h2, h3 {
    color: white;
    margin-top: 40px;
    margin-bottom: 20px;
}

/* Metric Cards */
div[data-testid="metric-container"] {
    background-color: #1e222d;
    border: 1px solid #333;
    padding: 20px;
    border-radius: 14px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161a23;
}

/* Dataframes */
[data-testid="stDataFrame"] {
    padding-top: 10px;
    padding-bottom: 20px;
}

/* Graph Spacing */
.plot-container {
    padding-top: 10px;
    padding-bottom: 25px;
}

/* Horizontal Line */
hr {
    margin-top: 35px;
    margin-bottom: 35px;
    border: 1px solid #2c2f36;
}

/* Buttons */
.stButton button,
.stDownloadButton button {
    border-radius: 10px;
    padding: 10px 18px;
}

/* General spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ---------------- #

st.sidebar.title('Customer Segmentation')

uploaded_file = st.sidebar.file_uploader(
    'Upload CSV File',
    type=['csv']
)

k = st.sidebar.slider(
    'Select Number of Clusters',
    2,
    10,
    5
)


# ---------------- TITLE ---------------- #

st.title('📊 Customer Segmentation Dashboard')

st.markdown(
    'Analyze retail customer behavior using K-Means clustering and Machine Learning.'
)


# ---------------- MAIN APP ---------------- #

if uploaded_file:

    with st.spinner('Processing Dataset...'):

        df = pd.read_csv(uploaded_file)

        # Dataset Preview
        st.subheader('Dataset Preview')

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        st.markdown("---")

        # Preprocessing
        X_scaled, processed_df = preprocess_data(df)

        # Elbow Method
        st.subheader('Elbow Method Analysis')

        wcss = find_wcss(X_scaled)

        elbow_df = pd.DataFrame({
            'Clusters': list(range(1, 11)),
            'WCSS': wcss
        })

        elbow_fig = px.line(
            elbow_df,
            x='Clusters',
            y='WCSS',
            markers=True,
            height=350
        )

        st.plotly_chart(
            elbow_fig,
            use_container_width=True
        )

        # Suggested K
        suggested_k = np.argmin(np.diff(wcss)) + 2

        st.info(
            f'Suggested Optimal Clusters: {suggested_k}'
        )

        st.markdown("---")

        # Apply K-Means
        model, labels = apply_kmeans(
            X_scaled,
            k
        )

        processed_df['Cluster'] = labels

        # Cluster Naming
        cluster_names = {}

        grouped = processed_df.groupby('Cluster').mean(
            numeric_only=True
        )

        for cluster, row in grouped.iterrows():

            income = row['Annual Income (k$)']
            spending = row['Spending Score (1-100)']

            if income > 60 and spending > 60:
                cluster_names[cluster] = 'Premium Customers'

            elif income > 60 and spending < 40:
                cluster_names[cluster] = 'Potential Customers'

            elif income < 40 and spending > 60:
                cluster_names[cluster] = 'Impulsive Buyers'

            else:
                cluster_names[cluster] = 'Low Value Customers'

        processed_df['Category'] = processed_df[
            'Cluster'
        ].map(cluster_names)

        # PCA
        pca_data = apply_pca(X_scaled)

        pca_df = pd.DataFrame({
            'PCA1': pca_data[:, 0],
            'PCA2': pca_data[:, 1],
            'Category': processed_df['Category']
        })

        # Metrics
        col1, col2, col3 = st.columns(3)

        col1.metric(
            'Customers',
            len(df)
        )

        col2.metric(
            'Clusters',
            k
        )

        col3.metric(
            'Features',
            4
        )

        st.markdown("---")

        # PCA Visualization
        st.subheader('Customer Segments')

        cluster_fig = px.scatter(
            pca_df,
            x='PCA1',
            y='PCA2',
            color='Category',
            height=500,
            title='PCA-Based Customer Segmentation'
        )

        st.plotly_chart(
            cluster_fig,
            use_container_width=True
        )

        st.markdown("---")

        # Cluster Distribution
        st.subheader('Cluster Distribution')

        cluster_counts = processed_df[
            'Category'
        ].value_counts().reset_index()

        cluster_counts.columns = [
            'Category',
            'Count'
        ]

        bar_fig = px.bar(
            cluster_counts,
            x='Category',
            y='Count',
            color='Category',
            height=350
        )

        st.plotly_chart(
            bar_fig,
            use_container_width=True
        )

        st.markdown("---")

        # Cluster Profile Table
        st.subheader('Cluster Profile Analytics')

        profile_table = processed_df.groupby(
            'Category'
        )[
            [
                'Age',
                'Annual Income (k$)',
                'Spending Score (1-100)',
                'Purchase Frequency'
            ]
        ].mean().round(2)

        st.dataframe(
            profile_table,
            use_container_width=True
        )

        st.markdown("---")

        # 3D Graph
        st.subheader('3D Customer Visualization')

        graph_3d = px.scatter_3d(
            processed_df,
            x='Annual Income (k$)',
            y='Spending Score (1-100)',
            z='Purchase Frequency',
            color='Category',
            height=650
        )

        st.plotly_chart(
            graph_3d,
            use_container_width=True
        )

        st.markdown("---")

        # Business Insights
        st.subheader('Business Insights')

        insights_df = generate_insights(
            processed_df,
            labels
        )

        st.dataframe(
            insights_df,
            use_container_width=True
        )

        # Recommendation Cards
        st.subheader('Marketing Recommendations')

        for _, row in insights_df.iterrows():

            st.success(
                f"{row['Category']} → {row['Recommendation']}"
            )

        st.markdown("---")

        # Download Button
        csv = insights_df.to_csv(index=False)

        st.download_button(
            label='Download Insights CSV',
            data=csv,
            file_name='customer_insights.csv',
            mime='text/csv'
        )

        st.markdown("---")

        # Hierarchical Clustering
        st.subheader(
            'Hierarchical Clustering Comparison'
        )

        hierarchical_labels = apply_hierarchical(
            X_scaled,
            k
        )

        hierarchical_df = pd.DataFrame({
            'PCA1': pca_data[:, 0],
            'PCA2': pca_data[:, 1],
            'Cluster': hierarchical_labels.astype(str)
        })

        hierarchical_fig = px.scatter(
            hierarchical_df,
            x='PCA1',
            y='PCA2',
            color='Cluster',
            height=500,
            title='Hierarchical Clustering Visualization'
        )

        st.plotly_chart(
            hierarchical_fig,
            use_container_width=True
        )