from random import randint, shuffle
from models.producer import Producer
from models.consumer import Consumer

class ProdConEnvironment:

    def __init__(self, size=8):
        
        # Semaphores
        self.mutex = False
        self.full = 0
        self.empty = size

        # Stores Values in Buffer
        self.buffer = []
        self.max_buffer_size = size

        # List of Producers
        self.producers = []

        # List of Consumers
        self.consumers = []

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
            con.digest()

    def insert_data(self):
        if (self.mutex == False and len(self.buffer) < self.max_buffer_size):
            self.mutex = True

            # Grab a value from a producer with a value
            for prod in self.producers[::-1]:
                if (not prod.isEmpty):
                    value = prod.supply()
                    self.buffer.append(value)
                    break

            self.mutex = False

    def remove_data(self):
        if (self.mutex == False and len(self.buffer) > 0):
            self.mutex = True
            random_index = randint(0, len(self.buffer)-1)
            value = self.buffer.pop(random_index)
            
            random_index = randint(0, len(self.consumers)-1)
            con = self.consumers[random_index]
            con.feed(value)

            self.mutex = False


    

    
