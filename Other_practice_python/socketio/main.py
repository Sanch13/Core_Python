from pprint import pprint

import eventlet
import socketio

# Создаем экземпляр синхронного сервера Socket.IO
sio = socketio.Server()

# Создаем WSGI приложение и связываем его с Socket.IO
app = socketio.WSGIApp(sio)


# Обработчик события подключения
@sio.event
def connect(sid, environ):
    pprint(environ)
    print(f"Клиент {sid} подключен")


@sio.on("message")
def incoming_message(sid, data):
    print("мне сказали", data, sid)


@sio.on('*')
def catch_all(event, sid, data):
    sio.emit("error", {"message": f"No handler for event {event}"})
    

# Обработчик события отключения
@sio.event
def disconnect(sid):
    print(f"Клиент {sid} отключен")


# Запускаем eventlet веб-сервер
eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
