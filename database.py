import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

def connect_db():
    """Connects to the SQLite database.

    Returns:
        A database connection object or None if connection fails.
    """
    try:
        conn = sqlite3.connect('user.db')
        return conn
    except sqlite3.Error as e:
        logging.error("Failed to connect to database", exc_info=True)
        return None

def create_user_table(conn):
    """Creates the 'users' table in the database.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )''')
        conn.commit()
    except Exception as e:
        logging.error(f"Error creating table", exc_info=True)

    

def execute_query(query, params=()):
    """Executes a query on the database connection and returns the fetched data or None.

    Args:
        query (str): The SQL query to execute.
        params (tuple, optional): Parameters for the query. Defaults to ().

    Returns:
        A dictionary representing the fetched data (or None if connection fails or no row found).
    """    
    conn = connect_db()
    if conn:
        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
            return True
        except Exception as e:
            message = f"Error executing query: {e}"
            logging.error(message)
            return False

    else:
        logging.error("Failed to connect to database")
        return False
