import math
import json

class A_star():
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

    def which_is_closest(self):
        current_closest_distance = 99999999
        current_closest = {}
        for candidate in self.candidates:
            d = self.get_distance(candidate, self.destination) + self.g_score[candidate["name"]]
            if d < current_closest_distance:
                current_closest_distance = d
                current_closest = candidate
        return current_closest

    def reconstruct_path(self, current):
        total_path = [current]
        while current["name"] in self.route.keys():
            current = self.route[current["name"]]
            total_path = [current] + total_path
        return total_path

    def a_star(self):
        '''
        This method implements A* with a loop
        '''
        while len(self.candidates) != 0:
            current = self.which_is_closest()
            if current["name"] == self.destination["name"]:
                return self.reconstruct_path(current)
            self.candidates.remove(current)
            self.closed.append(current)

            for connected_station in self.get_connected_stations(current):
                # Ignore the station which is already evaluated.
                if connected_station in self.closed:
                    continue

                # The distance from start to a connected_station
                cost_of_time = self.g_score[current["name"]] + \
                    self.get_distance(current, connected_station)

                if connected_station not in self.candidates:  # Discover a new node
                    self.candidates.append(connected_station)
                elif cost_of_time >= self.g_score[connected_station["name"]]:
                    continue

                # This route is the best until now so we save all necessary data
                self.route[connected_station["name"]] = current
                self.g_score[connected_station["name"]] = cost_of_time
                self.f_score[connected_station["name"]] = self.g_score[connected_station["name"]] + \
                    self.get_distance(connected_station, self.destination)

    def init_variables(self, origin, destination):
        '''
        Initialize all necessary variables in variables of a class.
        It is equal to say `this.variable` in Java. In python, we use `self.variable`
        '''
        self.origin = self.load_station(origin)
        self.destination = self.load_station(destination)


        # Station which have been evaluated and are not good for our solution
        self.closed = []

        # The set of currently discovered stations that are not evaluated yet
        # Only the origin is known
        self.candidates = [self.origin]

        # For each station, which set of stations it can most efficiently be reached from
        self.route = {}

        # For each station, the cost of getting from the origin to that station.
        self.g_score = {}

        # The cost of going from start to start is zero because you are already there!!
        self.g_score[self.origin["name"]] = 0

        # For each station, the total cost of getting from the start node to the goal + the distance in line from that station to destination
        self.f_score = {}

        # For the first station, f score is the distance in line from origin to destination
        self.f_score[self.origin["name"]] = (self.origin, self.destination)

    def __init__(self, origin, destination, data):
        if origin == destination:
            print("Su destino y origen son lo mismo")
            return

        self.json = data

        self.init_variables(origin, destination)

        self.all_route = self.a_star()
        ratio = 18.0267
        print(self.g_score[self.destination["name"]] * ratio)
        print(self.get_distance(self.origin, self.destination) * ratio)
        print(self.g_score)
