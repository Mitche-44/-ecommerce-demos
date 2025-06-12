from flask import Flask
from flask_migrate import Migrate

from models import db

app =Flask(__name__)

#configure a database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

#initialize flask migrate
migrate = Migrate(app=app,db=db)

#initialize the app to use sqlalchemy database
db.init_app(app=app)


#use flask cli
#inform cli about the flask app and port to use
#export FLASK_APP=app.py
#export FLASK_RUN_PORT=8000
#flask run --debug

#flask db init - to create a new migration
#flask db migrate - autogenerates new migration script in the migration folder
#flask db upgrade head - get the latest changes


# app operations
# fetch all data from the db and return as JSON


@app.get("/customers")
def get_all_customers():
    pass