# Project DS3
Project for the Software Development III course
## Overview

This project is for managing medical appointments, implementing concepts such as microservices, API Gateway, Kubernetes, and design patterns like Circuit Breaker and Saga.

## Key Features and Concepts

### 1. Microservices Architecture
The application is divided into several independent microservices, each responsible for a specific domain:

- **Authentication**:  
  Handles user login, token-based authentication, and security mechanisms.

- **User Management**:  
  Manages user profiles, roles (patient or doctor), and registration.

- **Medical Appointments**:  
  Performs CRUD operations for scheduling, updating, and canceling appointments. Also manages doctors' availability and automated notifications.


### 2. API Gateway
Centralizes request routing, authentication, and load balancing, ensuring that all client interactions with the backend services are efficient and secure.

### 3. Kubernetes Orchestration
Leverages Kubernetes to deploy, scale, and manage microservices across clusters, ensuring high availability and fault tolerance.

### 4. Design Patterns
- **Circuit Breaker**:  
  Prevents cascading failures by gracefully handling service unavailability and implementing fallbacks.

- **Saga Pattern**:  
  Manages distributed transactions to ensure data consistency, especially during complex workflows like appointment scheduling and cancellation.

## Participants
- **Dylan Farkas Quiza - 2183118**
- **Ervin Caravali Ibarra - 1925648**
- **Herney Eduardo Quintero Trochez - 1528556**
- **Javier Andres Martinez Granados - 2179687**
- **Manuel Alejandro Medina Gonzalez - 1943270**
- **Wilson Andres Mosquera Zapata - 2182116**

## Technologies
- **Backend**: Node.js, Flask, PostgreSQL, Redis, SQLite3
- **Frontend**: 

## Setup
1. Clone the repository.
2. Have ready a Kubernetes cluster (e.g., Minikube, Docker Desktop, GKE).
3. Build and Upload Docker Images for each microservice (This step is optional, you can use the images already uploaded to Docker Hub):
   ```bash
   sh build_upload.sh
   ```
   1. **Note**: Make to change user for Docker Hub in the file `build_upload.sh`
   2. **Note**: You can delete the local images using this command, also make sure change the user in the file `build_delete.sh`:
      ```bash
      sh build_delete.sh
      ``` 
4. Deploy the Kubernetes resources:
   ```bash
   sh create_deploy.sh
   ```
5. Access the application through the API Gateway service (`http://localhost:5000` or `http://127.0.0.1:5000`).
6. To delete the Kubernetes resources:
   ```bash
   sh delete_deploy.sh
   ```
7. In directory `test_HTTP_Requests` you can find a file with some HTTP requests to test the application.
8. You can use Intellij IDEA Ultimate to test the requests or other application that supports files `.http`, either way you can use it as example.

