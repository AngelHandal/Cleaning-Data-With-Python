import pandas as pd
import os

# Get a list of all .csv files in the current folder
csv_files = [f for f in os.listdir() if f.endswith('.csv')]

# Read each .csv file and modify it as indicated
for file in csv_files:
    df = pd.read_csv(file)
    # Convert the "Date" column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    # Extract only the date (no time)
    df['Date'] = df['Date'].dt.date
    # Move the "Zip Code" column to the end
    df['Zip Code'] = df.pop('Zip Code')
    # Select only the mentioned columns
    df = df[['Representative name', 'Date', 'Place ID', 'Place', 'Street Address', 'City', 'State', 'Zip Code']]
    # Save the modified file
    df.to_csv(file, index=False)