import json
import math


class A_star():
    destination = ''
    json = ''
    useless_stations = []
    route = []

    def load_station(self, name):
        for line in self.json:
            for station in self.json[line]:
                if station["name"] == name:
                    return station

    def get_connected_stations(self, station):
        stations = []
        for s in station["connected_to"]:
            stations.append(self.load_station(s))
        return stations

    def get_distance(self, station1, station2):
        return math.sqrt((station1["x"] - station2["x"])**2 + (station1["y"] - station2["y"])**2)

    def which_is_closest(self, candidates):
        current_closest_distance = 99999999
        current_closest = {}
        for name in candidates:
            for candidate in candidates[name]:
                d = self.get_distance(candidate, self.destination)
                if d < current_closest_distance:
                    current_closest_distance = d
                    current_closest = candidate
        return current_closest

    def remove_useless_stations(self, posibilities):
        for station in posibilities:
            if station in self.useless_stations or station in self.route:
                posibilities.remove(station)
        return posibilities
    '''
    1. Comprobobar que no sea si mismo
    2. Coger adyacentes
    3. Comprobar cual es mas cercano
    4.
    '''

    def main(self, current, candidates={}):

        posibilities = self.get_connected_stations(current)
        candidates[current["name"]] = self.remove_useless_stations(
            posibilities)

        new = self.which_is_closest(candidates)

        self.route.append(new)
        for s in self.route:
            print(s["name"])
        if new["x"] == self.destination["x"] and new["y"] == self.destination["y"] and new["name"] == self.destination["name"]:
            return
        else:
            self.main(new, candidates)

    def __init__(self, origin, destination):
        if origin == destination:
            print("Su destino y origen son lo mismo")
            return

        with open('../data/data.json') as data:
            self.json = json.load(data)

        origin = self.load_station(origin)
        self.destination = self.load_station(destination)
        self.route = [origin]

        self.main(origin)


A_star("Minor", "Beruni")
