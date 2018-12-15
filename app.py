import json
from flask import Flask, render_template, request
app = Flask(__name__)

from server.a_star import A_star as a_star
from server import data_handler as data_handler

def get_json():
    with open('./data/data.json') as d:
        return json.load(d)
data = get_json()

@app.route('/')
def index():
    return render_template('./index.html', stations=data, route=[], simple_route=[], scores=[], time = 0)

@app.route('/route', methods=['GET'])
def route():
    route = {}
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    
    a_star_solution = a_star(origin, destination, data)
    route = a_star_solution.all_route
    simple_route = data_handler.main(route, data)


    return render_template('./index.html', stations=data, route=route, simple_route=simple_route, scores=a_star_solution.iterations, time = data_handler.get_time(a_star_solution.f_score[destination], len(simple_route) - 2))

