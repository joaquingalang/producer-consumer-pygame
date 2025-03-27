from random import randint
from datetime import datetime

class Producer:

    def __init__(self):
        self.value = None
        self.timestamp = None
        self.isEmpty = True

    def spawn(self):
        if (self.isEmpty):
            self.value = randint(1, 100)
            self.timestamp = datetime.now()
            self.isEmpty = False

    def supply(self):
        if (not self.isEmpty):
            value = self.value
            self.value = None
            self.timestamp = None
            self.isEmpty = True
            return value
    
