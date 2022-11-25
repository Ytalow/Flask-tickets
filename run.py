from src import app, db
from src.models import Event, Ticket

if __name__ == "__main__":
    with app.app_context():
        # populate test event
        test_event = Event(name='Test', total_tickets=30)
        db.session.add(test_event)
        db.session.flush()

        # populate test event tickets
        for i in range(30):
            ticket = Ticket(event_id=test_event.id)
            db.session.add(ticket)
        db.session.commit()

        app.run(debug=True)
