# Use official PyTorch base image with CUDA support
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Set working directory
WORKDIR /app

# Copy Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all project files
COPY . .

# Set default command (can override this when running)
<<<<<<< HEAD
<<<<<<< HEAD
CMD ["python3", "-m", "web.app"]
=======
CMD ["python3", "web/app.py"]
>>>>>>> a0c4262 (added mbart config)
=======
CMD ["python3", "web/app.py"]
>>>>>>> a0c426296e806d1c03fae531f7b2029cfd039ec2
