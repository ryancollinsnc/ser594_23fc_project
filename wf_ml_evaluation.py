import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data_processed/final_zillow_data_small.csv')

# Preprocessing steps
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

# Split the data into training and test sets
X = data.drop('Value', axis=1)
y = data['Value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load and evaluate each model
open('evaluation/summary.txt', 'w').close()
model_names = ['RandomForestRegressor', 'LinearRegression', 'Lasso', 'Ridge', 'DecisionTreeRegressor']
mse_results = []
r2_results = []
for name in model_names:
    model = joblib.load(f'models/{name}.pkl')
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    mse_results.append(mse)
    r2_results.append(r2)
    print(f'{name} - MSE: {mse}, R2 Score: {r2}')
    with open('evaluation/summary.txt', 'a') as file:
        file.write(f'{name} - MSE: {mse}, R2 Score: {r2}\n')

# Visualization
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# MSE plot
ax[0].bar(model_names, mse_results, color='skyblue')
ax[0].set_title('Mean Squared Error (MSE) Comparison')
ax[0].set_ylabel('MSE')

# R2 plot
ax[1].bar(model_names, r2_results, color='lightgreen')
ax[1].set_title('R2 Score Comparison')
ax[1].set_ylabel('R2 Score')

plt.tight_layout()
plt.savefig('visuals/models_bargraph.png')
plt.show()
