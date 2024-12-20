from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Sample model (Replace with your actual trained model)
# For simplicity, a random forest classifier is used here
model = RandomForestClassifier(random_state=42)

# Sample customer data for model training (Replace with your actual dataset)
# Sample features: age, tenure, monthly_charge, gender
data = pd.DataFrame({
    'age': [25, 30, 45, 50],
    'tenure': [12, 24, 36, 48],
    'monthly_charge': [50, 70, 100, 120],
    'gender': ['Male', 'Female', 'Male', 'Female']
})
y = [0, 1, 0, 1]  # Labels: 0 - not churned, 1 - churned

# Preprocessing: Label encoding for categorical features
le = LabelEncoder()
data['gender'] = le.fit_transform(data['gender'])

# Train the model
model.fit(data, y)

# Define the API endpoint to accept customer details and return churn probabilities
@app.route('/predict_churn', methods=['POST'])
def predict_churn():
    try:
        # Get customer data from the request body
        input_data = request.get_json()

        # Extract features from the input
        age = input_data['age']
        tenure = input_data['tenure']
        monthly_charge = input_data['monthly_charge']
        gender = input_data['gender']

        # Preprocess the gender feature (label encode)
        gender_encoded = le.transform([gender])[0]

        # Create a DataFrame for prediction
        input_df = pd.DataFrame([[age, tenure, monthly_charge, gender_encoded]], columns=['age', 'tenure', 'monthly_charge', 'gender'])

        # Predict churn probability (class probability)
        churn_probability = model.predict_proba(input_df)[0][1]  # Probability of class 1 (churned)

        # Return the churn probability as a JSON response
        return jsonify({'churn_probability': churn_probability})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
