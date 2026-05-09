# Customer Segmentation Dashboard

A Machine Learning based customer segmentation web application built using K-Means clustering, PCA visualization, and interactive business analytics.

---

## Description

Customer segmentation is an important technique used by retail businesses to understand customer behavior and improve marketing strategies.

This project uses Machine Learning algorithms to group customers into different segments based on:

- Age
- Annual Income
- Spending Score
- Purchase Frequency

The application provides an interactive dashboard with clustering visualizations, PCA analysis, business insights, and customer behavior analytics.

---

# Features

- K-Means Clustering
- Elbow Method Analysis
- PCA Visualization
- Hierarchical Clustering Comparison
- Interactive Dashboard using Streamlit
- Business Insights Generation
- Cluster Profile Analytics
- 3D Customer Visualization
- Downloadable Insights Report
- Dark Theme Dashboard UI

---

# Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly, Matplotlib, Seaborn |
| Clustering Algorithm | K-Means |
| Dimensionality Reduction | PCA |
| Version Control | Git & GitHub |

---

# Dataset Used

Primary Dataset:

- Mall Customer Segmentation Dataset

Dataset Features:
- Customer ID
- Gender
- Age
- Annual Income
- Spending Score

Additional Feature:
- Purchase Frequency (generated for behavioral analysis)

Dataset Source:
https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

---

# Project Structure

```bash
ML Project/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   └── Mall_Customers.csv
│
└── src/
    ├── preprocessing.py
    ├── clustering.py
    ├── visualization.py
    └── insights.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-segmentation-dashboard.git
```

## Move Into Project Directory

```bash
cd customer-segmentation-dashboard
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Dashboard Features

## 1. Elbow Method
Used to determine the optimal number of clusters.

## 2. PCA Visualization
Reduces dimensions for easier cluster visualization.

## 3. Customer Segmentation
Groups customers into different behavioral categories.

## 4. Cluster Profile Analytics
Displays average values for:
- Age
- Income
- Spending Score
- Purchase Frequency

## 5. 3D Customer Visualization
Interactive 3D graph for customer analysis.

## 6. Business Insights
Generates marketing recommendations based on customer behavior.

---

# Customer Categories

The system identifies customer groups such as:

- Premium Customers
- Potential Customers
- Impulsive Buyers
- Low Value Customers

---

# Machine Learning Concepts Used

- Unsupervised Learning
- K-Means Clustering
- Euclidean Distance
- Cluster Centroids
- PCA (Principal Component Analysis)
- Hierarchical Clustering

---

# Future Improvements

- Real-time customer analytics
- Advanced clustering algorithms
- Automated report generation
- Deployment using cloud platforms
- Better recommendation engine
- Live database integration

---



## Author

Created by **[PrajwalShettyR](https://github.com/PrajwalShettyR)**

---

## Support

For issues, questions, or suggestions, please open an [issue](https://github.com/PrajwalShettyR/System-Performance-Monitor/issues) in the repository.
