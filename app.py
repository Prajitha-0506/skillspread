import pickle
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model and the skill vectorizer
try:
    with open('job_role_predictor.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('skill_vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
except FileNotFoundError:
    model = None
    vectorizer = None
    print("Model or vectorizer files not found!")

# Create an API endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    if model is None or vectorizer is None:
        return jsonify({'error': 'Model not loaded properly'}), 500

    # Get the data from the POST request (e.g., {"skills": "python, java, machine learning"})
    data = request.get_json(force=True)
    skills_text = data.get('skills', '')

    if not skills_text:
        return jsonify({'error': 'Skills not provided'}), 400
    
    # 1. Transform the input skills using the loaded vectorizer
    features = vectorizer.transform([skills_text])
    
    # 2. Make a prediction using the loaded model
    prediction = model.predict(features)
    
    # 3. Return the prediction as a JSON response
    return jsonify(predicted_job_role=prediction[0])

if __name__ == '__main__':
    # Use 0.0.0.0 to make it accessible on the network
    app.run(host='0.0.0.0', port=8080)