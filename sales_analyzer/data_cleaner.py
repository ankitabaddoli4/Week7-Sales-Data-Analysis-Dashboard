import numpy as np

def clean_data(df):
    """
    Clean dataset: remove duplicates, handle missing values, fix types
    """
    if df is None:
        return None

    print("\n🧹 Cleaning Data...")

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"Removed {before - after} duplicate rows")

    # Handle missing values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    # Fill numeric with median
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].median(), inplace=True)

    # Fill categorical with mode
    for col in categorical_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].mode()[0], inplace=True)

    # Convert date column
    if 'order_date' in df.columns:
        df['order_date'] = df['order_date'].astype('datetime64')

    print("✅ Data Cleaning Completed")
    return df