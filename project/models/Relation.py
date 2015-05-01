from project import db

class Relation(db.Model):
    __tablename__  = "relation"
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(64))
    target = db.Column(db.String(64))
    weight = db.Column(db.Float)

    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
        
    def __repr__(self):
        return "%d:  %s->%s: %lf " % (self.id, self.source.encode("utf-8"), self.target.encode("utf-8"), self.weight)

    def add(self):
        db.session.add(self)
        db.session.commit()


def get_relations(source):
    relations = Relation.query.filter_by(source=source).all()
    result = {}
    for relation in relations:
        result[relation.target.encode("utf-8")] = relation.weight
    return {"rel": result}
    