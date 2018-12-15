import json

'''
Array de salida (return)
1. Origen
2. Todas intercambiadores intermedios
3. Destino
'''

def get_color(data, station):
    for color in data:
        for _station in data[color]:
            if _station["name"] == station["name"]:
                return color
def unit_to_km(distance):
    ratio = 18.0267
    return ratio*distance/1000 # Divided by 1000 to convert meters to km
def get_time(distance):
    #get the distance in km
    distance = unit_to_km(distance)

    # Time taken in hours
    # We assume that the subway velocity is 45km/h
    time = distance / 45

    # transform hours to minutes
    time *= 60

    return time

def main(arr, data):
    nstations = 0
    res = []

    for i,station in enumerate(arr):
        if i == 0 or i == len(arr) -1:
            res.append([{"name": station["name"]  , "line": get_color(data, station), "time": get_time(station["g_score"]), "nstations": i - nstations}])
            nstations = i
        if i < len(arr) - 1 and station["x"] == arr[i + 1]["x"] and station["y"] == arr[i + 1]["y"]:
            res.append([{"name": station["name"],"line": get_color(data, station), "time": get_time(station["g_score"]), "nstations": i - nstations },{"name": arr[i+1]["name"],"line": get_color(data, arr[i+1]), "time": get_time(station["g_score"]), "nstations": i - nstations }])
            nstations = i

    return res

