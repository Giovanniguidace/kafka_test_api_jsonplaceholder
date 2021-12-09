import json
import requests
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: str(v).encode('utf-8'))

#JSON PLACEHOLDER - API TESTE

request = requests.get('https://jsonplaceholder.typicode.com/posts')
values = json.loads(request.content)
print(values)

#SEND TO TOPIC=PYTHON-TOPIC
producer.send('python-topic', values)

validar = producer.bootstrap_connected()
print("validar: ", validar)