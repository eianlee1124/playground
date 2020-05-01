import zmq
import json

ctx = zmq.Context()
sock = zmq.Socket(ctx, zmq.PUB)
sock.bind('tcp://*5556')

class ZeroMQSocketHandler(QueueHandler):
    def enqueue(self, record):
        self.queue.send_json(record.__dict__)

handler = ZeroMQSocketHandler(sock)
