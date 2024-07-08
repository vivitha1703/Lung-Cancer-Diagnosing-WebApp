# Use the official Python image as the base
FROM python:3.10.11

# Set the working directory inside the Docker image
WORKDIR /Lung_cancer

# Copy the necessary files to the working directory
COPY app.py .
COPY templates/ ./templates
COPY requirements.txt .
COPY model2.pkl .

# Install virtualenv and create a virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask application will listen on
EXPOSE 5000

# Set the command to run the application
CMD ["python", "app.py"]
