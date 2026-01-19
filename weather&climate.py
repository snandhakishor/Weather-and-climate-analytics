
# importing libraries
import requests
import pandas as pd

# documents: https://open-meteo.com/en/docs
url = "https://archive-api.open-meteo.com/v1/archive?latitude=9.9312&longitude=76.2673"

# defining extra parameters as per the variables listed in the documents
params = {
    'start_date' : '2022-01-01',
    'end_date' : '2025-12-31',
    "daily": ",".join([
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "windspeed_10m_max"
    ])
}
response = requests.get(url, params=params).json()
print(response)
# converting to pandas dataframe
df = pd.DataFrame(response['daily'])

# date column conversion
df['time'] = pd.to_datetime(df['time'], errors="coerce")

# print(df.dtypes)
# print(df.head())

# saving as csv
file = df.to_csv(r"C:\Users\ADMIN\PycharmProjects\PythonProject4\data\cleaned_weatherdata.csv", index=False)
