from xmlrpc.server import SimpleXMLRPCServer
import pickle
from datetime import datetime

print(f'Server : Hey. I am server. I am ready for work')


def get_time(string):
    if string == "time":
        return datetime.now().isoformat()


server = SimpleXMLRPCServer(("localhost", 6789))
# создаем сервер и передаем host and port. Он будет постоянно "слушать"!
server.register_function(get_time, 'get_time')
# регистрируем функцию, чтобы сделать ее доступной клиентам с помощью RPC
server.serve_forever()


