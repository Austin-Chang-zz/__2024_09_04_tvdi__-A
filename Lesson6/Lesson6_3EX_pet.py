import sqlite3

# Step 1: Create a list named 'pets' with 5 fields and 10 data records
# Each record has fields: id, name, species, age, and owner
pets = [
    (1, 'Buddy', 'Dog', 3, 'Alice'),
    (2, 'Whiskers', 'Cat', 5, 'Bob'),
    (3, 'Charlie', 'Bird', 2, 'Cathy'),
    (4, 'Goldie', 'Fish', 1, 'David'),
    (5, 'Bella', 'Rabbit', 4, 'Eva'),
    (6, 'Max', 'Dog', 6, 'Frank'),
    (7, 'Luna', 'Cat', 3, 'Grace'),
    (8, 'Milo', 'Bird', 2, 'Hank'),
    (9, 'Nemo', 'Fish', 1, 'Ivy'),
    (10, 'Daisy', 'Rabbit', 3, 'Jack')
]

# Step 2: Connect to SQLite database (or create it) and create an empty table
connection = sqlite3.connect('pets_database.db')
cursor = connection.cursor()

# Drop the table if it already exists for re-run purposes
cursor.execute("DROP TABLE IF EXISTS pets")

# Create the 'pets' table with fields: id, name, species, age, owner
cursor.execute('''
    CREATE TABLE pets (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        species TEXT NOT NULL,
        age INTEGER,
        owner TEXT
    )
''')

# Step 3: Insert the 'pets' list data into the SQLite table
cursor.executemany("INSERT INTO pets VALUES (?, ?, ?, ?, ?)", pets)

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Data inserted successfully into the 'pets' table.")
