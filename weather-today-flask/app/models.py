from . import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime as dt


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(256))
    temp = db.Column(db.String(8))
    description = db.Column(db.String(256))
    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return f'<City {self.city_name}, {self.temp}>'


    def __init__(self, city_name, temp, description):
        self.city_name = city_name
        self.temp = temp
        self.description = description
