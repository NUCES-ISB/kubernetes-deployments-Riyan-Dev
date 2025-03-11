FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY app.py .

# Expose the port Flask will run on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
