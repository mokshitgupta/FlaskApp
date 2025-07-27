# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Run the application
CMD ["python", "app.py"]
