# Weather and Climate Analytics

## Project Overview
This project analyzes historical weather data retrieved from a public REST API to identify temperature trends in Kochi, Kerala. The goal is to demonstrate API-based data extraction, data cleaning, and visualization using Python and matplotlib.

## Data Source 
The data was pulled from open-meteo.com (https://open-meteo.com), a free data source using GET request. The data pulled was in JSON format. 

## Construction of API url
The API url was constructed using the base url - https://archive-api.open-meteo.com and adding path and parameters as listed in the document - https://open-meteo.com/en/docs
Path - "v1/archive"
Parameters - latitude, longititude, start date, end date, max temperature, min temperature, precipitation amount and wind speed

## Data cleaning and parsing
- Parsing and cleaning of JSON data and its conversion to dataframe was done using Pandas.
- The dataframe was saved in CSV format in the local computer for later analysis and visualization.

## Data Analysis and Visualization using Matplotlib
- Cleaned weather data in CSV format was loaded into google colab for analysis and visualization
- Temperature trends and and its relationship with other attributes were plotted with the help of Matplotlib
- Detailed explanation of the analysis would be available in new documentation  
