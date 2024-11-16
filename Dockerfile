# Base Image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "routes:app", "--host", "0.0.0.0", "--port", "8000"]