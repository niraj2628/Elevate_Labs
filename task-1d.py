#PYTHON PROGRAM to standardize text values like gender, country names in dataset


import pandas as pd

# Load your dataset
file_path = r'C:\Users\niraj\Elevate_Labs\Dataset-1.csv'
df = pd.read_csv(file_path)

# Display original data (optional)
print("Original Gender (sample):")
print(df['Gender'].head())

# Standardize Gender column
df['Gender'] = df['Gender'].str.lower().str.strip()
df['Gender'] = df['Gender'].replace({
    'm': 'Male',
    'male': 'Male',
    'f': 'Female',
    'female': 'Female',
    'other': 'Other'
})


# Display standardized data (sample)
print("\nStandardized Gender values (sample):")
print(df['Gender'].head())

# Optional: Save cleaned data
# df.to_csv('standardized_dataset.csv', index=False)