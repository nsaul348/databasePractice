import sqlite3

def add_student(studentID, firstname, lastname):
    """Add a student record to the database."""
    conn = sqlite3.connect('DatabaseFile.db')  # Connect to the specified database file
    cursor = conn.cursor()

    # Insert a student record
    cursor.execute('''
    INSERT INTO students (studentID, firstname, lastname)
    VALUES (?, ?, ?)
    ''', (studentID, firstname, lastname))

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Example usage
if __name__ == "__main__":
    # Create the database and table if they don't exist
    conn = sqlite3.connect('DatabaseFile.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        studentID INTEGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

    # Add student records
    #add_student(1, 'John', 'Doe')
    #add_student(2, 'Jane', 'Smith')
    add_student(3, "Kim","Smith")

    print("Student records added successfully.")
