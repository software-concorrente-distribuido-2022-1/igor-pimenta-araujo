import Pyro4

@Pyro4.expose
class Box:
    def __init__(self):
        self.items = 0
        self.max_items = 10

    def isAvailableToProduce(self):
        return self.items != self.max_items

    def isAvailableToConsume(self):
        return self.items > 0
        
    def produce(self):
        if self.isAvailableToProduce():
            self.items += 1
        return self.items
    
    def consume(self):
        if self.isAvailableToConsume():
            self.items -= 1
        return self.items

Pyro4.Daemon.serveSimple({Box: 'Box',}, host="0.0.0.0", port=9090, ns=False, verbose=True)