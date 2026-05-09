import pandas as pd


def generate_insights(df, labels):

    df['Cluster'] = labels

    grouped = df.groupby('Cluster').mean(
        numeric_only=True
    )

    insights = []

    for cluster, row in grouped.iterrows():

        income = row['Annual Income (k$)']

        spending = row['Spending Score (1-100)']

        if income > 60 and spending > 60:

            category = 'Premium Customers'

            recommendation = (
                'Offer loyalty rewards'
            )

        elif income > 60 and spending < 40:

            category = 'Potential Customers'

            recommendation = (
                'Target with promotions'
            )

        elif income < 40 and spending > 60:

            category = 'Impulsive Buyers'

            recommendation = (
                'Use limited-time offers'
            )

        else:

            category = 'Low Value Customers'

            recommendation = (
                'Use budget campaigns'
            )

        insights.append({
            'Cluster': cluster,
            'Category': category,
            'Recommendation': recommendation
        })

    return pd.DataFrame(insights)