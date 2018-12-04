import json
#arr = [{'x': 351, 'y': 995, 'name': 'Beruni', 'connected_to': ['Tinchlik'], "g_score":17.8}, {'x': 407, 'y': 925, 'name': 'Tinchlik', 'connected_to': ['Beruni', 'Chorsu'], "g_score":17.8}, {'x': 475, 'y': 880, 'name': 'Chorsu', 'connected_to':['Gafur Golum', 'Tinchlik'], "g_score":17.8}, {'x': 526, 'y': 901, 'name': 'Gafur Golum', 'connected_to': ['Alisher Navoi', 'Chorsu'], "g_score":17.8}, {'x': 550, 'y': 847, 'name': 'Alisher Navoi', 'connected_to': ['Gafur Golum', 'Uzbekistan', 'Pakhtakor'], "g_score":17.8}, {'x': 550, 'y': 847, 'name': 'Pakhtakor', 'connected_to': ['Bunyodkor', 'Mustakillik Maydoni', 'Alisher Navoi'], "g_score":17.8}, {'x': 619, 'y': 836, 'name': 'Mustakillik Maydoni', 'connected_to': ['Pakhtakor', 'Amir Temur Hiyoboni'], "g_score":17.8}, {'x': 682, 'y': 818, 'name': 'Amir Temur Hiyoboni', 'connected_to': ['Mustakillik Maydoni', 'Khamid Alimjan', 'Yunus Rajably'], "g_score":17.8}, {'x': 682, 'y': 818, 'name': 'Yunus Rajably', 'connected_to': ['Ming Urik', 'Abdulla Kodiriy', 'Amir Temur Hiyoboni'], "g_score":17.8}, {'x': 667, 'y': 850, 'name': 'Abdulla Kodiriy', 'connected_to': ['Yunus Rajably', 'Minor'], "g_score":17.8}, {'x': 675, 'y': 907, 'name': 'Minor', 'connected_to': ['Abdulla Kodiriy', 'Bodomzor'], "g_score":17.8}]

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
def unit_to_meters (distance):
    ratio = 18.0267
    return ratio*distance

def main(arr, data):
    res = []

    for i,station in enumerate(arr):
        if i == 0 or i == len(arr) -1:
            res.append([{"name": station["name"]  , "line": get_color(data, station), "time": unit_to_meters(station["g_score"])*3/25, "nstations": + i}])
        if i < len(arr) - 1 and station["x"] == arr[i + 1]["x"] and station["y"] == arr[i + 1]["y"]:
            res.append([{"name": station["name"],"line": get_color(data, station), "time": unit_to_meters(station["g_score"])*3/25, "nstations": + i },{"name": arr[i+1]["name"],"line": get_color(data, arr[i+1]), "time": unit_to_meters(station["g_score"])*3/25, "nstations": + i+1}])

    return res

