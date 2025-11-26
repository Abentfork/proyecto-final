# 🎰 Plexios Casino: Online Casino Demo

[![Project Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)](https://github.com/Abentfork/proyecto-final)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stripe Usage](https://img.shields.io/badge/Payments-Stripe%20(Test%20Mode)-informational?style=for-the-badge&logo=stripe&logoColor=white)](https://stripe.com)

## 💡 Overview

Plexios Casino is an **educational online casino demo** project designed to showcase a complete full-stack web architecture. This project does *not* involve real money; it simulates payments and transactions using **Stripe in Test Mode**.

It includes three main games, integrated using **Godot Web** technology:

| 🃏 Available Games |
| :---: |
| **Slot** 🎰 |
| **Roulette** 🎡 |
| **Blackjack** ♠️ |

---

## 🚀 Technologies / Stack

A robust **Full-Stack** architecture combining performance and modern development practices.

### ⚙️ Backend & API

| Component | Description | Details |
| :--- | :--- | :--- |
| **Language** | Python 3.11+ | [![Python](https://img.shields.io/badge/Python-3.11+-3670A0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) |
| **Framework** | FastAPI | [![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/) |
| **Database** | SQLite / PostgreSQL | [![Database](https://img.shields.io/badge/DB-PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/) |
| **ASGI Server** | Uvicorn / Gunicorn | High performance for production environments. |
| **Payments** | Stripe API | **Test Mode** only. |

> **Key Dependencies:** `fastapi`, `uvicorn`, `sqlalchemy` / `tortoise-orm`, `python-dotenv`, `stripe`.

### 💻 Frontend & UI

| Component | Description | Details |
| :--- | :--- | :--- |
| **Library** | React | [![React](https://img.shields.io/badge/React-UI-61DAFB?style=for-the-badge&logo=react&logoColor=white)](https://react.dev/) |
| **Styling** | TailwindCSS | [![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Styles-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/) |
| **Games** | Godot Engine 4 | [![Godot](https://img.shields.io/badge/Godot-Games-478CBF?style=for-the-badge&logo=godot-engine&logoColor=white)](https://godotengine.org/) |

### 🌐 Hosting / Deployment

| Component | Details |
| :--- | :--- |
| **Provider** | Oracle Cloud |
| **Backend Service** | Gunicorn + Uvicorn |
| **Reverse Proxy** | Nginx |
| **Security (HTTPS)** | Let’s Encrypt |

---

## 💾 Database Design

The database design uses **SQLite** for local development and **PostgreSQL** for the server environment. The schema is centered on auditability and managing the virtual casino economy.

### Entity: `Users` 👤

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | SERIAL / **PK** | Unique user ID |
| `username` | VARCHAR(50) | Unique username |
| `email` | VARCHAR(100) | Unique email |
| `password_hash` | VARCHAR(255) | Hashed password |
| `credits` | NUMERIC(10,2) | **Current virtual balance** |
| `created_at` | TIMESTAMP | Registration date |
| `last_login` | TIMESTAMP | Last login timestamp |

### Entity: `Games` 🕹️

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | SERIAL / **PK** | Unique game ID |
| `name` | VARCHAR(50) | Game name |
| `type` | VARCHAR(20) | `slot` / `roulette` / `blackjack` |
| `created_at` | TIMESTAMP | Creation date |

### Entity: `Bets` 💰

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | SERIAL / **PK** | Unique bet ID |
| `user_id` | INT / **FK** | User placing the bet |
| `game_id` | INT / **FK** | Game played |
| `bet_amount` | NUMERIC(10,2) | Amount bet |
| `win_amount` | NUMERIC(10,2) | Amount won (0 if lost) |
| `outcome` | VARCHAR(20) | Result: `win` / `loss` / `draw` |
| `created_at` | TIMESTAMP | Timestamp of the bet |

### Entity: `Payments` 💳

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | SERIAL / **PK** | Unique payment ID |
| `user_id` | INT / **FK** | User making the payment |
| `amount` | NUMERIC(10,2) | Credits added |
| `stripe_payment_id` | VARCHAR(100) | Stripe test payment ID |
| `status` | VARCHAR(20) | Status: `succeeded` / `failed` |
| `created_at` | TIMESTAMP | Timestamp of payment |

> 📌 **Note:** An optional `Transactions log` table can be added to record **any change in user credits**, simulating a professional casino audit trail.

---

## ✨ Core Features

* ✅ **Authentication System:** User registration and login.
* 💰 **Virtual Economy:** Fully functioning virtual credits system.
* 🎮 **Integrated Games:** Play **Slot**, **Roulette**, and **Blackjack**.
* 💳 **Payment Simulation:** Stripe test payment integration for credit top-ups.
* 📊 **Detailed Tracking:** Individual tracking of every bet and game result.
* 🔧 **Scalability:** Designed to be easily expandable for future games.

---

## 🛠️ Setup / Installation

1. Clone the repository:

```bash
git clone [https://github.com/Abentfork/proyecto-final.git](https://github.com/Abentfork/proyecto-final.git)
cd proyecto-final
