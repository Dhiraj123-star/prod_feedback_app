
---

# 🏗️ Production-Grade Feedback System

A secure, scalable, and modular **FastAPI** application powered by **CouchDB**, built from the ground up with **production-ready architecture** — but fully runnable in local development via Docker.

---

## 🎯 Goal

To create a feedback management backend system that follows modern engineering standards:

* 🧱 Clean, modular architecture
* 🔐 Secure with JWT authentication
* 🐳 Fully containerized using Docker
* 🛡️ CouchDB with access protection
* ⚙️ Ready for CI/CD, monitoring, and scaling

---

## 📦 Tech Stack

* ⚡ **FastAPI** – Lightweight, high-performance web framework
* 🗃️ **CouchDB** – Reliable NoSQL document database
* 🐳 **Docker + Docker Compose** – Containerized setup
* 🔑 **JWT** – Secure user authentication
* 📁 **.env** – Environment-based configuration
* 🧪 **Modular Folder Design** – Easy to maintain and scale

---

## 🧱 Project Structure Overview

Organized for clarity, separation of concerns, and ease of extension:

* `app/` – All FastAPI logic (routes, models, config, utils)
* `db/` – CouchDB integration
* `routes/` – Auth and feedback APIs
* `utils/` – JWT token utilities
* `Dockerfile` & `docker-compose.yml` – Local containerization
* `.env` – Secrets and config for local environment
* `requirements.txt` – Python dependencies

---

## ✅ Current Features

| Feature                          | Description                                         |
| -------------------------------- | --------------------------------------------------- |
| 🧱 Modular Project Structure     | Scalable and clean directory layout                 |
| 🔐 Secure CouchDB                | Uses credentials, no open dev DB                    |
| 🐳 Docker-Based Setup            | Mimics cloud infrastructure                         |
| 🔑 JWT Authentication Skeleton   | Token-based secure login and registration           |
| ✍️ Feedback Submission API       | Authenticated users can submit feedback entries     |
| 📜 Feedback Listing API          | List all feedbacks created by the logged-in user    |
| 💾 CouchDB-Backed Feedback Store | Feedbacks saved and retrieved directly from CouchDB |
| ⚙️ Configurable with .env        | Keeps secrets and URLs out of code                  |

---


## 📌 Why This Matters

Even though it's a personal/POC-level project:

* ✅ It mirrors **real-world backend engineering practices**
* 🧱 Designed for **extension and team collaboration**
* 🧰 Showcases your skill across **API design, security, DevOps, and database modeling**
* 🧠 Highlights ability to integrate NoSQL with Python-based RESTful services

---
 