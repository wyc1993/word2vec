from flask import flash
from project import db

class Word(db.Model):
    __tablename__  = "word"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    heat = db.Column(db.Float)
    url = db.Column(db.String(128))

    def __init__(self, name, heat, url):
        self.name = name
        self.heat = heat
        self.url = url

    def __repr__(self):
        return "%d: %s %f %s" %(self.id, self.name.encode("utf-8"), self.heat, self.url.encode("utf-8"))

    def add(self):
        db.session.add(self)
        db.session.commit()

def get_top_heat(i):
    words = db.session.query(Word).order_by(1-Word.heat)[0:i]
    result = []
    for word in words:
        result.append(word.name.encode("utf-8"))
    return result

def get_url(s):
    words = db.session.query(Word).filter_by(name=s).all()
    if len(words) > 0:
        return words[0].url
    else:
        return ""