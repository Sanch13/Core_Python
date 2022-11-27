import re
import time
import zmq
import pickle
from Bill_Lubanovic_Introducing_Python.Ch_12_Wrangle_and_Mangle_Data.Wrangl_and_Mangle_Data import mammoth

poem_list = re.findall(r"\b[a-zA-Z][^\d\s]*\b", mammoth)   # выделяем только слова из стиха mammoth
# print(*[poem_list[i:i + 7] for i in range(0, len(poem_list), 7)], sep='\n')

host, port = '127.0.0.1', 9090

print(f'Server : Hey. I am server. I am ready for work')
context = zmq.Context()
# создаем объект типа Context — это объект ZeroMQ.
pub = context.socket(zmq.PUB)        # создаем сервер-публикатор PUB
pub.bind(f'tcp://{host}:{port}')     # метод bind() заставляет слушать определенный IP-адрес и порт
"""Есть проблема медленного присоединившегося: даже если вы запустите клиент раньше сервера, 
тот начнет отправлять данные сразу после запуска, а клиенту потребуется некоторое время, чтобы
подключиться к серверу."""
time.sleep(1)       # спим 1 секунду
"""Простейший способ исправить это — заставить публикатор пропустить секунду после вызова метода
bind() и до того, как он начнет отправлять сообщения."""
for word in poem_list:                  # итерируемся по списку
    word_bytes = pickle.dumps(word)     # преобразуем строку в байтовую строку
    pub.send_multipart([b'words', word_bytes])  # отсылаем тему и слово в байтовом виде
print(f'Server : I has closed my work')     # выводим в консоль
pub.close()