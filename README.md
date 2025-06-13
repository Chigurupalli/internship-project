🚀 Internship Project - CI/CD with GitHub Actions, Docker, and Kubernetes

This project demonstrates a complete CI/CD pipeline for deploying a **Python Flask** web application using **GitHub Actions**, **Docker**, and **Kubernetes (Minikube)**.

---

## 📌 Tech Stack

- 🐍 Python (Flask)
- 🐳 Docker
- ☸️ Kubernetes (Minikube)
- 🤖 GitHub Actions (CI/CD)
- 🛠️ kubectl

---

## 📁 Folder Structure

internship-project/ ├── app/                     # Flask app source │   └── app.py ├── Dockerfile               # Docker build file ├── k8s/                     # Kubernetes manifests │   ├── deployment.yaml │   └── service.yaml ├── .github/ │   └── workflows/ │       └── ci-cd.yaml       # GitHub Actions workflow ├── requirements.txt         # Flask dependencies └── README.md

---

## ⚙️ How It Works

### 🔄 GitHub Actions CI/CD Flow

1. Triggered on push to `main` branch
2. Installs Docker & kubectl
3. Decodes `kubeconfig` from secret
4. Deploys Flask app to Kubernetes

---

## 🐳 Docker Commands

### Build Image
```bash
docker build -t flask-app .

Run Container Locally

docker run -p 5000:5000 flask-app


---

☸️ Kubernetes (Minikube)

Start Minikube

minikube start

Deploy App

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

Access App

minikube service flask-app-service


---

🔐 GitHub Secrets Required

Before pushing the workflow, add the following secret in your GitHub repository:

KUBECONFIG_B64 = base64 of your kubeconfig file
To generate:

cat ~/.kube/config | base64 -w 0



---

📄 GitHub Actions Workflow (.github/workflows/ci-cd.yaml)

name: CI/CD Pipeline

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout source
      uses: actions/checkout@v4

    - name: Set up kubectl
      run: |
        curl -LO "https://dl.k8s.io/release/$(curl -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
        chmod +x kubectl
        sudo mv kubectl /usr/local/bin/

    - name: Decode kubeconfig
      run: |
        echo "${{ secrets.KUBECONFIG_B64 }}" | base64 -d > kubeconfig
        export KUBECONFIG=$PWD/kubeconfig
        kubectl get nodes

    - name: Deploy to Kubernetes
      run: |
        export KUBECONFIG=$PWD/kubeconfig
        kubectl apply -f k8s/


---

🙌 Author

Hruthik Sai (@Chigurupalli)
Final Year CSE | DevOps & Cloud Enthusiast 🚀
