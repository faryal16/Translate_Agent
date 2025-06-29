# Use an official lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Chainlit uses
EXPOSE 7860

# Run the Chainlit app
CMD ["chainlit", "run", "main.py", "-h", "0.0.0.0", "-p", "7860"]
