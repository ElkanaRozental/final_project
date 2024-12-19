import pandas as pd
from pandas import DataFrame
import toolz as t

from app.db.database import session_maker
from app.repository.statistics_repository import get_all_events



def convert_to_dataframe(data):
    stream = t.pipe(
        data,
        t.partial(
            map,
            lambda event:
            {key: value for key, value in event.items() if key != '_sa_instance_state'}
        ),
        list
    )
    df = pd.DataFrame(stream)
    return df



def calculate_fatal_score(df: DataFrame, limit):
    df["fatal_score"] = (df["kill_number"].fillna(0) * 2) + (df["wound_number"].fillna(0) * 1)
    top_events = df.sort_values(by="fatal_score", ascending=False).head(limit)
    return top_events

print(calculate_fatal_score(convert_to_dataframe(get_all_events(session=session_maker)), 5))