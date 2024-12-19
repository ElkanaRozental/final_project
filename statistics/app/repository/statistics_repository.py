from typing import Callable

from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from app.db.database import session_maker
from app.models import Event, Country


def calculate_fatal_event_score():
    return (func.coalesce(Event.kill_number, 0) * 2 + func.coalesce(Event.wound_number, 0)).label("score")

def get_most_fatal_events(session, limit):
    with session() as session:
        top_events = (
            session.query(Event)
            .add_columns(calculate_fatal_event_score())
            .order_by(desc(calculate_fatal_event_score()))
            .limit(limit)
            .all()
        )
        return top_events


def get_mean_fatal_event_for_country(session: Callable[[], Session], limit, country: str):
    with session() as session:
        try:
            mean_fatal = (
                session.query(Event, func.avg(calculate_fatal_event_score()).label("mean_score"))
                .join(Country, Event.country_id == Country.id)
                .filter(Country.country == country)
                .group_by(Event.id)
                .order_by(desc("mean_score"))
                .limit(limit)
                .all()
            )
            return mean_fatal
        except Exception as e:
            print(f"Error occurred while querying: {e}")
            return []



def get_all_events(session: Callable[[], Session]):
    with session() as session:
        events = (
            session.query(Event)
        ).all()
        return [event.__dict__ for event in events]



