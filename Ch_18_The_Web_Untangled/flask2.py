from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def home():
#     return app.send_static_file('templates/flask2.html')


@app.route('/echo/<thing>')
def echo(thing):
    return render_template("flask2.html", thing=thing)


app.run(port=9999, debug=True)
# http://localhost:9999/echo/Gamera