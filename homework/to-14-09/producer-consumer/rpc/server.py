from xmlrpc.server import SimpleXMLRPCServer

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

box = Box()

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(box.consume, "consume")
server.register_function(box.produce, "produce")
server.serve_forever()