from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)

file_path = 'Specialist.xlsx'
data = pd.read_excel(file_path)

def preprocess_data(data):
    if data.columns[0].startswith('Unnamed'):
        data = data.drop(columns=[data.columns[0]])
    data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]
    return data

data_cleaned = preprocess_data(data)

import numpy as np

def recommend_specialist(input_symptoms, data):
    input_symptoms = [symptom.strip().lower().replace(' ', '_') for symptom in input_symptoms if symptom.strip()]

    invalid_symptoms = [symptom for symptom in input_symptoms if symptom not in data.columns]
    if invalid_symptoms:
        return {'error': f"Invalid symptoms: {', '.join(invalid_symptoms)}"}

    matching_specialists = []
    for idx, row in data.iterrows():
        if all(row.get(symptom, 0) == 1 for symptom in input_symptoms):
            matching_specialists.append(row['disease'])

    if not matching_specialists:
        return {'error': "No specialists found for the given symptoms."}
    
    return {'recommendations': list(set(matching_specialists))}


@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    if request.method == 'POST':
        symptoms = request.form.get('symptoms')
        input_symptoms = [symptom.strip() for symptom in symptoms.split(",")]
        try:
            recommendations = recommend_specialist(input_symptoms, data_cleaned)
        except ValueError as e:
            return render_template('index.html', error=str(e))
    
    return render_template('index.html', recommendations=recommendations)


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('query').lower()
    suggestions = [col.replace('_', ' ') for col in data_cleaned.columns if query in col]
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)
