from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime



#create metadata instance
metadata = MetaData()

#create a flask SQLAlchemy instance

db= SQLAlchemy(metadata=metadata)

class Customer(db.model):
    __tablename__=