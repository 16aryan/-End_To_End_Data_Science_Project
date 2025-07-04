from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Safely get form inputs (prevent crash on missing values)
            gender = request.form.get('gender')
            race_ethnicity = request.form.get('ethnicity')
            parental_level_of_education = request.form.get('parental_level_of_education')
            lunch = request.form.get('lunch')
            test_preparation_course = request.form.get('test_preparation_course')

            reading_score = float(request.form.get('reading_score') or 0)
            writing_score = float(request.form.get('writing_score') or 0)

            # Create data object
            data = CustomData(
                gender=gender,
                race_ethnicity=race_ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )

            # Convert to DataFrame
            pred_df = data.get_data_as_data_frame()
            print("Input DataFrame:", pred_df)

            # Make prediction
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            print("Prediction result:", results)

            return render_template('home.html', results=results[0])

        except Exception as e:
            # Display full error message on screen if something breaks
            return f"<h3>❌ Internal Server Error:</h3><pre>{str(e)}</pre>", 500

# Run the app with debug mode on
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)