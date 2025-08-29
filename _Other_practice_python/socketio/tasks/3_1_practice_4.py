import json
import pprint
from random import choice

import socketio
import uvicorn

sio = socketio.AsyncServer(async_mode="asgi")

app = socketio.ASGIApp(sio)

all_rooms = {
    "red": [],
    "green": [],
    "blue": [],
}


async def print_all_rooms():
    pprint.pprint(all_rooms)


@sio.event
async def connect(sid, environ):
    print(f"Client {sid} connected")
    room = choice(list(all_rooms.keys()))
    all_rooms[room].append(sid)
    await sio.enter_room(sid, room=room)
    await print_all_rooms()


@sio.on("message")
async def handle_message(sid, data):
    _, room = sio.rooms(sid)

    print(_, room)
    await sio.send(
        data=data,
        room=room,
        skip_sid=sid,
    )

    # text = data["text"]
    # for room, members in rooms.items():
    #     if sid in members:
    #         print(room, members)
    #         await sio.emit(event="message", room=room, data={"text": text}, skip_sid=sid)


@sio.event
async def disconnect(sid, environ):
    print(f"Client {sid} disconnected")


if __name__ == '__main__':
    print("Starting server...")
    uvicorn.run(app, host='0.0.0.0', port=8000)

