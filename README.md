# Task Manager DevOps

A production-style Flask REST API containerized with Docker and deployed on AWS EC2 — demonstrating a complete DevOps workflow from local development to live cloud deployment.

## Live Case Study

Full deployment walkthrough with architecture, screenshots, cost breakdown, and lessons learned:
https://d2uko7csallknv.cloudfront.net/task-manager-showcase.html

## Tech Stack

- Python (Flask)
- Docker
- AWS EC2 (Ubuntu 24.04)
- Linux (SSH, systemd, apt)
- Git & GitHub

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<id>/complete` | Mark a task as complete |
| DELETE | `/tasks/<id>` | Delete a task |

## Local Development

Install dependencies:

    pip install -r requirements.txt

Run the app:

    python app.py

App runs on `http://127.0.0.1:5000`

## Docker

Build the image:

    docker build -t task-manager .

Run the container:

    docker run -d -p 5000:5000 --name task-manager-app task-manager

Verify the container is running:

    docker ps

## Production Deployment

Deployed to AWS EC2 following these steps:

1. Launched an Ubuntu 24.04 t3.micro instance
2. Configured security group to allow SSH (port 22) and app traffic (port 5000)
3. Connected to the instance via SSH using a key pair
4. Installed Docker and Git on the server
5. Cloned this repository directly onto the instance
6. Built the Docker image and ran the container in detached mode
7. Verified the API from the public internet using the EC2 public IP

## Deployment Highlights

- Successfully deployed on AWS EC2 (Ubuntu 24.04, t3.micro)
- Docker container running with zero downtime during testing
- Public API endpoint accessible from anywhere in the world
- Total deployment cost: near-zero (free tier eligible)
- Verified with GET and POST requests from external clients

## DevOps Workflow

    Local Development
           |
           v
    Docker Containerization
           |
           v
    GitHub Repository
           |
           v
    AWS EC2 Deployment
           |
           v
    Live Production API

## Author

Ahmad Waheed — Cloud Engineer

- Portfolio: https://d2uko7csallknv.cloudfront.net
- LinkedIn: https://www.linkedin.com/in/ahmadwaheed2002/
- Case Study: https://d2uko7csallknv.cloudfront.net/task-manager-showcase.html
