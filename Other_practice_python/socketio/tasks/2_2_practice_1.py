import socketio
import eventlet

sio = socketio.Server()

app = socketio.WSGIApp(sio)

list_clients = []


# Обработчик события подключения
@sio.event
def connect(sid, environ):
    list_clients.append(sio)
    print(f"Клиент {sid} подключен")
    print('Подключен очередной клиент', {"online": len(list_clients)})


@sio.on("get_users_online")
def get_users_online(sid, data):
    sio.emit("get_users_online", {"online": len(list_clients)}, to=sid)


@sio.event
def disconnect(sid):
    list_clients.remove(sio)
    print(f"Клиент {sid} отключен")


# Запускаем eventlet веб-сервер
eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), app)
