from flask import Flask, session
from checker import check_logged_in

app = Flask(__name__)

app.secret_key = "Secret_key"


@app.route("/login")
def do_login() -> str:
    """Login user in the system"""
    session["logged_in"] = True
    return "You are now logged in"


@app.route("/logout")
def do_logout() -> str:
    """Logout user in the system"""
    session.pop("logged_in", False)
    return "You are now logged out"


@app.route("/")
def hello() -> str:
    return "This is a simple webapp"


@app.route("/page1")
@check_logged_in  # check login user?
def page1() -> str:
    return "This is page1"


@app.route("/page2")
@check_logged_in
def page2() -> str:
    return "This is page2"


@app.route("/page3")
@check_logged_in
def page3() -> str:
    return "This is page3"


# @app.route("/status")
# def check_status() -> str:
#     if "logged_in" in session:
#         return "You are currently logged in"
#     return "You are NOT logged in"

if __name__ == '__main__':
    app.run(debug=True)
