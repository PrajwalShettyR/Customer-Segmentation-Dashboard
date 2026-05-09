import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def load_data(path):
    df = pd.read_csv(path)
    return df


def preprocess_data(df):

    # Convert Gender to numeric
    df['Gender'] = df['Gender'].map({
        'Male': 0,
        'Female': 1
    })

    # Create Purchase Frequency column
    df['Purchase Frequency'] = (
        df['Spending Score (1-100)'] / 10
    ).astype(int) + np.random.randint(1, 5, len(df))

    # Features used for clustering
    features = [
        'Age',
        'Annual Income (k$)',
        'Spending Score (1-100)',
        'Purchase Frequency'
    ]

    X = df[features]

    # Feature Scaling
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, df