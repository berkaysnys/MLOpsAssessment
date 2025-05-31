import pytest
import pandas as pd
from train_model import train_and_save_model
import pickle
import os
from predict import predict_price
import numpy as np

def test_train_and_save_model():
    train_and_save_model()
    assert os.path.exists('model/model.pkl')

def test_model_prediction():
    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f)

    input_data = {'Rooms': 3, 'Bathroom': 2, 'Landsize': 150, 'Distance':2.5, 'YearBuilt':2010}
    prediction = predict_price(model, input_data)

    assert isinstance(prediction, float) or isinstance(prediction, (int, np.number))
    assert prediction > 0

