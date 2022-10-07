import zmq, pickle

host, port = '127.0.0.1', 9090

print(f'Client : Hey. I am client.  Send me time UTC.')
context = zmq.Context()
# создаем объект типа Context — это объект ZeroMQ.
client = context.socket(zmq.REQ)
client.connect(f'tcp://{host}:{port}')          # коннектимся к серверу
client.send(pickle.dumps('time'))             # пересылаем данные time через  сериализатор pickle
reply_from_server = pickle.loads(client.recv(1024))    # получаем time utc от сервера
print(f'Client : Time UTC is {reply_from_server}')
client.close()  # Закрываем соединение с сервером
print(f'Client : Client has closed. Bye bye')


