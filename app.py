import json 
from flask import Flask, render_template, request
app = Flask(__name__)

from server.a_star import A_star as a_star

@app.route('/', methods=['GET'])
def index():
    with open('./data/data.json') as d:
        data = json.load(d)
    route = {}
    if request.method == 'GET':
        origin = request.args.get('origin')
        destination = request.args.get('destination')
        route = a_star(origin, destination, json).route
    return render_template('./index.html', route=route, stations=data)
