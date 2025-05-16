import socketio
import eventlet

sio = socketio.Server()

app = socketio.WSGIApp(sio)

lost_queries = {"lost": 0}


# Обработчик события подключения
@sio.event
def connect(sid, environ):
    print(f"Клиент {sid} подключен")


@sio.on("count_queries")
def count_queries(sid, data):
    sio.emit("count_queries", data=lost_queries, to=sid)


@sio.on("*")
def catch_all(event, sid, data):
    lost_queries["lost"] += 1
    sio.emit("")


@sio.event
def disconnect(sid):
    print(f"Клиент {sid} отключен")


if __name__ == '__main__':
    # Запускаем eventlet веб-сервер
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), app)
