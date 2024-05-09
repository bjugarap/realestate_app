from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Login(db.Model):
    __tablename__ = 'logins'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.now)
    is_active = db.Column(db.Boolean, nullable=False)

class Agent(db.Model):
    __tablename__ = 'agents'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('logins.id'))

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('logins.id'))
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'))

class Listing(db.Model):
    __tablename__ = 'listings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    house_size = db.Column(db.Integer, nullable=False)
    lot_size = db.Column(db.Integer, nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'))

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(255))
    description = db.Column(db.Text, nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.now)   
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    review_date = db.Column(db.DateTime, default=datetime.now)   
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))