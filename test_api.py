import requests

# Sample data matching the feature order used in training
TEST_DATA = {
    "Pclass": 3,
    "Sex": 1,
    "Age": 25,
    "SibSp": 0,
    "Parch": 0,
    "Fare": 7.25,
    "Embarked_Q": 0,
    "Embarked_S": 1
}

# Send a POST request to the Flask prediction endpoint
response = requests.post(
    "http://127.0.0.1:5000/predict",
    json=TEST_DATA,
    headers={"Content-Type": "application/json"}
)

# Print the status code and response data
print("Status Code:", response.status_code)
print("Response:", response.json())
