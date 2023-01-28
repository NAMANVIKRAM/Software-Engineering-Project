import sqlite3
import os

def create_table(cursor):
    try:
        # Create the table (if it doesn't already exist)
        cursor.execute('''CREATE TABLE IF NOT EXISTS people
                      (name TEXT, address TEXT, parents_name TEXT, photograph BLOB)''')
    except sqlite3.Error as e:
        print(f"Error occurred while creating table: {e}")
        
def insert_data(cursor, name, address, parents_name, photograph):
    try:
        # Open the photograph file and read its contents
        with open(photograph, 'rb') as img:
            img_data = img.read()

        # Insert the person's information into the table
        cursor.execute('''INSERT INTO people(name, address, parents_name, photograph)
                      VALUES (?,?,?,?)''', (name, address, parents_name, img_data))
    except sqlite3.Error as e:
        print(f"Error occurred while inserting data: {e}")
    except FileNotFoundError as e:
        print(f"Error occurred while opening file: {e}")

def main():
    try:
        # Connect to the database (or create it if it doesn't exist)
        conn = sqlite3.connect('people.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Creating table
        create_table(cursor)
        
        # Ask the user for the person's information
        name = input("Enter the person's name: ")
        address = input("Enter the person's address: ")
        parents_name = input("Enter the person's parents name: ")
        photograph = input("Enter the file path of the person's photograph: ")
        
        # Inserting data
        insert_data(cursor, name, address, parents_name, photograph)
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error occurred while connecting to the database: {e}")

if _name_ == "_main_":
    main()