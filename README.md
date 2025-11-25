# Plexios Casino: Online Casino Demo

## Overview
Plexios Casino is an educational online casino demo featuring three games:
- Slot
- Roulette
- Blackjack

The project uses **Stripe in test mode** for simulated payments (no real money is involved).  
It demonstrates a full web-based architecture with backend, frontend, integrated games, and a database.

---

## Technologies / Stack

**Backend**
- Python 3.11+
- FastAPI
- ASGI server: Uvicorn / Gunicorn
- Database: SQLite (local development) / PostgreSQL (server)
- JWT authentication for user login
- Stripe API (test mode)
- Dependencies: `fastapi`, `uvicorn`, `sqlalchemy` / `tortoise-orm`, `python-dotenv`, `stripe`

**Frontend**
- React
- TailwindCSS
- Integration with Godot Web games via `<iframe>` or `<canvas>`
- API calls via `fetch` or `axios`

**Games**
- Godot 4 exported to HTML5 / WebAssembly
- Each game in its own folder: `slot/`, `roulette/`, `blackjack/`
- Communicates with backend to update credits and register bets

**Hosting / Deployment**
- Oracle Cloud
- Backend served with Gunicorn + Uvicorn behind Nginx
- HTTPS via Let’s Encrypt

---

## Database Design

### Users
| Field | Type | Description |
|-------|------|------------|
| id | SERIAL / PK | Unique user ID |
| username | VARCHAR(50) | Unique username |
| email | VARCHAR(100) | Unique email |
| password_hash | VARCHAR(255) | Hashed password |
| credits | NUMERIC(10,2) | Virtual balance |
| created_at | TIMESTAMP | Registration date |
| last_login | TIMESTAMP | Last login |

### Games
| Field | Type | Description |
|-------|------|------------|
| id | SERIAL / PK | Unique game ID |
| name | VARCHAR(50) | Game name |
| type | VARCHAR(20) | slot, roulette, blackjack |
| created_at | TIMESTAMP | Creation date |

### Bets
| Field | Type | Description |
|-------|------|------------|
| id | SERIAL / PK | Unique bet ID |
| user_id | INT / FK → Users(id) | User placing the bet |
| game_id | INT / FK → Games(id) | Game played |
| bet_amount | NUMERIC(10,2) | Amount bet |
| win_amount | NUMERIC(10,2) | Amount won (0 if lost) |
| outcome | VARCHAR(20) | win / loss / draw |
| created_at | TIMESTAMP | Timestamp of the bet |

### Payments
| Field | Type | Description |
|-------|------|------------|
| id | SERIAL / PK | Unique payment ID |
| user_id | INT / FK → Users(id) | User making the payment |
| amount | NUMERIC(10,2) | Credits added |
| stripe_payment_id | VARCHAR(100) | Stripe test payment ID |
| status | VARCHAR(20) | succeeded / failed |
| created_at | TIMESTAMP | Timestamp of payment |

> Optional: Transactions log table can be added to record **any change in credits**, simulating a professional casino audit trail.

---

## Features
- User registration & login  
- Virtual credits system  
- Play Slot, Roulette, and Blackjack  
- Stripe test payment integration  
- Track every bet and result individually  
- Expandable to add new games in the future  

---

## Setup / Installation

1. Clone the repository:
```bash
git clone https://github.com/Abentfork/proyecto-final.git
