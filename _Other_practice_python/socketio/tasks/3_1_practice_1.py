import socketio
import uvicorn
from fastapi import FastAPI, Body

app = FastAPI()
sio = socketio.AsyncServer(async_mode='asgi')
socket_app = socketio.ASGIApp(sio, app)

storage = []
room_name = 'lobby'


@sio.event
async def connect(sid, environ):
    print(f"Пользователь {sid} подключился")
    await sio.enter_room(sid, room=room_name)  # вход в комнату
    #  отсылаем data на подписанное событие update кроме подлкюч. sid
    await sio.emit(event="update", data={"message": f"user_joined sid={sid}"}, skip_sid=sid, room=room_name)


@sio.event
async def disconnect(sid):
    print(f"Пользователь {sid} отключился")
    await sio.leave_room(sid, room=room_name)  # выход из комнаты
    #  отсылаем data на подписанное событие update кроме отключ. sid
    await sio.emit(event="update", data={"message": f"user leave chat sid={sid}"}, skip_sid=sid, room=room_name)


if __name__ == '__main__':
    uvicorn.run(socket_app, host='0.0.0.0', port=8000)
