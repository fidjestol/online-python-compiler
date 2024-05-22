# Online Python Compiler

## Python Docker IDE Installation Guide Using Docker

### Prerequisites
Before beginning the installation, ensure that you have Docker installed on your system. Docker will handle the creation and management of the container where both the Flask application and Python execution environment reside.

- Download and install Docker from [Docker's official site](https://www.docker.com/).

### Step 1: Download the Application
Clone the repository or download the source code:

```bash
git clone https://github.com/fidjestol/online-python-compiler
cd python-docker-ide
```
# If you are not using Git, download the ZIP file of the project and extract it to your preferred directory.

### Step 2: Build the Docker Image
Navigate to the directory containing the Docker file and build the Docker image. This image will include your Flask application, all its dependencies, and any necessary configurations.

```bash
docker build -t python-runner .
docker run -p 5000:5000 python-runner
```
### Step 3: Access the IDE
Open a web browser and navigate to http://localhost:5000/. You should see the Python Docker IDE interface, ready to execute Python code. Replace localhost with the IPv4 of your server if necessary.

Troubleshooting
Docker Issues: If the Docker container fails to start, verify that the Docker image was built correctly and that there are no errors in the Docker logs. Use docker logs [container_id] to view logs.
Port Availability: Ensure that port 5000 is not in use on your host. If it is, you can either free the port or modify the docker run command to map to a different port.
