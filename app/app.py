from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        Rooms = int(request.form['Rooms'])
        Bathroom = int(request.form['Bathroom'])
        Landsize = int(request.form['Landsize'])
        Distance = float(request.form['Distance']) 
        YearBuilt = int(request.form['YearBuilt'])
    except (ValueError, KeyError):
        return "Invalid input", 400

    features = np.array([Rooms, Bathroom, Landsize, Distance, YearBuilt]).reshape(1, -1)

    prediction = model.predict(features)[0]
    price = round(prediction, 2)

    return render_template('results.html', price=price)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

