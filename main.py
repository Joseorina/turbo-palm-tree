from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.integer(),primary_key=True)
	username = db.Column(db.String(255))
	password = db.Column(db.string(255))

	def __init__(self,username):
    		self.username = username

	def __repr__(self):
    	 return f"<User '{self.username}>"		
