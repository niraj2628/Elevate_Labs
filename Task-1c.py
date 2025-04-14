#identifying duplicates and drop duplicates


import pandas as pd

# Load the dataset
file_path = r'C:\Users\niraj\Elevate_Labs\Dataset-1.csv'
df = pd.read_csv(file_path)

# Show the original shape
print(f"Original dataset shape: {df.shape}")

# Remove duplicate rows (keep the first occurrence by default)
df_no_duplicates = df.drop_duplicates()

# Show the new shape
print(f"Dataset shape after removing duplicates: {df_no_duplicates.shape}")

# Optional: Save the cleaned dataset to a new file
# df_no_duplicates.to_csv('cleaned_dataset.csv', index=False)

# Preview the cleaned data
print("\nCleaned dataset preview:")
print(df_no_duplicates.head())