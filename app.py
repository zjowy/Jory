from flask import Flask, request, render_template
import numpy as np
import joblib
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
#pipe= pickle.load(open('/Users/shatha/Prog yogesh/our finalised model.pickle','rb'))
app = Flask(__name__, static_folder='static')

# Load the trained Random Forest model and scaler
rf_model = joblib.load('rf_model.joblib')
scaler = joblib.load('scaler.joblib')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        # Get input features fropm the form
        features = [
            float(request.form['Purchases']),
            float(request.form['bTotal']),
            float(request.form['bSolar']),
            float(request.form['bNonSolar']),
            float(request.form['bHydro']),
            float(request.form['mcvTotal']),
            float(request.form['mcvSolar']),
            float(request.form['mcvNonsolar']),
            float(request.form['mcvHydro']),
            float(request.form['fsvTotal']),
            float(request.form['fsvSolar']),
            float(request.form['fsvNonSolar']),
            float(request.form['fsvHydro'])
        ]

        # Scale the input features
        features_scaled = scaler.transform([features])

        # Make prediction
        prediction = rf_model.predict(features_scaled)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)