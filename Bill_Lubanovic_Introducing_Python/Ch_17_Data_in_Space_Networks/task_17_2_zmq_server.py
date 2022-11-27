import zmq, pickle
from datetime import datetime

host, port = '127.0.0.1', 9090

print(f'Server : Hey. I am server. I am ready for work')
context = zmq.Context()
# создаем объект типа Context — это объект ZeroMQ, который сопровождает состояние.
server = context.socket(zmq.REP)
# создаем сокет ZeroMQ, имеющий тип REP (получено от REPly — ответ)
server.bind(f'tcp://{host}:{port}')
# метод bind() заставляет слушать определенный IP-адрес и порт.
request_from_client = pickle.loads(server.recv(1024))     # получаем данные от клиента
if request_from_client == 'time':     # если данные от клиента равны  time
    print(f'Server : Create time utc in ISO')
    utc_time = pickle.dumps(datetime.utcnow().isoformat())       # генерируем время utc
    # используя сериализатор pickle переводим данные (time utc) в байты
    print(f'Server : Send data to client')
    server.send(utc_time)                   # отправляем ответ клиенту
server.close()                              # закрываем сервер



