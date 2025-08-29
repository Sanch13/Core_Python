import socketio
import eventlet

sio = socketio.Server()

app = socketio.WSGIApp(sio)


users = []


# Обработчик события подключения
@sio.event
def connect(sid, environ):
    print(f"Клиент {sid} подключен")
    users.append(sid)
    sio.emit(event='message', to=sid, data={"users": users, "online": len(users)})


@sio.event
def disconnect(sid):
    if sid in users:
        users.remove(sid)
    print(f"Клиент {sid} отключен")


if __name__ == '__main__':
    # Запускаем eventlet веб-сервер
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), app)
