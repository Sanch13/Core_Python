import socketio
import eventlet

sio = socketio.Server()

app = socketio.WSGIApp(sio)

users = []


def get_status_server() -> None:
    if len(users) == 1:
        print("Пользователь один")

    if len(users) >= 2:
        print("Команда в сборе")


def is_users_empty() -> None:
    if not users:
        print("Сервер пуст")


@sio.event
def connect(sid, environ):
    is_users_empty()
    print(f"Клиент <{sid}> подключился!")
    users.append(sid)
    get_status_server()


@sio.event
def disconnect(sid):
    print(f"Клиент <{sid}> отключился")
    users.remove(sid)
    get_status_server()
    is_users_empty()


if __name__ == '__main__':
    # Запускаем eventlet веб-сервер
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), app)
