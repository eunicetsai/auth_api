
import logging

from database import connect_db, execute_query
from werkzeug.security import check_password_hash

class UserRepository:
    logging.basicConfig(level=logging.DEBUG)
    
    def __init__(self, conn):
        self.conn = conn

    def verify_user(self, username, password):
        conn = self.conn
        query = 'SELECT * FROM users WHERE username = ?'    
        
        try:
            user = execute_query(query, (username,))

            if not user:
                msg = "Username not found"
                logging.error(msg)
                return None, msg

        # Check password if username exists
            stored_hashed_password = user[1]
            if not check_password_hash(stored_hashed_password, password):
                msg = "Invalid password"
                logging.error(msg)
                return None, msg
        
        except Exception as e:
            msg = "Error verifying user"
            logging.error(msg)
            return None, msg

        # Username and password match, return user data
        return user, None

    def create_user(self, username, password):
        """
        This function creates a new user in the database.

        Args:
            username: The username for the new user (must be unique).
            password: The password for the new user (securely hashed before storing).

        Returns:
            A dictionary containing the newly created user information if successful,
            None otherwise.
        """
        query = 'INSERT INTO users (username, password) VALUES (?, ?)'
        
        try:
            success = execute_query(query, (username, password))
            if not success:
                msg = "Error creating user"
                logging.error(msg)
        
        except Exception as e:
            msg = f"Error creating user: {e}"
            logging.error(msg)
            return None, msg
    
        return success


    def get_by_username(self, username):
        """
        This function retrieves a user from the database based on their username.

        Args:
            username: The username of the user to retrieve.

        Returns:
            A dictionary containing user information if found, None otherwise.
        """
        query = 'SELECT * FROM users WHERE username = ?'

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(query, (username,))
            user = cursor.fetchone() 
            return user if user else None 
        except Exception as e:
            msg = f"Error getting user by username: {e}"
            logging.error(msg)
            return None