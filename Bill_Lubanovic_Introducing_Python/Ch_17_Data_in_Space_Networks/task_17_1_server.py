import socket
from datetime import datetime

"""Сервер должен установить сетевое соединение с помощью двух методов, 
импортированных из пакета socket.
Первый метод - socket.socket() - создает сокет. В качестве аргументов принимает различные соединения
Второй метод - server.bind() - привязывается к нему (socket.socket()). В качестве аргументов 
принимает адрес = (IP:Port). Метод bind() слушает любые данные, приходящие на этот IP-адрес и порт.
Когда ваши программы просто беседуют друг с другом на одной машине,
вы можете использовать имя 'localhost' или эквивалентный адрес '127.0.0.1'.
"""


address = ('127.0.0.1', 9090)

print(f'Server : Hey. Server is here')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET означает, что мы создаем интернет-сокет (IP).
# SOCK_STREAM, чтобы получить потоковый протокол TCP
server.bind(address)    # слушает любые данные, приходящие на этот address ('localhost', 6789)
server.listen(5)    # сервер конфигурируется так, чтобы поставить в очередь
# пять клиентских соединений, прежде чем отказывать в следующем
client, addr = server.accept()
"""принимаем подключение с помощью метода accept, который возвращает кортеж с двумя элементами:
новый сокет и адрес клиента. Именно этот сокет и будет использоваться для приема и посылке
клиенту данных."""
data = client.recv(1024)
if data == b'time':
    utc_time = str(datetime.utcnow().isoformat())
    data = utc_time.encode('utf-8')
    print(f'Server : I am sending to client {addr} time utc.')
    client.sendall(data)
client.close()
server.close()
print(f'Server : Server has closed. Bye bye')
