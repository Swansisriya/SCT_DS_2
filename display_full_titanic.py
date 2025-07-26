import pandas as pd

# Load Titanic data
df = pd.read_csv('train.csv')

# Add a proper index column from 1 to 891
df.index = range(1, len(df) + 1)

# Display full DataFrame with all columns and rows
pd.set_option('display.max_rows', 891)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.colheader_justify', 'center')

print(df)
