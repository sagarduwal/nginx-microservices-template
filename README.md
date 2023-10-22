# 🚀 Nginx Microservices Setup

This project is a microservices setup using Nginx, FastAPI Backend, and React Frontend service. The goal of this project is to demonstrate how to set up and run a microservices architecture using Docker and Nginx.

## 📚 Services

- **Nginx**: Acts as a reverse proxy to route requests to the appropriate backend service. It handles incoming requests and forwards them to the appropriate service, either the backend or the frontend.

- **Backend**: Serves as the FastAPI backend service. It is responsible for handling API requests and returning responses. The backend service is built with FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

- **Frontend**: Serves the React frontend of the application. It is responsible for displaying the user interface and interacting with the backend service. The frontend service is built with React, a popular JavaScript library for building user interfaces, and TypeScript, a statically typed superset of JavaScript that adds types to the language.

## 🛠️ Setup

1. Build the Docker images for the services:

```bash
docker-compose build
```

This command builds the Docker images for the services. It uses the Dockerfiles in each service's directory to build the images.

2. Run the Docker containers:

```bash
docker-compose up
```

This command starts the Docker containers for the services. It uses the docker-compose.yml file to determine how to run the containers.

3. Shutdown the docker containers:

```bash
docker-compose down
```

This command stops and removes the Docker containers for the services. It is useful for when you want to stop the services and clean up.

## 📖 API Documentation

The API documentation is available at `http://localhost/docs`. It is generated automatically by FastAPI and provides an interactive interface for exploring the API.

## 📄 License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

