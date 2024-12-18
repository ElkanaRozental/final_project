import csv
import json
import os

from app.db.database import session_maker
from app.repository.insert_repository import insert_normalized_message
from app.service.normalize_data import normalize_message


def read_csv(csv_path: str):
    try:
        with open(csv_path, mode='r', encoding='iso-8859-1') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


terror_data_path = "./data/globalterrorismdb_0718dist-1000 rows.csv"
