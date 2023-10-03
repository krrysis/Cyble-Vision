import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('file.csv')

# Extract the repository name from each URL and store it in a new column
df['repository_name'] = df['url'].str.extract(r'github\.com/([^/]+/[^/]+)')

# Drop duplicates based on the repository name column, keeping only the first instance
df.drop_duplicates(subset='repository_name', keep='first', inplace=True)

# Save the resulting dataframe to a new CSV file
df.to_csv('file2.csv', index=False)
