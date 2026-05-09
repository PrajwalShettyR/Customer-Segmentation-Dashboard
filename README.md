# Customer Segmentation Dashboard
A comprehensive Machine Learning based customer segmentation web application with K-Means clustering, PCA visualization, interactive analytics dashboard, and business insights generation.

## Description
An intelligent customer segmentation platform built with Python and Machine Learning. This application leverages K-Means clustering algorithms to automatically segment customers into distinct groups based on behavioral and demographic patterns. The dashboard provides interactive visualizations, PCA-based dimensional reduction analysis, and actionable business insights for targeted marketing strategies.

## Key Features

- K-Means clustering for customer segmentation
- PCA (Principal Component Analysis) visualization
- Interactive analytics dashboard
- Real-time customer insights generation
- Behavioral pattern analysis
- Demographic segmentation
- Business recommendations engine
- Data preprocessing and normalization
- Multiple clustering metrics and evaluation

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.7+ |
| ML Framework | Scikit-learn |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboard | Streamlit / Flask |
| Data Processing | Pandas, NumPy |
| Dimensionality Reduction | Scikit-learn PCA |
| Database | SQLite (optional) |
| Data Format | CSV, JSON |

## File Structure

```
Customer-Segmentation-Dashboard/
│
├── main.py                 # Main application entry point
├── segmentation.py         # K-Means clustering module
├── pca_analysis.py         # PCA visualization module
├── dashboard.py            # Interactive dashboard
├── data_preprocessing.py    # Data cleaning and normalization
├── insights_generator.py    # Business insights generation
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── data/                   # Data directory
│   ├── raw/                # Raw customer data
│   ├── processed/          # Cleaned and normalized data
│   ├── segments/           # Segmentation results
│   └── sample_data.csv     # Sample dataset
├── models/                 # Trained models directory
│   └── kmeans_model.pkl    # Serialized K-Means model
├── results/                # Output and results
│   ├── clusters.json       # Clustering results
│   ├── insights.json       # Generated insights
│   └── visualizations/     # Generated charts
├── logs/                   # Log files directory
│   └── app.log             # Application logs
├── README.md               # Project documentation
└── .gitignore              # Git ignore file
```

## Installation Instructions

### Prerequisites
- Python (v3.7 or higher)
- pip (Python package manager)
- Virtual environment (recommended)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/PrajwalShettyR/Customer-Segmentation-Dashboard.git
cd Customer-Segmentation-Dashboard
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage Examples

### Basic Usage
```bash
python main.py
```

### With Custom Arguments
```bash
python main.py --clusters 4 --algorithm kmeans --output json
```

### Available Options

| Option | Description | Default |
|--------|-------------|---------|
| --input | Input data file path | data/sample_data.csv |
| --clusters | Number of customer segments | 3 |
| --algorithm | Clustering algorithm | kmeans |
| --output | Output format (json, csv, html) | json |
| --visualize | Generate visualizations | True |
| --log-level | Logging level (DEBUG, INFO, WARNING) | INFO |

## Configuration

Edit `config.py` to customize segmentation parameters:

```python
# K-Means Configuration
NUM_CLUSTERS = 3
MAX_ITERATIONS = 300
RANDOM_STATE = 42
INIT_METHOD = 'k-means++'

# PCA Configuration
PCA_COMPONENTS = 2
EXPLAINED_VARIANCE_THRESHOLD = 0.95

# Data Preprocessing
NORMALIZE_DATA = True
HANDLE_OUTLIERS = True
OUTLIER_METHOD = 'iqr'  # 'iqr' or 'zscore'

# Logging
LOG_FILE = "logs/app.log"
LOG_LEVEL = "INFO"

# Output Settings
OUTPUT_DIR = "results/"
SAVE_MODELS = True
```

## Output Examples

### Console Output
```
=== Customer Segmentation Results ===

Clustering Summary:
  - Number of Clusters: 3
  - Algorithm: K-Means
  - Inertia: 1254.32
  - Silhouette Score: 0.652

Cluster Breakdown:
  Cluster 0: 156 customers (32.5%)
    - Avg Spending: $2,450
    - Avg Purchase Frequency: 12/year
    
  Cluster 1: 215 customers (44.8%)
    - Avg Spending: $1,800
    - Avg Purchase Frequency: 8/year
    
  Cluster 2: 109 customers (22.7%)
    - Avg Spending: $4,100
    - Avg Purchase Frequency: 18/year

PCA Variance Explained: 87.3%
```

### Dashboard Features
- Interactive cluster visualization
- Customer distribution charts
- Segment characteristics analysis
- Business insights and recommendations
- Export functionality for reports

## Running the Application

### Terminal Execution
```bash
# Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run segmentation
python main.py

# Run with custom parameters
python main.py --clusters 5 --output html --visualize

# Run dashboard
streamlit run dashboard.py  # if using Streamlit
```

## Future Enhancements

- [ ] Advanced clustering algorithms (DBSCAN, Hierarchical Clustering)
- [ ] Real-time data streaming integration
- [ ] REST API endpoints
- [ ] Web-based dashboard with authentication
- [ ] Automated customer profiling
- [ ] Predictive analytics for churn prediction
- [ ] Multi-language support
- [ ] Docker containerization
- [ ] Machine learning model versioning
- [ ] Performance optimization for large datasets

## Error Codes & Troubleshooting

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError: scikit-learn | Run `pip install -r requirements.txt` |
| No data found | Verify CSV file path in config or use `--input` parameter |
| Memory error on large datasets | Reduce data size or optimize preprocessing |
| PCA convergence issues | Adjust `EXPLAINED_VARIANCE_THRESHOLD` or normalize data |
| No visualizations generated | Check `VISUALIZE` setting and ensure matplotlib is installed |

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author

Created by **PrajwalShettyR**

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue in the repository or contact the maintainer.

## Acknowledgments

- Scikit-learn for ML algorithms
- Pandas for data manipulation
- Plotly for interactive visualizations
- The open-source community
