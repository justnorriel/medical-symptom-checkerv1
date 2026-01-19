FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY bayesian_model.py .
COPY templates/ ./templates/

# Expose port (Cloud Run uses $PORT)
EXPOSE 8080

# Use gunicorn for production
CMD ["gunicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
