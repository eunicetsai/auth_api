# Use a base image with Python
FROM python:3.9

# Create a working directory within the container
WORKDIR /app

# Copy requirements.txt (if using dependencies)
COPY requirements.txt .

# Install dependencies (if any)
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Expose the port where your Flask application runs (adjust if needed)
EXPOSE 5000

# Set the command to run your application
CMD ["python", "app.py"]