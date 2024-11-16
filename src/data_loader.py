import pandas as pd

def load_data(filepath):
    """Load the dataset from a CSV file and perform basic preprocessing."""
    data = pd.read_csv(filepath)
    # Drop any rows with missing values (adjust based on data needs)
    data.dropna(inplace=True)
    return data
