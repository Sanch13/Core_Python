import datetime

import socketio
import eventlet

sio = socketio.Server()

app = socketio.WSGIApp(sio)

users = {}


def get_formatted_time(time_: datetime.datetime) -> str:
    now = datetime.datetime.now()
    delta_time = now - time_
    seconds = delta_time.seconds
    minutes, seconds = divmod(seconds, 60)
    formatted_time = f"{minutes}:{seconds:02d}"
    return formatted_time


@sio.event
def connect(sid, environ):
    print(f"Клиент <{sid}> подключился!")
    if sid not in users:
        users[sid] = datetime.datetime.now()


@sio.event
def disconnect(sid):
    formatted_time = ''
    if sid in users:
        formatted_time += get_formatted_time(users[sid])
    print(f"Клиент <{sid}> отключился, время сессии: {formatted_time}")


if __name__ == '__main__':
    # Запускаем eventlet веб-сервер
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), app)
