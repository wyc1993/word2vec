from project import db

class Heat(db.Model):
    __tablename__  = "heat"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    heat = db.Column(db.Float)
    month = db.Column(db.Integer)
    
    def __init__(self, name, heat, month):
        self.name = name
        self.heat = heat
        self.month = month

    def __repr__(self):
        return "%d: %s %d %f" %(self.id, self.name.encode("utf-8"),self.month, self.heat)

    def add(self):
        db.session.add(self)
        db.session.commit()

def get_heats(word):
    words = db.session.query(Heat).filter_by(name = word).all()

    result = [i for i in xrange(0, len(words)) ]
    for word in words:
        result[word.month] = word.heat

    print result
    return result

def get_top_hot_of_month(i, month):
    heat = db.session.query(Heat).filter_by(month = int(month)).order_by(1.0- Heat.heat)[0:i]

    print heat
    result = []
    for h in heat:
        result.append({'word': h.name, "heat": h.heat})
    return result
