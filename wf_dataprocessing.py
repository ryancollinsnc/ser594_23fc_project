import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data
df = pd.read_csv('data_original/zillow_data.csv')

# Initial inspection
print(df.head())

# Separate the non-date and date columns
non_date_cols = df.columns[:5]
date_cols = df.columns[5:]

# Separate the data into non-date and date DataFrames
non_date_df = df[non_date_cols]
date_df = df[date_cols].apply(pd.to_numeric, errors='coerce')

# Print initial missing values stats
print("Initial missing values count:")
print(date_df.isnull().sum())

# Interpolate missing values for the date columns (which should be numeric)
date_df.interpolate(method='linear', axis=1, inplace=True)

# Check missing values after interpolation
print("\nMissing values count after interpolation:")
print(date_df.isnull().sum())

# Combine the non-date and interpolated date data back together
cleaned_df = pd.concat([non_date_df, date_df], axis=1)

# Melt the DataFrame to transform it into a long format
melted_df = cleaned_df.melt(id_vars=non_date_cols.tolist(), 
                            var_name='Date', 
                            value_name='Value')

# We should ensure the 'Date' column contains only date-like strings before converting them to datetime
melted_df = melted_df[melted_df['Date'].str.match(r'\d{4}-\d{2}-\d{2}')]

# Now, Convert 'Date' column to datetime type
melted_df['Date'] = pd.to_datetime(melted_df['Date'], format='%Y-%m-%d')

# Print the cleaned and melted DataFrame
print(melted_df.head())

print(melted_df.info())

melted_df.dropna(inplace=True)

melted_df.to_csv('data_processing/final_zillow_data.csv', index=False)

import hashlib

def calculate_md5_hash(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(4096):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

# Load the dataset
file_path = 'data_processing/final_zillow_data.csv'
data = pd.read_csv(file_path)

# Specify the stratification column
stratify_col = 'StateName'  # Replace with your stratification column


# Perform stratified sampling to reduce the size of the dataset
# Adjust 'test_size' as needed to control the size of the reduced dataset
data_reduced, _ = train_test_split(data, test_size=0.9, stratify=data[stratify_col], random_state=42)

# Display the size of the original and the reduced datasets
print(f"Original Dataset Size: {data.shape[0]}")
print(f"Reduced Dataset Size: {data_reduced.shape[0]}")
data_reduced.to_csv('data_processed/final_zillow_data_small.csv', index=False)

# Replace with the actual file path
file_path = 'data_processing/final_zillow_data.csv'
md5 = calculate_md5_hash(file_path)
print(f"MD5 Hash: {md5}")
