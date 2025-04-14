#PYTHON PROGRAM to rename column headers to be clean and uniform(e.g., lowercase, no spaces) in dataset





import pandas as pd

# Load your dataset
file_path = r'C:\Users\niraj\Elevate_Labs\Dataset-1.csv'
df = pd.read_csv(file_path)

# Show original column names
print("Original column headers:")
print(df.columns.tolist())

# Clean column names
df.columns = (
    df.columns
    .str.strip()              # remove leading/trailing whitespace
    .str.lower()              # convert to lowercase
    .str.replace(' ', '_')    # replace spaces with underscores
    .str.replace(r'[^\w_]', '', regex=True)  # remove special characters
)

# Show cleaned column names
print("\nCleaned column headers:")
print(df.columns.tolist())

# Optional: Save the cleaned dataset
# df.to_csv('cleaned_columns_dataset.csv', index=False)
