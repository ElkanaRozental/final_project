import csv
import pandas as pd
import toolz as t
from itertools import chain

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


terror_data_path1 = "C:\\Users\\rozen\\Downloads\\globalterrorismdb_0718dist.csv"
terror_data_path2 = "C:\\Users\\rozen\\Downloads\\RAND_Database_of_Worldwide_Terrorism_Incidents.csv"













