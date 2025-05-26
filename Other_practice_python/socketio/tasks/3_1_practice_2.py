import socketio
import uvicorn

sio = socketio.AsyncServer(async_mode='asgi')
socket_app = socketio.ASGIApp(sio)

storage = {}
room_name = 'lobby'


async def update_storage(room: str, sid: str):
    if sid not in storage.get(room, []):
        storage.setdefault(room, []).append(sid)


@sio.event
async def connect(sid, environ):
    print(f"Пользователь {sid} подключился")
    await update_storage(room_name, sid)

    await sio.enter_room(sid, room=room_name)  # вход в комнату
    #  отсылаем data на подписанное событие update кроме подлкюч. sid
    await sio.emit(event="update", data=storage, skip_sid=sid, room=room_name)


@sio.on("join")
async def join(sid, data):
    room = data.get("room")
    await update_storage(room, sid)

    await sio.enter_room(sid, room=room)  # вход в комнату
    await sio.emit(event="update", data=storage, skip_sid=sid, room=room_name)


@sio.event
async def disconnect(sid):
    print(f"Пользователь {sid} отключился")
    for_delete = []
    for room, list_sids in storage.items():
        if sid in list_sids:
            list_sids.remove(sid)
            if not list_sids:
                for_delete.append(room)

    for room in for_delete:
        del storage[room]

    #  отсылаем data на подписанное событие update кроме подлкюч. sid
    await sio.emit(event="update", data={"message": f"user leave chat"}, skip_sid=sid, room=room_name)
    await sio.emit(event="update", data=storage, skip_sid=sid, room=room_name)


if __name__ == '__main__':
    uvicorn.run(socket_app, host='0.0.0.0', port=8000)
