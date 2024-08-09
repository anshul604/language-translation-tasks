# data_preparation.py
import pandas as pd

def load_data():
    file_path = 'Desktop/task_3/data/eng_hindi.csv'  # File path
    try:
        df = pd.read_csv(file_path)
        print("CSV file loaded successfully.")
        print("Columns in DataFrame:", df.columns)
        
        # Strip any whitespace from column names
        df.columns = df.columns.str.strip()
        
        if 'English' not in df.columns or 'Hindi' not in df.columns:
            raise ValueError("CSV file must contain 'English' and 'Hindi' columns.")
        
        # Handle missing values
        df.dropna(inplace=True)
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
