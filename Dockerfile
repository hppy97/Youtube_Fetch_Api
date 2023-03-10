FROM python:3.8

# create root directory for project in the container
RUN mkdir /youtube_browse_api

# Set the working directory to /youtube_fetch_api
WORKDIR /youtube_browse_api

# Copy the current directory contents into the container at /youtube_fetch_api
ADD . /youtube_browse_api/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt