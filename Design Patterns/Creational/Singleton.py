"""
Singleton Pattern

- Singleton pattern is a design pattern that ensures a class has only one instance and provides a global point of access to it.

Use Case:
- We need to create a singleton class for the database connection.
- We need to create a singleton class for the Kafka Producer connection.
- We need to create a singleton class for the Unified Logger service.

Pros:
- We can ensure that there is only one instance of the class.

Cons:
- In case of multi-threaing, ensure proper locking mechanism to avoid race conditions.
- Difficult to test as it is global and can be accessed from anywhere, can not predict behavior.
- Singleton doesn't matter in multi-instance servers.
"""
from kafka import KafkaProducer
import logging

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class KafkaProducerConnection(metaclass=MetaSingleton):
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def get_producer(self):
        return self.producer

class LoggerService(metaclass=MetaSingleton):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_logger(self):
        return self.logger

kafka_producer_connection = KafkaProducerConnection()
logger_service = LoggerService()
print(kafka_producer_connection)
print(logger_service)
