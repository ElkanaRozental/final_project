from app.db.elastic_db import elastic_client
import os
from dotenv import load_dotenv

from app.service.queries_service import normalize_elastic_response

load_dotenv(verbose=True)


def search_news_fuzzy(limit, keyword):
    try:
        query = {
            "query": {
                "match": {
                    "description": {
                        "query": keyword,
                        "fuzziness": "AUTO"
                    }
                }
            },
            "size": limit
        }
        response = elastic_client.search(index=os.environ["NOWADAYS_DATA_INDEX"], body=query)
        return normalize_elastic_response(response)
    except Exception as e:
        print(str(e))

def search_historic_fuzzy(limit, keyword):
    try:
        query = {
            "query": {
                "match": {
                    "description": {
                        "query": keyword,
                        "fuzziness": "AUTO"
                    }
                }
            },
            "size": limit
        }
        response = elastic_client.search(index=os.environ["HISTORICAL_DATA_INDEX"], body=query)
        return normalize_elastic_response(response)
    except Exception as e:
        print(str(e))

def search_old_with_date_fuzzy(limit, keyword, start_date, end_date):
    try:
        query = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "description": {
                                    "query": keyword,
                                    "fuzziness": "AUTO"
                                }
                            }
                        }
                    ],
                    "filter": {
                        "range": {
                            "timestamp": {
                                "gte": start_date,
                                "lte": end_date
                            }
                        }
                    }
                }
            },
            "size": limit
        }
        response = elastic_client.search(
            index=os.environ["HISTORICAL_DATA_INDEX"],
            body=query
        )
        return normalize_elastic_response(response)
    except Exception as e:
        print(str(e))

def search_new_with_date_fuzzy(limit, keyword, start_date, end_date):
    try:
        query = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "description": {
                                    "query": keyword,
                                    "fuzziness": "AUTO"
                                }
                            }
                        }
                    ],
                    "filter": {
                        "range": {
                            "timestamp": {
                                "gte": start_date,
                                "lte": end_date
                            }
                        }
                    }
                }
            },
            "size": limit
        }
        response = elastic_client.search(
            index=os.environ["NOWADAYS_DATA_INDEX"],
            body=query
        )
        return normalize_elastic_response(response)
    except Exception as e:
        print(str(e))


