from sqlalchemy import text

from src import app, db
from src.models import Event

delete_query = text('TRUNCATE event CASCADE;')

if __name__ == "__main__":
    with app.app_context():
        db.execute(delete_query)
        test_event = Event(event_name='Test', total_tickets=30)
        db.session.add(test_event)
        db.session.commit()
        app.run(debug=True)
