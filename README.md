# Kubernetes Lab

## Overview

This repository contains the configuration files and documentation for a Kubernetes lab. The lab demonstrates the deployment and management of a FastAPI application and a Kubernetes Job.

## Contents

- `Dockerfile`: Docker configuration for building the FastAPI application container.
- `example-job.yml`: YAML file for a Kubernetes Job that prints "Hello World" at intervals.
- `fastapi-deployment.yml`: YAML file for deploying the FastAPI application.
- `fastapi-service.yml`: YAML file for exposing the FastAPI application as a service.

## Setup

### Prerequisites

- Kubernetes cluster (Minikube, Docker Desktop, or a cloud-based cluster)
- kubectl command-line tool
- Docker (for building images)
- GitHub CLI (for repository management)

### Steps

1. **Build Docker Image**

   Build the Docker image for the FastAPI application:

   ```bash
   docker build -t sattu2024/fastapi-fibonacci:latest .

# Apply Kubernetes Configuration
Apply the Kubernetes Deployment and Service configurations:
 - kubectl apply -f fastapi-deployment.yml
 - kubectl apply -f fastapi-service.yml

# Apply the Kubernetes Job configuration:
 - kubectl apply -f example-job.yml

# verify Deployments and Services
Check the status of pods and services:
- kubectl get pods
- kubectl get services

# View Logs
View logs of running pods:
- kubectl logs <pod-name>

# Cleaning Up
To delete the deployments, services, and jobs:
- kubectl delete -f fastapi-deployment.yml
- kubectl delete -f fastapi-service.yml
- kubectl delete -f example-job.yml

Additional Notes

	•	The Kubernetes Job is configured to print “Hello World” every 2 seconds for 30 seconds.
	•	Ensure that you have the correct permissions and access to your Kubernetes cluster and Docker registry.