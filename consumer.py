from kafka import KafkaConsumer

#  REALIZAR A CONEXÃO COM O TÓPICO "python-topic"
consumer = KafkaConsumer(
    'python-topic',
     bootstrap_servers=['localhost:9092'])

# IMPRIMIR MENSAGENS RECEBIDAS DO PRODUCER
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))