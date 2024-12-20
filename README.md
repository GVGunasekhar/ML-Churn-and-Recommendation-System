Churn Prediction API
This project provides a Flask API for predicting customer churn based on customer details like age, tenure, monthly charge, and gender. The API uses a pre-trained machine learning model to predict the likelihood of a customer churning (leaving the service).

Table of Contents
Prerequisites
Setting Up the Project
Running the Flask App Locally
Testing the API
Sample Request and Response
Prerequisites
Before running the API, ensure you have the following installed:

Python 3.x: Download Python
Flask: A micro web framework for Python.
scikit-learn: Machine learning library.
Pandas: For data handling and manipulation.
NumPy: For numerical operations.
You can install the required dependencies by running the following command in your terminal or command prompt:

bash
Copy code
pip install flask numpy pandas scikit-learn
Setting Up the Project
Clone the repository (or download the code) to your local machine.
Save the Python code for the Flask app in a file named app.py.
Example project directory:
bash
Copy code
/ChurnPrediction
    ├── app.py
    └── requirements.txt
In the requirements.txt file, add the dependencies:
txt
Copy code
flask
numpy
pandas
scikit-learn
Running the Flask App Locally
Open your terminal or command prompt.
Navigate to the folder containing the app.py file:
bash
Copy code
cd path/to/ChurnPrediction
Run the Flask app using the following command:
bash
Copy code
python app.py
You should see output indicating that the Flask development server is running, typically on http://127.0.0.1:5000.

Sample Output:
bash
Copy code
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
The API is now running locally on http://127.0.0.1:5000.

Testing the API
You can test the API locally using Postman, cURL, or any HTTP client that supports POST requests.

Testing with Postman
Open Postman (Download it here if you don’t have it).
Set the HTTP method to POST.
Enter the URL: http://127.0.0.1:5000/predict_churn.
In the Body tab, select raw and choose JSON from the dropdown menu.
Paste the following JSON object in the request body:
json
Copy code
{
  "age": 35,
  "tenure": 24,
  "monthly_charge": 50,
  "gender": "Male"
}
Click Send.
Expected Response:
json
Copy code
{
  "churn_probability": 0.42
}
The response contains the predicted churn probability for the given customer details.

Testing with cURL
Alternatively, you can use cURL to test the API from your command line.

Run the following command in your terminal:

bash
Copy code
curl -X POST http://127.0.0.1:5000/predict_churn -H "Content-Type: application/json" -d '{
  "age": 35,
  "tenure": 24,
  "monthly_charge": 50,
  "gender": "Male"
}'
You should see the churn probability response in the terminal:

json
Copy code
{
  "churn_probability": 0.42
}
Sample Request and Response
Request
Send a POST request to http://127.0.0.1:5000/predict_churn with the following JSON body:

json
Copy code
{
  "age": 35,
  "tenure": 24,
  "monthly_charge": 50,
  "gender": "Male"
}
Response
The response will return the churn probability as a JSON object:

json
Copy code
{
  "churn_probability": 0.42
}
Conclusion
You have successfully set up the Flask API for churn prediction and tested it locally using Postman or cURL. This API can be further extended or deployed to cloud platforms like Heroku, AWS, or Google Cloud for production use.