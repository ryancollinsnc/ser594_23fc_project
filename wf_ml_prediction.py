# wf_ml_prediction.py
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

def preprocess_input(input_data, training_data):
    df = pd.DataFrame([input_data])
    df.fillna(df.mean(), inplace=True)
    df['Year'] = pd.to_datetime(df['Date']).dt.year
    df['Month'] = pd.to_datetime(df['Date']).dt.month
    df.drop(['Date', 'RegionID'], axis=1, inplace=True)

    label_encoders = {}
    for col in ['RegionName', 'RegionType', 'StateName']:
        if col in df:
            le = LabelEncoder()
            le.fit(training_data[col])
            df[col] = le.transform(df[col])
            label_encoders[col] = le

    return df

# Function to make predictions using a given model
def make_prediction(model, input_data):
    """
    Makes predictions using the given model on the provided input data.

    :param model: The trained model to use for making predictions.
    :param input_data: The DataFrame containing the preprocessed data on which predictions are to be made.
    :return: Predictions made by the model.
    """
    prediction = model.predict(input_data)
    return prediction

# Load the training data (for label encoding)
training_data = pd.read_csv('data_processed/final_zillow_data_small.csv')

# Sample input data
sample_input = {
    'RegionID': 809312,
    'SizeRank': 21497,
    'RegionName': 'Seneca Falls',
    'RegionType': 'neighborhood',
    'StateName': 'NV',
    'Date': '2010-12-31'
}

# Preprocess the input data
preprocessed_input = preprocess_input(sample_input, training_data)

# Load a model and make a prediction
model = joblib.load('models/RandomForestRegressor.pkl')
result = make_prediction(model, preprocessed_input)
print(f"Prediction: {result}")
print(f"Actual Value: [{training_data['Value'][0]}]")

sample_input = {
    'RegionID': 40981,
    'SizeRank': 348,
    'RegionName': 'South Miami Heights',
    'RegionType': 'neighborhood',
    'StateName': 'FL',
    'Date': '2017-10-31'
}
preprocessed_input = preprocess_input(sample_input, training_data)

# Load a model and make a prediction
model = joblib.load('models/RandomForestRegressor.pkl')
result = make_prediction(model, preprocessed_input)
print(f"Prediction: {result}")
print(f"Actual Value: [{training_data['Value'][1]}]")