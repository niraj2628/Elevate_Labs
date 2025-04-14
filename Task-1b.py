#identifying duplicates


import pandas as pd

# Load the dataset
file_path = r'C:\Users\niraj\Elevate_Labs\Dataset-1.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Check for duplicate rows
duplicates = df[df.duplicated()]

# Print summary
print(f"\nNumber of duplicate rows: {duplicates.shape[0]}")

# Show the duplicate rows (if any)
if not duplicates.empty:
    print("\nDuplicate rows:")
    print(duplicates)
else:
    print("No duplicate rows found.")