from fastapi import FastAPI, Body, Response, Header
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/hello")  # простой URL
def greet():
    return "Hello? World?"


@app.get("/hey/{who}")  # параметр в пути URL
def greet1(who):
    return f"Hello? {who}?"


@app.get("/hi")  # в качестве параметра запроса после символа ? в URL
def greet2(who):
    return f"Hello? {who}?"


@app.post("/data")
def data(who: str = Body(embed=True)):  # Выражение Body(embed=True) мы получаем значение who из тела запроса в формате JSON
    return f"Hello {who}"


@app.post("/header")
def header(user_agent: str = Header()):  # передать аргумент в качестве HTTP-заголовка
    return f"{user_agent}"


@app.get("/happy")
def happy(status_code=200):
    return ":)"


@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"
