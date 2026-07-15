# Task Manager DevOps

A serverless-style Flask REST API containerized with Docker and deployed on AWS EC2 — demonstrating a complete DevOps workflow from local development to production deployment.

## Live Deployment
Coming soon — deploying on AWS EC2 with an automated CI/CD pipeline.

## Tech Stack
- Python (Flask)
- Docker
- AWS EC2 (Ubuntu)
- GitHub Actions (CI/CD)
- Nginx (reverse proxy)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<id>/complete` | Mark task as complete |
| DELETE | `/tasks/<id>` | Delete a task |

## Local Development

Install dependencies and run locally:
