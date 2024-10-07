# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for psycopg2 and locale
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    locales \
    && rm -rf /var/lib/apt/lists/*

# Generate the required locale (e.g., pt_BR.UTF-8)
RUN echo "pt_BR.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen pt_BR.UTF-8 && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=pt_BR.UTF-8

# Set the locale environment variables
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt
ENV LC_ALL pt_BR.UTF-8

# Copy the requirements.txt to the working directory
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the working directory
COPY . /app/

# Expose the port that the Django app runs on
EXPOSE 8000

# Run Django server on container startup
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
