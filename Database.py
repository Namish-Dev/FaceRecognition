import sqlite3

def create_database():
    # Connect to the SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect("Database.db")
    
    # Create the Students table if it doesn't exist
    conn.execute('''CREATE TABLE IF NOT EXISTS STUDENTS (
                        ID INTEGER PRIMARY KEY,
                        Name TEXT NOT NULL,
                        Age INTEGER NOT NULL
                    );''')
    
    print("Database and table created successfully")
    
    # Close the connection
    conn.close()

# Run this function once to create the database and table
create_database()
