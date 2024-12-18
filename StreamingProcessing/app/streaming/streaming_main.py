import os

import faust
from dotenv import load_dotenv

from app.service.normalize_data import normalize_message

# Load environment variables
load_dotenv(verbose=True)

# Faust app for stream processing
app = faust.App(
    'terror_data_streaming',  # App name
    broker="172.19.116.76:9092",  # Kafka broker
    value_serializer='json'  # Message value format
)

# Define a Kafka topic to consume_settings from
terror_topic = app.topic('terror_data')

mongodb_topic = os.environ['MONGODB_TOPIC']
postgresql_topic = os.environ['POSTGRESQL_TOPIC']

# Define an output Kafka topic to produce to
processed_topic_for_mongoDB = app.topic(mongodb_topic)
processed_topic_for_postgresQL = app.topic(postgresql_topic)


async def process_psql(messages):
    async for message in messages:
        normalize_data = normalize_message(message)

        await processed_topic_for_postgresQL.send(value=normalize_data)
        print(f"Processed and sent: {normalize_data}")