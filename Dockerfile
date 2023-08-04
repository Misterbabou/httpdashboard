FROM python:3.11-slim

# Copy the application code
COPY ./app /app

# Install requirements
RUN pip install -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Expose the port for the HTTP server
EXPOSE 8000

# Start the App and serve the HTML files using Python's built-in HTTP server on port 8000
CMD ["/bin/bash", "-c", "python3 render.py & python3 -m http.server 8000 --directory ./site"]