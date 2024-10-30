import sqlite3

def view_students():
    """Retrieve and print all student records from the database."""
    conn = sqlite3.connect('DatabaseFile.db')  # Connect to the specified database file
    cursor = conn.cursor()

    # Query the records
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()

    # Print the records
    if rows:
        for row in rows:
            print(f"Student ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}")
    else:
        print("No records found.")

    # Close the connection
    conn.close()

# Example usage
if __name__ == "__main__":
    print("Current student records:")
    view_students()
