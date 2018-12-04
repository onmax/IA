import json 
from flask import Flask, render_template, request
app = Flask(__name__)

from server.a_star import A_star as a_star

<<<<<<< HEAD
@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/route', methods=['GET'])
def route():
    print(999)
    route = {}
    with open('./data/data.json') as d:
        data = json.load(d)
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    route = (a_star(origin, destination, data)).all_route
    print(route)
=======
@app.route('/', methods=['GET'])
def index():
    route = {}
    if request.method == 'GET':
        origin = request.args.get('origin')
        destination = request.args.get('destination')
        route = a_star(origin, destination, json).route
>>>>>>> a909ac38d3c4bb688373285debdd7f1f5ec435e0
    return render_template('./index.html', route=route, stations=data)