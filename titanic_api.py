from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('titanic_model_new.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()

        # Prepare features for prediction (matching the trained model)
        features = np.array([
            float(data['Pclass']),
            float(data['Sex']),
            float(data['Age']),
            float(data['SibSp']),
            float(data['Parch']),
            float(data['Fare']),
            int(data['Embarked_Q']),
            int(data['Embarked_S'])
        ]).reshape(1, -1)

        # Make prediction using the trained model
        prediction = model.predict(features)
        
        # Return the prediction as JSON
        return jsonify({'survived': int(prediction[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
