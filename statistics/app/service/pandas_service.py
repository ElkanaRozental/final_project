import pandas as pd
from pandas import DataFrame
from toolz import *
from app.db.database import session_maker
from app.repository.statistics_repository import get_all_events, \
    get_attack_type_target_type_correlation


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




