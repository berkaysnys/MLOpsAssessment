import pytest
from preprocess import load_and_clean_data

def test_load_and_clean_data():
    df = load_and_clean_data()
    assert not df.empty

    #Checking for column names
    expected_cols = ['Rooms', 'Bathroom', 'Landsize', 'Distance', 'YearBuilt', 'Price']
    assert list(df.columns) == expected_cols

    #No missing values
    assert df.isnull().sum().sum() == 0

