import zmq
import pickle


host, port = '127.0.0.1', 9090

print(f'Client : Hey. I am client.  Send me words\n')
context = zmq.Context()
# создаем объект типа Context — это объект ZeroMQ.
sub = context.socket(zmq.SUB)        # создаем подписчика SUB
sub.connect(f'tcp://{host}:{port}')  # подключ. к серверу
sub.setsockopt(zmq.SUBSCRIBE, b'words')
# Подписываемся на байтовую строку b'words'(тема). Если вы хотите подписываться на все темы,
# то нужно подписаться на пустую строку байтов ''
while True:
    words, word = sub.recv_multipart()  # считываем с сервера тему и слово в байтах
    word = pickle.loads(word)           # переводим в строку из байтов
    if len(word) == 5 and word.isalpha():         # если слово состоит из 5 букв
        print(f"Client : Word [ {word} ] consists 5 of letters")    # вывод в консоль






