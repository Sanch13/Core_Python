import socketio
import uvicorn
from fastapi import FastAPI, Body

app = FastAPI()
sio = socketio.AsyncServer(async_mode='asgi')
socket_app = socketio.ASGIApp(sio, app)

storage = []


@sio.event
async def connect(sid, environ):
    storage.append(sid)
    print(f"Пользователь {sid} подключился")


@sio.event
async def disconnect(sid):
    if sid in storage:
        storage.remove(sid)
    print(f"Пользователь {sid} отключился")


@app.get("/")
async def get_index():
    await sio.emit("message", {"text": "someone visited over http"})
    return f"{storage}"


@app.post("/")
async def get_index(text: str = Body(embed=True)):
    await sio.emit("message", data=text)
    return f"{text}"


if __name__ == '__main__':
    uvicorn.run(socket_app, host='0.0.0.0', port=8000)
