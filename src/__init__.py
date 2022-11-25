from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///events.db"
app.config["SECRET_KEY"] = "abcde"

db = SQLAlchemy(app)

from src import routes