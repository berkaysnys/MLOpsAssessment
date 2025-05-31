import pandas as pd

def predict_price(model, input_data: dict):
    df = pd.DataFrame([input_data])
    return model.predict(df)[0]

