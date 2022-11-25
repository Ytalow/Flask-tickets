from src import app, db
from src.models import Event, Ticket
from flask import render_template, request
from sqlalchemy import update

@app.route("/", methods=["GET"])
def homepage():
    events = Event.query.all()
    return render_template("index.html", events=events)

@app.route("/event/<event_id>", methods=["GET"])
def event_visualizer(event_id):
    tickets = Ticket.query.filter_by(event_id=event_id).all()
    event = Event.query.where(Event.id == event_id).first()
    return render_template("event.html", event=event, tickets=tickets)

@app.route("/event", methods=["POST"])
def add_event(event_name, event_date, total_tickets):
    event = Event(event_name=event_name, event_date=event_date, total_tickets=total_tickets)
    db.session.add(event)
    db.session.flush()
    ticket = Ticket(event_id=event.id)
    for i in range(total_tickets):
        db.session.add(ticket)
    db.session.commit()
    tickets = Ticket.query.filter_by(event_id=event.id).all()
    return render_template("event.html", event=event, tickets=tickets)

@app.route("/redeem/<event_id>/<ticket_id>", methods=["GET"])
def redeem_ticket(event_id, ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    event = Event.query.get(event_id)
    if ticket.redeemed == True:
        return "Ticket already redeemed!", 410
    ticket.redeemed = True
    event.redeemed_tickets += 1
    db.session.commit()
    return render_template("redeemed_ticket.html", ticket=ticket, event_name=event.name)