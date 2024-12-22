import pandas as pd
from pandas import DataFrame
from toolz import *
import numpy as np
from app.db.database import session_maker
from app.repository.statistics_repository import \
     get_casualties_killers_correlation


def convert_to_dataframe(data):
    stream = pipe(
        data,
        partial(
            map,
            lambda model:
            {key: value for key, value in model.items() if key != '_sa_instance_state'}
        ),
        list
    )
    df = pd.DataFrame(stream)
    return df


def calculate_fatal_score(df: DataFrame, limit):
    df["fatal_score"] = (df["kill_number"].fillna(0) * 2) + (df["wound_number"].fillna(0) * 1)
    top_events = df.sort_values(by="fatal_score", ascending=False).head(limit)
    return top_events


def calculate_correlation_from_results(result1, result2, key1, key2):
    values1 = [row[key1] for row in result1]
    values2 = [row[key2] for row in result2]

    correlation = np.corrcoef(values1, values2)[0, 1]

    return correlation


def calculate_percentage_change_attacks_by_region(res):
    df = pd.DataFrame(res, columns=["country", "city", "region", "date", "attack_count", "longitude", "latitude"])
    df["percentage_change"] = (
            df.groupby("region")["attack_count"]
            .pct_change() * 100
    )
    df = df.dropna()
    return df.to_dict(orient="records")
