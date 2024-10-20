# create_db.py
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('furever_data.db')
c = conn.cursor()

# Create table for pets
c.execute('''
CREATE TABLE IF NOT EXISTS pets (
    PetID TEXT PRIMARY KEY,
    PetType TEXT,
    Breed TEXT,
    AgeMonths INTEGER,
    Color TEXT,
    Size TEXT,
    WeightKg REAL,
    Vaccinated INTEGER,
    HealthCondition INTEGER,
    TimeInShelterDays INTEGER,
    AdoptionFee REAL,
    PreviousOwner INTEGER,
    AdoptionLikelihood INTEGER
)
''')

# Commit and close
conn.commit()
conn.close()
