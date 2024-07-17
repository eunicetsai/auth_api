from typing import Optional
from werkzeug.security import generate_password_hash

class User:
    def __init__(self, username, hashed_password):
        self.username = username
        self.hashed_password = hashed_password
        
