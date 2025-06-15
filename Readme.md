
---

# Flask Customer Management API

This is a simple **Customer Management REST API** built with **Flask**, **Flask-SQLAlchemy**, and **Flask-Migrate**. The application allows CRUD operations on customers and stores customer data in a local SQLite database.

---

##  Features

* Create, read, update, and delete customer records
* Built using Flask with SQLAlchemy ORM
* Auto-migrations using Flask-Migrate
* Duplicate phone/email protection
* Structured database seeding script

---

##  Project Structure

```bash
├── app.py              # Main Flask application
├── models.py           # SQLAlchemy models
├── seed.py             # Script to populate database with seed data
├── migrations/         # Auto-generated migration files
├── store.db            # SQLite database (auto-created)
├── README.md           # Project documentation
```

---

##  Technologies Used

* Python 
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* SQLite
* SQLAlchemy Serializer

---

## Setup Instructions

### 1.  Install Dependencies

Create a virtual environment (recommended), then:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate sqlalchemy_serializer
```

### 2. Initialize the Database

```bash
export FLASK_APP=app.py
export FLASK_RUN_PORT=8000

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 3. 🌱 Seed the Database

```bash
python seed.py
```

### 4. ▶ Run the Server

```bash
flask run --debug
```

Server will run on `http://localhost:8000`

---

##  API Endpoints (POSTMAN)

| Method | Endpoint          | Description               |
| ------ | ----------------- | ------------------------- |
| GET    | `/customers`      | Get all customers         |
| GET    | `/customers/<id>` | Get a specific customer   |
| POST   | `/customers`      | Add a new customer        |
| PATCH  | `/customers/<id>` | Update part of a customer |
| DELETE | `/customers/<id>` | Delete a customer         |

### Sample POST Body

```json
{
  "first_name": "Sammy",
  "last_name": "Chirchir",
  "email": "sammy@gmail.com",
  "phone": "0712345611",
  "gender": "male",
  "age": 27
}
```

---

## 🧠 Model Overview

### Customer

```python
class Customer(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    first_name  = db.Column(db.String, nullable=False)
    last_name   = db.Column(db.String, nullable=False)
    email       = db.Column(db.String(100), unique=True, nullable=False)
    phone       = db.Column(db.String, unique=True, nullable=False)
    gender      = db.Column(db.String, nullable=False)
    age         = db.Column(db.Integer)
    created_at  = db.Column(db.DateTime, default=datetime.now)
```

---

##  Notes

* `PATCH` only updates fields that are provided in the request.
* Unique constraints prevent adding customers with duplicate phone or email.
* All responses are returned as JSON using `make_response`.

---

## 📬 Contact

Built with 💻 by **Mitchelle Ngetich**

Feel free to reach out with questions or improvements!

---


