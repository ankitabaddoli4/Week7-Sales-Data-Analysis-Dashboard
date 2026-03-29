import pandas as pd

def load_data(file_path):
    """
    Load data from CSV or Excel file
    """
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")

        print(f"✅ Data Loaded Successfully: {df.shape}")
        return df

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None