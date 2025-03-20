# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
#COPY requirements.txt ./

#add fiels into image
ADD . ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's source code from your host to your image filesystem.
#COPY main.py .

# Run your_script.py when the container launches
CMD ["python", "./main.py"]