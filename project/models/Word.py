from flask import flash
from project import db

class Word(db.Model):
    __tablename__  = "word"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "%d: %s" %(self.id, self.name)

    def add(self):
        db.session.add(self)
        db.session.commit()