# FELFEL Task Work (Edwin Hermans)

This project handles the running of a basic dockerized Python Flask app using Redis.

The project is to show understanding of Docker, Kubernetes and peripheral systems.

It consists of:

- basic piece of Python code, provided by FELFEL with minor modifications by applicant
- requirements.txt and Dockerfile to build docker container
- Docker Compose compose.yml for local testing

## How to run locally

To run the application locally we'll need to install the dependencies and have a running redis data store available.
We'll make it simple by using Docker Compose to handle these steps for us.

Docker Compose will build the docker container image if it's not yet available and spin up a redis container and the application container.

```bash
docker compose up
```

(add `-d` after `up` if you want the process to detach and not connected to the foreground shell)

After the application starts up you can browse to http://localhost:8080 to see it in action. When you refresh the page the count should increase.

To stop and remove the containers run:

```bash
docker compose down
```

When you bring the compose setup once more you'll notice the count has reset to 0.

## How to run on Kubernetes

## Hot to use the Helm chart
