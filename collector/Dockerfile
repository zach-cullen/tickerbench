# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /collector

# Copy the application files
COPY . /collector/

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]