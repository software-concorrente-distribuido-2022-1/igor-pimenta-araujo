import json
import threading

from base_server import BaseServer

class Box:
    def __init__(self):
        self.items = 0
        self.max_items = 10
        self.can_produce = True
        self.can_consume = False
        self.monitor = threading.Condition()
    
    def handle_request(self, data: str):
        request = json.loads(data)
        event_type = request.get('event_type')
        print(event_type)
        return self.produce() if event_type == 'PRODUCE' else self.consume()

    def isAvailableToProduce(self):
        return self.items != self.max_items

    def isAvailableToConsume(self):
        return self.items > 0
    
    def produce(self):
        with self.monitor: 

            if not self.isAvailableToProduce():
                print(f"Waiting to produce again")
                self.monitor.wait()

            if (self.items < self.max_items):
                self.items += 1
                print(f"Adding new item on box. Total: {self.items}")

            if (self.items == self.max_items):
                print(f"Max items on box")

            self.monitor.notify()

            return str(self.items)
    
    def consume(self):
        with self.monitor:

            if not self.isAvailableToConsume():
                print(f"Waiting to consume some item of the box")
                self.monitor.wait()

            if (self.items > 0):
                self.items -= 1
                print(f"Retrieving an item from box. Remaining: {self.items}")

            self.monitor.notify()

            return str(self.items)
            
deposit_box_server = BaseServer(3000, 1024, Box())
deposit_box_server.start_server()