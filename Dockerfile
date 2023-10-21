# Use the python:3.11 image as the base image
FROM python:3.11

# Set the initial working directory to /app
WORKDIR /app

# Copy all files to /app
COPY . ./

# Install dependencies
RUN pip3 install -r requirements.txt

# Change the working directory to /app/src
WORKDIR /app/src

# Expose port 8080
EXPOSE 8080

# Set the entry point for the container
ENTRYPOINT [ "reaction_roles.py" ]