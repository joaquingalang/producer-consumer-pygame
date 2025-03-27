from models.producer import Producer
from models.consumer import Consumer

class ProdConEnvironment:

    def __init__(self, size=7):
        
        # Semaphores
        self.mutex = False
        self.full = 0
        self.empty = size

        # Stores Values in Buffer
        self.buffer = []
        self.max_buffer_size = size
        self.current_buffer_size = size

        # List of Producers
        self.producers = []

        # List of Consumers
        self.consumers = []

    def increase_buffer_size(self):
        if (self.current_buffer_size < self.max_buffer_size):
            self.current_buffer_size += 1

    def decrease_buffer_size(self):
        if (self.current_buffer_size > 1):
            self.current_buffer_size -= 1

    def add_prod(self):
        if (len(self.producers) < 5):
            producer = Producer()
            self.producers.append(producer)

    def add_con(self):
        if (len(self.consumers) < 5):
            consumer = Consumer()
            self.consumers.append(consumer)

    def delete_prod(self):
        if (len(self.producers) > 0):
            self.producers.pop()

    def delete_con(self):
        if (len(self.consumers) > 0):
            self.consumers.pop()

    def produce(self):
        for prod in self.producers:
            prod.spawn()

    def consume(self):
        for con in self.consumers:
            con.feed()

    

    
