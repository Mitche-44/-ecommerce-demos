from flask import Flask, make_response,request
from flask_migrate import Migrate

from models import db, Customer

# create a flask application instance / heart of the application
app = Flask(__name__)

# configure a database connection
# app.config

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# initialize flask migrate
migrate = Migrate(app=app, db=db)


# initalize the app to use sqlalchemy database
db.init_app(app=app)


# flask cli
# inform the cli about the flask app and the port to use
#export FLASK_APP=app.py
#export FLASK_RUN_PORT=8000
#flask run --debug

#flask db init - to create a new migration
#flask db migrate - autogenerates new migration script in the migration folder
#flask db upgrade head - get the latest changes


# app operations
# fetch all data from the db and return as JSON


# CRUD OPERATIONS ON CUSTOMERS
# CREATE A CUSTOMER
# RETRIEVE INFO ABOUT A CUSTOMER
# UPDATE A CUSTOMER
# DELETE A CUSTOMER


@app.get("/customers")
def get_all_customers():
    # query the database and retrieve all the customers
    # return the data in a format that other applications can understand
    # customers = db.session.query(Customer).all()
    customers = Customer.query.all()
    customer_list = [
        {
            "id": customer.id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
            "phone": customer.phone,
            "gender": customer.gender,
            "age": customer.age,
        }
        for customer in customers
    ]
    # the other way
    cust_list = []
    for customer in customers:
        cust = {
            "id": customer.id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
            "phone": customer.phone,
            "gender": customer.gender,
            "age": customer.age,
        }
        cust_list.append(cust)

    return make_response(cust_list, 200)


@app.get("/customers/<int:id>")
def get_one_customer(id):
    # query the databse and we get a customer by the customer id
    # if the customer exists -> return the details of that customer
    # else -> rreturn an appropriate response and the appropriate status code

    # .get(id)
    # technique 1
    # customer = Customer.query.get(id)

    # filter_by - technique 2
    customer = Customer.query.filter_by(id=id).first()

    if customer:
        customer_dict = {
            "id": customer.id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
            "phone": customer.phone,
            "gender": customer.gender,
            "age": customer.age,
        }
        return make_response(customer_dict, 200)
    else:
        return make_response({"status": 404, "message": "No customer found"}, 404)


# post

@app.post("/customers")
def add_customer():
    try:
        data = request.get_json()

        phone = data.get("phone")

        # Check for duplicate phone number
        existing = Customer.query.filter_by(phone=phone).first()
        if existing:
            return make_response({
                "code": 409,
                "message": "Phone number already exists. Please use a different one."
            }, 409)

        customer = Customer(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            phone=phone,
            gender=data.get("gender"),
            age=data.get("age"),
        )

        db.session.add(customer)
        db.session.commit()

        return make_response({
            "code": 201,
            "message": "Customer account created successfully"
        }, 201)

    except Exception as e:
        return make_response({
            "code": 400,
            "message": "An error occurred",
            "error": str(e)
        }, 400)

# perfom patch operations
# partial updates -> write the logic to account for this

@app.patch("/customers/<int:id>")
def update_customer(id):
    customer = Customer.query.filter_by(id=id).first()
    if not customer:
        return make_response({"message": "Customer not found"}, 404)

    data = request.get_json()

    # Update only provided fields
    if "first_name" in data:
        customer.first_name = data["first_name"]
    if "last_name" in data:
        customer.last_name = data["last_name"]
    if "email" in data:
        customer.email = data["email"]
    if "phone" in data:
        customer.phone = data["phone"]
    if "gender" in data:
        customer.gender = data["gender"]
    if "age" in data:
        customer.age = data["age"]

    db.session.commit()

    return make_response({
        "message": "Customer updated successfully",
        "customer": {
            "id": customer.id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
            "phone": customer.phone,
            "gender": customer.gender,
            "age": customer.age
        }
    }, 200)


# delete operations

@app.delete("/customers/<int:id>")
def delete_customer(id):
    customer = Customer.query.filter_by(id=id).first()
    if not customer:
        return make_response({"message": "Customer not found"}, 404)

    db.session.delete(customer)
    db.session.commit()

    return make_response({"message": f"Customer with ID {id} deleted successfully."}, 200)


# serialization to_dict()