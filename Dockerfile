# FROM python:3.10.11

# # Set the working directory
# WORKDIR /app
  
# # Copy the requirements file
# COPY requirements.txt .
# RUN pip3 install --upgrade pip setuptools wheel
# # RUN pip3 install --upgrade pip
# RUN pip3 install --no-cache-dir -r requirements.txt
# # Install curl
# # RUN apk add --no-cache curl

# # Copy the application code
# COPY . .

# EXPOSE 3002

# # Set the command to run the application
# CMD [ "python","app.py"]

FROM python:3.10.11-slim

# Set the working directory
WORKDIR /app

# Update package lists and install required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    nano \
    git \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Upgrade pip, setuptools, and wheel
# RUN pip3 install --upgrade pip setuptools wheel

# Install packages from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 3002

# Set the command to run the application
CMD [ "python", "app.py" ]