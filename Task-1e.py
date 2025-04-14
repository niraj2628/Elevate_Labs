#PYTHON PROGRAM to convert date formats to a consistent type (e.g., dd-mm-yyyy) in dataset


import pandas as pd

# Load your dataset
file_path = r'C:\Users\niraj\Elevate_Labs\Dataset-1.csv'
df = pd.read_csv(file_path)

# Specify the name of your date column
date_column = 'ScheduledDay'  # Change this to match your column name

# Try to convert dates to datetime format (handles mixed formats)
df[date_column] = pd.to_datetime(df[date_column], errors='coerce', dayfirst=True)

# Format dates as dd-mm-yyyy
df[date_column] = df[date_column].dt.strftime('%d-%m-%Y')

# Display the standardized dates
print("Standardized date column:")
print(df[[date_column]].head())

# Optional: Save the cleaned dataset
df.to_csv('date_standardized_dataset.csv', index=False)