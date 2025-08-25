# Use official Python image
FROM python:3.13-slim-bullseye

# Set work directory inside container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
COPY backend/.env .
RUN pip install -r requirements.txt

# Copy backend code
COPY backend/ ./backend
