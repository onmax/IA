import json 
from flask import Flask, render_template, request
app = Flask(__name__)

from server.a_star import A_star as a_star

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
    return render_template('./index.html', route=route, stations=data)