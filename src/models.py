from datetime import datetime
from src import app, db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    total_tickets = db.Column(db.Integer)
    redeemed_tickets = db.Column(db.Integer, default=0)
    def __repr__(self):
        return self.name

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    redeemed = db.Column(db.Boolean, default=False, nullable=False)
    def __repr__(self):
        return self.id

with app.app_context():
    # clear database
    db.drop_all()
    # create tables
    db.create_all()