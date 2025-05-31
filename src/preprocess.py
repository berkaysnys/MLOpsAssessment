import pandas as pd

def load_and_clean_data(path='data/houseprice.csv'):
    df = pd.read_csv(path)
    df = df[['Rooms', 'Bathroom', 'Landsize', 'Distance', 'YearBuilt', 'Price']]
    df = df.dropna()
    return df
