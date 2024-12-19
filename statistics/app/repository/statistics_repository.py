from typing import Callable
from pydantic import BaseModel
from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from app.db.database import session_maker
from app.models import Event, Country, AttackType, TargetType


def calculate_fatal_event_score():
    return (func.coalesce(Event.kill_number, 0) * 2 + func.coalesce(Event.wound_number, 0)).label("score")

def get_most_fatal_attack_type(session, limit):
    with session() as session:
        query = (
            session.query(AttackType.attack_type).join(Event, Event.attack_type_id == AttackType.id)
            .add_columns(calculate_fatal_event_score())
            .order_by(AttackType.attack_type,desc(calculate_fatal_event_score()))
        )
        if limit:
            query = query.limit(limit)
        result = query.all()
        result = [
            {"attack_type": row[0], "fatal_score":row[1]}
            for row in result
        ]
        return result

print(get_most_fatal_attack_type(session_maker, 5))

def get_mean_fatal_event_for_country(session: Callable[[], Session], limit):
    with session() as session:
        try:
            results = (
                session.query(
                    Country.country.label("country"),
                    func.avg(calculate_fatal_event_score()).label("mean_score")
                )
                .join(Country, Event.country_id == Country.id)
                .group_by(Country.country)
                .order_by(desc("mean_score"))
            )
            if limit:
                query = results.limit(limit)
            query = query.all()
            mean_fatal = [
                {"country": row.country, "fatal_avg": float(row.mean_score)}
                for row in query
            ]
            return mean_fatal
        except Exception as e:
            print(f"Error occurred while querying: {e}")
            return []


def get_top_terror_groups(session, limit):
    with session() as session:
        results = (
            session.query(Event.terror_group,
                          func.sum(Event.kill_number + Event.wound_number).label('total_victims'))
            .group_by(Event.terror_group)
            .order_by(desc('total_victims'))
        )
        if limit:
            query = results.limit(limit)

        all_groups = query.all()
        top_groups = [
            {"terror_group_name": row.terror_group, "total_victims": float(row.total_victims)}
            for row in all_groups
        ]
        return top_groups


def get_casualties_killers_correlation(session):
    with session() as session:
        result = (
            session.query(
                (func.coalesce(Event.kill_number, 0) + func.coalesce(Event.wound_number, 0)).label("casualties"),
                Event.killers_number
            )
            .group_by(Event.killers_number, (func.coalesce(Event.kill_number, 0) + func.coalesce(Event.wound_number, 0)))
            .all()
        )
        correlation_data = [
            {"killers_number": row.killers_number, "casualties": row.casualties}
            for row in result
        ]
        return correlation_data

def get_attack_type_target_type_correlation(session):
    with session() as session:
        correlation_data = (
            session.query(
                AttackType.attack_type,
                TargetType.target_type,
            )
            .join(Event, Event.attack_type_id == AttackType.id)
            .join(TargetType, Event.target_type_id == TargetType.id)
            .group_by(AttackType.attack_type, TargetType.target_type)
            .all()
        )
        return correlation_data


# print(get_casualties_killers_correlation(session_maker))


def get_all_events(session: Callable[[], Session]):
    with session() as session:
        events = (
            session.query(Event)
        ).all()
        return [event.__dict__ for event in events]



