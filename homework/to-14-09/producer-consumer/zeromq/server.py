import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

items = 0
max_items = 10

def isAvailableConsume(): return items > 0
def isAvailableProduce(): return items < max_items

def producer():
    if not isAvailableProduce(): return "Full"
    global items
    items += 1
    return items

def consumer():
    if not isAvailableConsume(): return "Empty"
    global items
    items -= 1
    return items

while True:
    #  Wait for next request from client
    function = socket.recv()
    print("Received request: %s" % function)

    if function == b"Producer":
        socket.send_string(str(producer()))

    if function == b"Consumer":
        socket.send_string(str(consumer()))

    #  Send reply back to client
    # socket.send_string(str(function))