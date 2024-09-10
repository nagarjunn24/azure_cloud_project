from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Immigrant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    country_of_origin = db.Column(db.String(80), nullable=False)
    visa_type = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)
