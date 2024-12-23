from sqlalchemy import func
from sqlalchemy.orm import Query
from app.models import Country, Province, Region, City, Event


def filter_and_return_all(
        limit: int, country: Country,
        province: Province,
        region: Region,
        city: City, result: Query):
    if country:
        result = result.filter(Country.country == country)
    if province:
        result = result.filter(Province.province == province)
    if region:
        result = result.filter(Region.region == region)
    if city:
        result = result.filter(City.city == city)
    if limit:
        result = result.limit(limit)
    return result.all()


def avg_calculator(res):
    scores = [row.score for row in res if row.score is not None]
    return sum(scores) / len(scores)


def calculate_fatal_event_score():
    return (func.coalesce(Event.kill_number, 0) * 2 + func.coalesce(Event.wound_number, 0)).label("score")

def normalize_elastic_response(res):
    res = [
        {
            "country": row["_source"].get("country", None),
            "city": row["_source"].get("city", None),
            "longitude": float(row["_source"]["longitude"]) if row["_source"].get("longitude") not in [None, ""] else None,
            "latitude": float(row["_source"]["latitude"]) if row["_source"].get("latitude") not in [None, ""] else None,
            "description": row["_source"].get("description", None),
        }
        for row in res["hits"]["hits"]
        if row["_source"].get("longitude") not in [None, ""] and row["_source"].get("latitude") not in [None, ""]
    ]
    print(res)
    return res
