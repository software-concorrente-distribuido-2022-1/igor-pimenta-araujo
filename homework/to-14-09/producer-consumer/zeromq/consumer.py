import zmq
import time

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    time.sleep(1)
    print("Sending request %s …" % request)
    socket.send_string("Consumer")

    #  Get the reply.
    message = socket.recv()
    print("Item consumido. Total: " + str(message))