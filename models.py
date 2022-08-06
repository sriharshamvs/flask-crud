from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class YellowpagesModel(db.Model):
    __tablename__ = "directory"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    company_name = db.Column(db.String())
    email = db.Column(db.String(), unique = True)
    number = db.Column(db.Integer(), unique = True)
    address = db.Column(db.String())
 
    def __init__(self, name, company_name, email, number, address):
        self.name = name
        self.company_name = company_name
        self.email = email
        self.number = number
        self.address = address
 
    def __repr__(self):
        return f"{self.name}:{self.email}:{self.number}:{self.company_name}"