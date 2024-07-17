## Auth API - Python Flask Application
This is a Python Flask application for a simple authentication API. It allows functionalities like user creation(registration) and user verification based on username and password.

### Features

* User creation(registration) with username and password (securely hashed)
* User verification by username with username and password

### Running & Testing Application

Currently, I am unable to build the Docker image due to limitations in Docker Desktop for my macOS version. I apologize for any inconvenience this may cause.

Therefore, this project includes a Dockerfile and a requirements.txt file at root folder for docker deployment purpose.

Key requirements:

* Python 3.x
* Flask
* sqlite3

Running the app:
    
```bash
    python app.py
```

This will start the Flask development server, typically accessible at http://127.0.0.1:5000/ by default in your web browser.

The application provides interactive API documentation using Swagger. You can access the documentation and test at the following URL:

http://127.0.0.1:5000/api/doc




