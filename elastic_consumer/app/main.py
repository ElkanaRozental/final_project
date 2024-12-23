import os
from app.consume_settings.consumer import consume_topic
from app.db.elastic_connect import elastic_client
from app.repository.insert_repository import insert

if __name__ == '__main__':
    # elastic_client.indices.delete(index='nowadays_data_index', ignore=[400, 404])
    # elastic_client.indices.delete(index='historical_data_index', ignore=[400, 404])
    consume_topic(os.environ["ELASTIC_TOPIC"], insert)