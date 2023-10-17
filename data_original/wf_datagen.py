import pandas as pd
import requests
from io import StringIO

# List of URLs for scraping
urls = [
    "https://files.zillowstatic.com/research/public_csvs/zhvi/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv?t=1697437279",
    "https://files.zillowstatic.com/research/public_csvs/zhvi/State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv?t=1697437279",
    "https://files.zillowstatic.com/research/public_csvs/zhvi/Neighborhood_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv?t=1697437279",
    "https://files.zillowstatic.com/research/public_csvs/zhvi/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_month.csv?t=1697437279"
]

dfs = []  # A list to store DataFrames

for url in urls:
    # Sending a HTTP request to the URL and save the response
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Using StringIO to convert the text data into a file-like object so it can be read into a pandas dataframe
        data = StringIO(response.text)
        
        # Reading the data into a pandas dataframe
        df = pd.read_csv(data)
        
        # Adding the dataframe to the list of dataframes
        dfs.append(df)
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

# Concatenating all the dataframes in the list into a single dataframe
final_df = pd.concat(dfs, ignore_index=True)

# Printing the first 5 rows of the concatenated dataframe to the console
print(final_df.head())

# Saving the concatenated dataframe to a new CSV file
final_df.to_csv('zillow_data.csv', index=False)
