# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /luganodes_task2

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY Client.py .
COPY server.py .
COPY config.json .
# Specify the default command to run the application
CMD ["python", "Client.py"]
