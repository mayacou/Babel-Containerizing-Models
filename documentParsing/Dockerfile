# Use a lightweight Python base image
FROM python:3.10-slim

# Set environment variable to suppress interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libreoffice \
    tesseract-ocr \
    poppler-utils \
    ghostscript \
    fonts-dejavu-core \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full documentParsing codebase into the image
COPY . .

# Set the default command to run your main script
CMD ["python", "main.py"]
