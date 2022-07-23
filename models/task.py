from utils.db import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(100))
    description = db.Column(db.String(100))
    priority = db.Column(db.String(100))

    def __init__(self, tittle, description, priority):
        self.tittle = tittle
        self.description = description
        self.priority = priority
