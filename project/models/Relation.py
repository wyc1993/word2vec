from flask import flash
from project import db

class Relation(db.Model):
    __tablename__  = "relation"
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Integer)
    target = db.Column(db.Integer)
    weight = db.Column(db.Float)

    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
        
    def __repr__(self):
        return "%d:  %s->%s: %lf " % (self.id, self.source, self.target, self.weight)

    def add(self):
        db.session.add(self)
        db.session.commit()