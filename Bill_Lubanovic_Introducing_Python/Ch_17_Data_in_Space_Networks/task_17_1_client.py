import socket


address = ('127.0.0.1', 9090)
print(f'Client : Hey. I am client.  Send me time UTC.')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET означает, что мы создаем интернет-сокет (IP).
# SOCK_STREAM, чтобы получить потоковый протокол TCP
client.connect(address)
client.sendall(b'time')
"""вызоваем connect() с целью установить поток между клиентом и сервером"""
answer_form_server = client.recv(1024)  # 1024 байт принимаем
"""Теперь client просто ждет прихода данных от сервера (recv). метод recv, который в качестве
аргумента принимает количество байт для чтения. Когда данные появляются, они записываються в
 answer_form_server
"""
print(f'Client : Time UTC is {answer_form_server.decode("utf-8")}')
client.close()  # Закрываем соединение с сервером
print(f'Client : Client has closed. Bye bye')

