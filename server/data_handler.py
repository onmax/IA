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
    #get the distance in km
    ratio = 18.0267
    distance = ratio*distance/1000 # Divided by 1000 to convert meters to km
    # Time taken in hours
    # We assume that the subway velocity is 45km/h
    time = distance / 45

    # transform hours to minutes
    time *= 60
    return time

def get_time(distance, nstations):
    # minutes in the train + minutes changing lines 
    return unit_to_km(distance) + nstations * 3

def main(arr, data):
    nstations = 0
    res = []

    for i,station in enumerate(arr):
        # If it is origin or destination
        if i == 0 or i == len(arr) -1:
            res.append([{"name": station["name"]  , "line": get_color(data, station), "nstations": i - nstations}])
            nstations = i

        # If interchange statin
        if i < len(arr) - 1 and station["x"] == arr[i + 1]["x"] and station["y"] == arr[i + 1]["y"]:
            res.append([{"name": station["name"],"line": get_color(data, station), "nstations": i - nstations },{"name": arr[i+1]["name"],"line": get_color(data, arr[i+1]), "nstations": i - nstations }])
            nstations = i

    return res

