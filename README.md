# MLOpsAssessment - House Price Prediction

## Project Overview
This project is part of an MLOps assessment. It predicts house prices using data from the Melbourne Housing Market dataset. The core of the project includes a machine learning model (XGBoost) trained to predict housing prices based on specific features, deployed via a Flask web application.

---

## Features Used for Prediction

The model was trained using the following features:

- `Rooms` – Number of rooms
- `Bathroom` – Number of bathrooms
- `Landsize` – Size of land in square meters
- `Distance` – Distance from Central Business District
- `YearBuilt` – Year the house was built

---

## Model

- **Type**: XGBoost Regressor
- **Input**: A JSON or form input with the 5 features listed above
- **Output**: Predicted house price (float)

---

## Repository Structure

- `data/` — Raw dataset files 
- `src/` — Source code for preprocessing, training, and prediction  
- `app/` — Flask API code  
- `model/` — Saved model file (`model.pkl`)  
- `tests/` — Unit tests  
- `.github/workflows/` — GitHub Actions CI/CD pipelines  
- `Dockerfile` — For containerizing the app  
- `requirements.txt` — Python dependencies
- `README.md` — This file 

