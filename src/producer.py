import csv
import json
from azure.eventhub import EventHubProducerClient, EventData

producer = EventHubProducerClient.from_connection_string(
    "xxxxx", eventhub_name="pedidos"
)

with open("data/Sales Transaction v.4a.csv") as f:
    reader = csv.DictReader(f)
    batch = []

    for row in reader:
        batch.append(EventData(json.dumps(row)))

    with producer:
        producer.send_batch(batch)
