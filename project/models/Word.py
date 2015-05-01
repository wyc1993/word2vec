from project import db

class Word(db.Model):
    __tablename__  = "word"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    heat = db.Column(db.Float)

    def __init__(self, name, heat):
        self.name = name
        self.heat = heat

    def __repr__(self):
        return "%d: %s %f" %(self.id, self.name.encode("utf-8"), self.heat)

    def add(self):
        db.session.add(self)
        db.session.commit()

def get_top_heat(i):
    words = db.session.query(Word).order_by(1-Word.heat)[0:i]
    result = []
    for word in words:
        result.append(word.name.encode("utf-8"))
    return result
