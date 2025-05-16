import socketio
import eventlet

sio = socketio.Server()

app = socketio.WSGIApp(sio)

users = []


# Обработчик события подключения
@sio.event
def connect(sid, environ):
    print(f"Клиент <{sid}> подключился!")
    users.append(sid)
    print(f"Клиент подключился!")
    print(f"{users}")


@sio.event
def disconnect(sid):
    print(f"Клиент <{sid}> отключился")
    if sid in users:
        users.remove(sid)
    print(f"{users}")


if __name__ == '__main__':
    # Запускаем eventlet веб-сервер
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), app)
