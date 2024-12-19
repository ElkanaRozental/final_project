from app.db.database import session_maker
from app.repository.insert_repository import insert_normalized_message
from app.service.normalize_data import normalize_message
from app.service.read_file import read_csv, terror_data_path


def read_and_insert_terror_data():
    terror_data = read_csv(terror_data_path)
    # batch_size = 200
    # batch = []
    for terror in terror_data:
        terror = normalize_message(terror)
        insert_normalized_message(terror, session=session_maker)
        # batch.append(terror)
    #     if len(batch) == batch_size:
    #         for x in batch:
    #             insert_normalized_message(x, session=session_maker)
    #         batch = []
    # if batch:
    #     for x in batch:
    #         insert_normalized_message(x, session=session_maker)