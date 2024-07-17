import logging
import re
from typing import Optional
from models.user import User
from repositories.user import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def verify_user(self, username, password):
        

        user = self.user_repository.get_by_username(username)
        # Check password if username exists
        stored_hashed_password = user[1]
        if not check_password_hash(stored_hashed_password, password):
            msg = "Invalid password"
            logging.error(msg)
            return None, msg


        # user, msg = self.user_repository.verify_user(username, password)
        if not user:
            msg = "Invalid user"
            logging.error(msg)
            return None
        
        logging.info("User verifiction success")        
        return user, None

    def create_user(self, username, password):        
        """
        This function creates a new user in the database if the username doesn't exist.

        Args:
            username: The username for the new user (must be unique).
            password: The password for the new user (securely hashed before storing).

        Returns:
            A tuple containing two elements:
                - success (bool): True if user created successfully, False otherwise.
                - message (str, optional): Informative message about the outcome (None if successful).
        """

        # Username validation
        if not self.validate_username(username):
            msg = "Username must be between 3 and 32 characters."
            logging.error(msg)
            return False, msg

        # Password validation
        if not self.validate_password(password):
            msg = "Password must be between 8 and 32 characters, containing at least 1 uppercase letter, 1 lowercase letter, and 1 number."
            logging.error(msg)
            return False, msg

        # Check if user exists
        user = self.user_repository.get_by_username(username)
        if user:
            msg = "Username already exists."
            logging.error(msg)
            return False, msg

        # Create user with hashed password
        hashed_password = generate_password_hash(password)
        success = self.user_repository.create_user(username, hashed_password)
        if not success:
            msg = "Failed to create user"
            logging.error(msg)
            return False, msg
        
        logging.info("User creation success")
        return True, ""

    # Define validation functions
    def validate_username(self, username):
        return 3 <= len(username) <= 32

    def validate_password(self, password):
        pattern = r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])\w{8,32}"  # Regex for password validation
        return bool(re.match(pattern, password))

