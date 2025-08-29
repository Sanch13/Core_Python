import socketio
import eventlet

sio = socketio.Server()

app = socketio.WSGIApp(sio)

users = {}


# Обработчик события подключения
@sio.event
def connect(sid, environ):
    if sid not in users:
        users[sid] = {"score": 0}
    print(f"Клиент {sid} подключен")


@sio.on("increase")
def increase(sid, data):
    if sid in users:
        users[sid]["score"] += 1


@sio.on("decrease")
def decrease(sid, data):
    if sid in users and users[sid]["score"] > 0:
        users[sid]["score"] -= 1


@sio.on("get_score")
def get_score(sid, data):
    sio.emit(event="get_score", data=users.get(sid), to=sid)


@sio.event
def disconnect(sid):
    print(f"Клиент {sid} отключен")


if __name__ == '__main__':
    # Запускаем eventlet веб-сервер
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), app)
