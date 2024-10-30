import sqlite3

# Connect to the database (it will be created if it doesn't exist)
conn = sqlite3.connect('DatabaseFile.db')

# Create a cursor object
cursor = conn.cursor()

# Create the students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    studentID INTEGER PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL
)
''')

# Commit the changes
conn.commit()
conn.close()