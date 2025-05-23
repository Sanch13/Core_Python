import eventlet
import socketio

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Путь к статике
static_files = {'/': str(Path(BASE_DIR, 'static/index.html'))}

sio = socketio.Server(cors_allowed_origins='*', async_mode='eventlet')

app = socketio.WSGIApp(sio, static_files=static_files)


@sio.event
def connect(sid, environ):
    print(f"Пользователь {sid} подключился")


@sio.event
def disconnect(sid):
    print(f"Пользователь {sid} отключился")


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), app)
