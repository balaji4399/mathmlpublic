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

FROM python:3.10-alpine

# Set the working directory within the container
WORKDIR /app
# RUN wget http://dl-cdn.alpinelinux.org/alpine/v3.15/main/x86_64/ca-certificates-20211220-r0.apk
# RUN apk add ca-certificates-20211220-r0.apk
# RUN rm ca-certificates-20211220-r0.apk
               
# Install necessary system dependencies using apk
RUN apk add --no-cache \
    build-base \
    jpeg-dev \
    zlib-dev \
    libjpeg \
    gettext \
    py3-lxml \
    py3-pillow \
    openldap-dev \
    python3-dev

# Install the pix2text library using pip
RUN pip install pix2text

# Copy the requirements file
COPY requirements.txt .

# Install any necessary packages or dependencies
# RUN apt-get update && apt-get install -y  \
#     && rm -rf /var/lib/apt/lists/*

# Install dependencies
# RUN pip install --no-cache --upgrade pip setuptools wheel
RUN pip install --no-cache --upgrade pip 
RUN pip install --no-cache setuptools 
RUN pip install --no-cache wheel 
RUN pip install --no-cache-dir -r requirements.txt
           
# Copy the application code
COPY app.py .
COPY utils.py .

# Set the entrypoint
CMD ["python3", "app.py"]