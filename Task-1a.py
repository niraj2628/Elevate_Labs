#Finding null values in dataset

import pandas as pd

# Load the dataset
file_path = r'C:\Users\niraj\Elevate_Labs\Dataset-1.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Check for null values in each column
print("\nNull values in each column:")
print(df.isnull().sum())

# Optionally, show rows with any null values
print("\nRows with any null values:")
print(df[df.isnull().any(axis=1)])