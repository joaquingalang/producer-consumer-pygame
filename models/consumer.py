class Consumer:

    def __init__(self):
        self.store = None
        self.isEmpty = True

    def feed(self, value):
        if (self.isEmpty):
            self.store = value
            self.isEmpty = False

    def digest(self):
        if (not self.isEmpty):
            self.store = None
            self.isEmpty = True