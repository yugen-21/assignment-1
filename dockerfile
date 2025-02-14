# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
