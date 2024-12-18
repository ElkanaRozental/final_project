from sqlalchemy import desc, func
from app.models import Event


def get_top_5_fatal_events(session, limit):
    with session() as session:
        score = func.coalesce(Event.kill_number, 0) * 2 + func.coalesce(Event.wound_number, 0)
        top_events = (
            session.query(Event)
            .order_by(desc(score))
            .limit(limit)
            .all()
        )
        return list(top_events)


