import pickle
import xmlrpc.client

print(f'Client : Hey. I am client.  Send me time UTC.')

proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
str_time = "time"
result = proxy.get_time(str_time)   # Функция была создана динамически с помощью сервера.
# Механизм RPC волшебным образом прикрепляет имя функции к вызову удаленного сервера.
print(f'Now time is {result}')



