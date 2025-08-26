import pprint

import socketio
import uvicorn

sio = socketio.AsyncServer(async_mode="asgi")

app = socketio.ASGIApp(sio)

storage = {}
room_name = 'lobby'


async def print_storage():
    pprint.pprint(storage)


async def update_storage(room: str, sid: str):
    if sid not in storage.get(room, []):
        storage.setdefault(room, []).append(sid)


async def check_and_delete_sid(sid):
    for room, lists_sids in storage.items():
        if sid in lists_sids:
            print(f"Sid {sid} remove from room: {room}")
            lists_sids.remove(sid)


@sio.event
async def connect(sid, environ):
    await update_storage(room_name, sid)
    print(f"Client {sid} connected")
    await print_storage()
    await sio.emit(event="update", data=storage, skip_sid=sid)


@sio.on("join")
async def join(sid, data):
    room = data.get("room")
    if room is not None:
        await check_and_delete_sid(sid)
        await update_storage(room, sid)

        await sio.enter_room(sid, room=room)  # вход в комнату
        await print_storage()

    await sio.emit(event="update", data=storage, skip_sid=sid)


@sio.event
async def disconnect(sid, environ):
    print(f"Client {sid} disconnected")
    await check_and_delete_sid(sid=sid)
    await print_storage()
    await sio.emit(event="update", data=storage, skip_sid=sid)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
