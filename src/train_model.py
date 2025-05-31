import pickle
from sklearn.model_selection import train_test_split
from preprocess import load_and_clean_data
import numpy as np
import xgboost as xgb

def train_and_save_model():
    df = load_and_clean_data()
    X = df[['Rooms', 'Bathroom', 'Landsize', 'Distance', 'YearBuilt']]
    y = df['Price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = xgb.XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=4)
    model.fit(X_train, y_train)

    # Save model to disk
    with open('model/model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("Model training complete and saved to model/model.pkl")

if __name__ == "__main__":
    train_and_save_model()

