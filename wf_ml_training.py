import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.tree import DecisionTreeRegressor  # Import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load and preprocess the data
data = pd.read_csv('data_processed/final_zillow_data_small.csv')
data.fillna(data.mean(), inplace=True)
data['Year'] = pd.to_datetime(data['Date']).dt.year
data['Month'] = pd.to_datetime(data['Date']).dt.month
data.drop(['Date', 'RegionID'], axis=1, inplace=True)

# Label encoding for categorical variables
label_encoders = {}
for col in ['RegionName', 'RegionType', 'StateName']:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Split the data
X = data.drop('Value', axis=1)
y = data['Value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and train models
models = {
    'RandomForestRegressor': RandomForestRegressor(),
    'LinearRegression': LinearRegression(),
    'Lasso': Lasso(),
    'Ridge': Ridge(),
    'DecisionTreeRegressor': DecisionTreeRegressor()
}

# Train and save each model
for name, model in models.items():
    model.fit(X_train, y_train)
    joblib.dump(model, f'models/{name}.pkl')
