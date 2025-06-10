
---

# 🏗️ Production-Grade Feedback System

A secure, scalable, and modular **FastAPI** application powered by **CouchDB**, built from the ground up with **production-ready architecture** — but fully runnable in local development via Docker.

---

## 🎯 Goal

To create a feedback management backend system that follows modern backend engineering standards:

* 🧱 Clean, modular architecture
* 🔐 JWT-based user authentication
* 🐳 Fully containerized using Docker & Docker Compose
* 🛡️ CouchDB with access control
* 🔄 Seamless integration between CouchDB and relational feedback store

---

## 📦 Tech Stack

* ⚡ **FastAPI** – Modern, high-performance Python web framework
* 🗃️ **CouchDB** – NoSQL document database for secure user storage
* 🐳 **Docker + Docker Compose** – Local container orchestration
* 🔑 **JWT Auth** – Secure token-based authentication
* 📁 **.env** – Environment-based configuration
* 🧪 **Modular Project Structure** – Clean, scalable backend design

---



## ✅ Current Features

| Feature                             | Description                                                  |
| ----------------------------------- | ------------------------------------------------------------ |
| 🧱 Modular Project Structure        | Clean, extensible architecture ideal for scaling             |
| 🔐 Secure CouchDB                   | Stores user credentials securely (hashed)                    |
| 🔑 JWT Authentication               | Users authenticate via secure tokens                         |
| 🧑‍💼 User Registration & Login      | Register and login endpoints backed by CouchDB               |
| ✍️ Submit Feedback                  | Authenticated users can submit feedback entries              |
| 📜 List Feedbacks                   | List feedback entries owned by the logged-in user            |
| ♻️ Update Feedback                  | Users can update their own feedback entries by ID            |
| ❌ Delete Feedback                  | Users can delete their own feedback entries by ID            |
| ⚙️ Configurable with .env           | Easily manage environment-specific variables and secrets     |
| 🐳 Dockerized Local Development     | Run the full stack (FastAPI + CouchDB + SQLite) via Docker   |
| 📤 CI/CD-Ready with GitHub Actions  | Supports automated Docker builds and Docker Hub deployment   |

---

