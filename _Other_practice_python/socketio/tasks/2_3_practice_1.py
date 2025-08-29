import socketio
import eventlet

sio = socketio.Server()

app = socketio.WSGIApp(sio)


# Обработчик события подключения
@sio.event
def connect(sid, environ):
    print(f"Клиент {sid} подключен")
    sio.emit(event="message", to=sid, data={"message": "Welcome to the server"})


@sio.event
def disconnect(sid):
    print(f"Клиент {sid} отключен")


if __name__ == '__main__':
    # Запускаем eventlet веб-сервер
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), app)
