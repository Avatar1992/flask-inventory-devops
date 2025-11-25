🚀 Flask Inventory App – DevOps Project (Docker + Kubernetes + Argo CD)

A fully containerized Flask + MySQL Inventory Application deployed on a Kubernetes cluster with GitOps automation using Argo CD.

This project demonstrates real-world DevOps skills including CI/CD pipelines, infrastructure automation, containerization, and GitOps workflows.

📌 Architecture Overview

Flask App → Docker → Kubernetes → GitHub Actions CI → Argo CD CD → Ingress → Web Browser

🚀 Features
🔹 Backend

Flask application (CRUD API)

Python + Jinja template

🔹 Database

MySQL running inside Kubernetes

Initialized with inventorydb

🔹 DevOps / Cloud

Dockerized backend

GitHub Actions CI (build + push image)

Kubernetes deployment manifests

Argo CD GitOps automation

NGINX Ingress for routing

MySQL & Flask connected using environment variables

🛠️ Tech Stack
Component	Technology
Backend	Python Flask
Database	MySQL 8
Container	Docker
Orchestration	Kubernetes
CI	GitHub Actions
CD	Argo CD
Routing	NGINX Ingress
Cluster	Minikube/Cloud

📂 Project Structure
flask-inventory-devops/
├── app/
│   ├── app.py
│   ├── templates/
│   └── requirements.txt
├── manifests/
│   ├── deployment-backend.yaml
│   ├── deployment-mysql.yaml
│   └── ingress.yaml
├── docker-compose.yml
├── Dockerfile
└── README.md


CI/CD Pipeline
🔹 CI – GitHub Actions

Automatically builds & pushes Docker image:

Triggers on push to main

Builds Docker image

Pushes to Docker Hub

🔹 CD – Argo CD

Watches GitHub repo

Syncs Kubernetes manifests automatically

Zero-downtime updates

🐳 Run Locally with Docker
docker-compose up --build

☸️ Deploy on Kubernetes
kubectl apply -f manifests/

🌐 Access via Ingress
http://inventory.local

🎯 Outcome

This project demonstrates:

✔ Kubernetes expertise
✔ GitOps workflow (Argo CD)
✔ Docker containerization
✔ CI/CD automation
✔ MySQL–Flask integration
✔ Cloud-native architecture
