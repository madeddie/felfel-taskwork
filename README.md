# FELFEL Task Work (Edwin Hermans)

This project handles the running of a basic dockerized Python Flask app using Redis.

The project is to show understanding of Docker, Kubernetes and peripheral systems.

It consists of:

- basic piece of Python code, provided by FELFEL with minor modifications by applicant
- requirements.txt and Dockerfile to build docker container

## How to run locally

The application can be run directly on a local CLI, provided the required dependencies are available.
Installing the dependencies is best done in a Python virtualenv, but left as exercise for the reader, find the dependencies in app/requirements.txt.

Since the application requires a Redis data store the initial usage will fail when we would view the webpage.
To run a local Redis instance we'll use docker:

```bash
docker run --rm -p 6379:6379 --name taskwork-redis -d redis
```

Run the application:

```bash
REDIS_USERNAME="" REDIS_PASSWORD="" REDIS_HOST=localhost REDIS_PORT=6379 REDIS_DB=0 python app/main.py
```

The application itself listens on any local IP on port 8080, so http://localhost:8080 should work in a local browser.
