# Base Image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY /backend .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "routes:app", "--host", "0.0.0.0", "--port", "8000"]