COLUMN_DESCRIPTIONS = {
  "age": "Age of the patient in years",
  "sex": "Patient sex, encoded as 0 or 1",
  "cp": "Chest pain type",
  "trestbps": "Resting blood pressure in mm Hg",
  "chol": "Serum cholesterol in mg/dl",
  "fbs": "Fasting blood sugar greater than 120 mg/dl",
  "restecg": "Resting electrocardiographic results",
  "thalach": "Maximum heart rate achieved",
  "exang": "Exercise induced angina",
  "oldpeak": "ST depression induced by exercise relative to rest",
  "slope": "Slope of the peak exercise ST segment",
  "ca": "Number of major vessels colored by fluoroscopy",
  "thal": "Thalassemia result",
  "num": "Heart disease diagnosis"
}

def get_column_description(column):
  return COLUMN_DESCRIPTIONS.get(column, "No description available")