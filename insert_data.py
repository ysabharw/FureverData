# insert_data.py
import sqlite3
import pandas as pd

# Load the CSV file
df = pd.read_csv('pet_adoption_data.csv')

# Connect to SQLite database
conn = sqlite3.connect('furever_data.db')

# Insert data into the 'pets' table
df.to_sql('pets', conn, if_exists='replace', index=False)

conn.commit()
conn.close()
