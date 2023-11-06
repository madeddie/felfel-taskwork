# FELFEL Task Work (Edwin Hermans)

This project handles the running of a basic dockerized Python Flask app using Redis.

The project is to show understanding of Docker, Kubernetes and peripheral systems.

It consists of:

- a simple Python Flask app, provided by FELFEL with minor modifications by applicant
- requirements.txt and Dockerfile to build docker container
- Docker Compose compose.yml for local testing
- Kubernetess resource definitions for Deployment, Service and Ingress in ./k8s and shell script to deploy resources

## How to run locally

To run the application locally we'll need to install the dependencies and have a running redis data store available.
We'll make it simple by using Docker Compose to handle these steps for us.

Docker Compose will build the docker container image if it's not yet available and spin up a redis container and the application container.

```bash
docker compose up
```

(add `-d` after `up` if you want the process to detach and not connected to the foreground shell)

After the application starts up you can browse to http://localhost:8080 to see it in action. When you refresh the page the count should increase.
You can also browse to

- http://localhost:/8080/metrics see the Prometheus metrics endpoint of the app
- http://localhost:9090 Prometheus server to see the collected metric

To stop and remove the containers run:

```bash
docker compose down
```

When you bring up the compose setup once more you'll notice the count has reset to 0.

## How to run on Kubernetes

There are k8s resource definitions provided in the ./k8s directory for a Deployment and connected Service and Ingres types.
Deploy to Kubernetes using the `deploy_k8s_local.sh` script.

```bash
deploy_k8s_local.sh
```

If your local k8s instance has the NGINX ingress controller deployed, you should be able to browse to http://felfel-taskwork.127.0.0.1.nip.io 
which is a special DNS record that resolves to 127.0.0.1 and will connect to your local k8s instance.
Without the NGINX ingress controller available, please use a port-forward to connect to the application like so:

```bash
kubectl port-forward $(kubectl get pods -l "app=felfel-taskwork" -o jsonpath="{.items[0].metadata.name}") 8080
```

Then browse to http://localhost:8080, just like with the Docker Compose setup.

Prometheus metrics will be collected based on the k8s resource annotations so no further configuration steps need to be taken.

To clean up the resources run:

```bash
deploy_k8s_local.sh delete
```
