import sqlite3

def create_tables(cursor):
    #Creating all the required tables with proper relationships
    
    try:
        # Publishers table with each publisher having a unique name
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)
        
        # Magazines table with each magazine belonging to 1 publisher (1-to-many)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
        )
        """)
        
        # Subscribers table with naming and addressing must be non-null
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            UNIQUE(name, address)
        )
        """)
        
        # Subscriptions table with joining table for many-to-many relationship
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER,
            magazine_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
        )
        """)
        
        print("Tables created successfully.")
        
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
        

def test_tables_exist(cursor): #Test function to verify tables creations
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Tables in database:")
        for table in tables:
            print(f"  - {table[0]}")
    except sqlite3.Error as e:
        print(f"Error checking tables: {e}")
        
        
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        print(f"Added publisher: {name}")
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists in database.")
        

def add_magazine(cursor, name, publisher_name):
    try:
        #getting the publisher_id (foreign key lookup)
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        result = cursor.fetchone()
        
        if result is None:
            print(f"Publisher '{publisher_name}' not found. Cannot add magazine.")
            return
            
        publisher_id = result[0]  #Get the ID from first column
        
        #inserting the magazine
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", 
                      (name, publisher_id))
        print(f"Added magazine: {name} (Publisher: {publisher_name})")
        
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already exists in database.")
    except sqlite3.Error as e:
        print(f"Error adding magazine: {e}")
        

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", 
                      (name, address))
        print(f"Added subscriber: {name} at {address}")
    except sqlite3.IntegrityError:
        print(f"Subscriber '{name}' at '{address}' already exists in database.")
        
        
def add_subscription(cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):
    try:
        #Get subscription ID
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", 
                      (subscriber_name, subscriber_address))
        subscriber_result = cursor.fetchone()
        
        if subscriber_result is None:
            print(f"Subscriber '{subscriber_name}' at '{subscriber_address}' not found.")
            return
        
        # Get magazine_id
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        magazine_result = cursor.fetchone()
        
        if magazine_result is None:
            print(f"Magazine '{magazine_name}' not found.")
            return
        
        subscriber_id = subscriber_result[0]
        magazine_id = magazine_result[0]
        
        # Check if subscription already exists
        cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", 
                      (subscriber_id, magazine_id))
        if cursor.fetchone():
            print(f"Subscription for '{subscriber_name}' to '{magazine_name}' already exists.")
            return
        
        # Insert subscription
        cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", 
                      (subscriber_id, magazine_id, expiration_date))
        print(f"Added subscription: {subscriber_name} -> {magazine_name} (expires: {expiration_date})")
        
    except sqlite3.Error as e:
        print(f"Error adding subscription: {e}")
        
def execute_queries(cursor):
    print("\nTask4: SQL queries")
    
    try:
        # Query 1: All the subscribers
        print("\n1. All subscribers:")
        cursor.execute("SELECT * FROM subscribers")
        results = cursor.fetchall()
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Address: {row[2]}")
        
        # Query 2: All of the magazines sorted by name
        print("\n2. All magazines sorted by name:")
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        results = cursor.fetchall()
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Publisher ID: {row[2]}")
        
        # Query 3: Magazines for a specific publisher (using JOIN)
        print("\n3. Magazines published by 'Tech Publications':")
        cursor.execute("""
        SELECT m.magazine_id, m.name as magazine_name, p.name as publisher_name
        FROM magazines m 
        JOIN publishers p ON m.publisher_id = p.publisher_id 
        WHERE p.name = ?
        """, ("Tech Publications",))
        results = cursor.fetchall()
        for row in results:
            print(f"Magazine ID: {row[0]}, Magazine: {row[1]}, Publisher: {row[2]}")
            
    except sqlite3.Error as e:
        print(f"Error executing queries: {e}")


def main():
    #Main functions to run all tasks
    try:
        # Task 1: Connecting to database
        with sqlite3.connect("../db/magazines.db") as conn:
            conn.execute("PRAGMA foreign_keys = 1")  # Enableing foreign key constraints
            cursor = conn.cursor()
            
            print("Database created and connected successfully.")
            
            # Task 2: Creating tables
            create_tables(cursor)
            test_tables_exist(cursor)
            
            #Task 3: populating tables with sample data (I guess custom database)
            print("\nPopulating Tables")
            
            # Adding publishers first (no dependencies)
            add_publisher(cursor, "Tech Publications")
            add_publisher(cursor, "Lifestyle Media")
            add_publisher(cursor, "Science Weekly")
            
            # Adding magazines (depends on publishers)
            add_magazine(cursor, "Computer World", "Tech Publications")
            add_magazine(cursor, "Mobile Tech", "Tech Publications")
            add_magazine(cursor, "Home & Garden", "Lifestyle Media")
            add_magazine(cursor, "Fashion Today", "Lifestyle Media")
            add_magazine(cursor, "Nature Science", "Science Weekly")
            add_magazine(cursor, "Physics Quarterly", "Science Weekly")
            
            # Adding subscribers (no dependencies)
            add_subscriber(cursor, "John Smith", "123 Main St, Anytown USA")
            add_subscriber(cursor, "Jane Doe", "456 Oak Ave, Somewhere CA")
            add_subscriber(cursor, "Bob Johnson", "789 Pine Rd, Elsewhere TX")
            add_subscriber(cursor, "Alice Brown", "321 Elm St, Nowhere FL")
            
            # Adding subscriptions (dependencies: both subscribers and magazines)
            add_subscription(cursor, "John Smith", "123 Main St, Anytown USA", 
                           "Computer World", "2025-12-31")
            add_subscription(cursor, "John Smith", "123 Main St, Anytown USA", 
                           "Nature Science", "2025-06-30")
            add_subscription(cursor, "Jane Doe", "456 Oak Ave, Somewhere CA", 
                           "Fashion Today", "2025-09-15")
            add_subscription(cursor, "Jane Doe", "456 Oak Ave, Somewhere CA", 
                           "Home & Garden", "2025-11-30")
            add_subscription(cursor, "Bob Johnson", "789 Pine Rd, Elsewhere TX", 
                           "Physics Quarterly", "2026-03-31")
            add_subscription(cursor, "Alice Brown", "321 Elm St, Nowhere FL", 
                           "Mobile Tech", "2025-08-15")
            
            conn.commit() # Commiting all the changes
            execute_queries(cursor)# Executing the task 4 queries
            
            print("\nAll data inserted and committed successfully!")
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()