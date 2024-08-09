import pandas as pd

def load_data(file_path):
    """Load dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path, encoding='utf-8', usecols=['English', 'French', 'Hindi'])
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    return data
