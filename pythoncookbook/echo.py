from functools import partial
from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)
        
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT: ' + line)

serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVE:'))
serv.serve_forever()