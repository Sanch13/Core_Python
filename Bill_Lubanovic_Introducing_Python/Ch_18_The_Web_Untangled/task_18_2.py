from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def home():
    thing = request.values.get('thing')
    height = request.values.get('height')
    color = request.values.get('color')
    return render_template('home.html', thing=thing, height=height, color=color)


app.run(port=5000, debug=True)

# http://localhost:5000/?thing=Octothorpe&height=7&color=green
