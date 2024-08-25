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