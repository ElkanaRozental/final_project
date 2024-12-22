from app.db.database import create_tables, create_db, create_indexes
from app.service.insert_service import read_and_insert_terror_data

if __name__ == '__main__':
    create_db()
    create_tables()
    read_and_insert_terror_data()
    create_indexes()