from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("birthweight_predictor.pkl")
scaler = joblib.load("scaler.pkl")

# Define the features used during training
features = ['gestation', 'parity', 'age', 'height', 'weight', 'smoke']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        gestation = float(request.form['gestation'])
        parity = int(request.form['parity'])
        age = float(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        smoke = int(request.form['smoke'])

        # Feature engineering
        gestation_weeks = gestation / 7
        BMI = (weight * 703) / (height ** 2)

        # Create dataframe
        new_data = pd.DataFrame([{
            "gestation": gestation,
            "parity": parity,
            "age": age,
            "height": height,
            "weight": weight,
            "smoke": smoke,
        }])

        # Ensure column order matches training
        new_data = new_data[features]

        # Scale data
        new_data_scaled = scaler.transform(new_data)

        # Predict
        predicted_bwt = model.predict(new_data_scaled)[0]

        return render_template('index.html', prediction=f"Predicted Birthweight: {predicted_bwt:.2f} oz")

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
