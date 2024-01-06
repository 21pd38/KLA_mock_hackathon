# main python file

# Level 0
print("----------------------------------------")
print("Level 0")
print("----------------------------------------")
n2 = [[0, 3366, 2290, 3118, 1345, 854, 1176, 1291, 1707, 2160, 1606, 702, 1820, 1985, 1838, 1515, 3370, 1643, 2874, 1418, 2495],
[3366, 0, 1076, 512, 2021, 2512, 2190, 2075, 1923, 1206, 1760, 2664, 1546, 1645, 1528, 1851, 376, 1723, 492, 1948, 1135],
[2290, 1076, 0, 1494, 945, 1436, 1114, 999, 2905, 536, 684, 1588, 876, 2627, 452, 775, 1358, 647, 716, 872, 2117],
[3118, 512, 1494, 0, 1773, 2264, 1942, 1827, 1411, 958, 1512, 2416, 1298, 1133, 1280, 1603, 252, 1475, 778, 1700, 623],
[1345, 2021, 945, 1773, 0, 491, 403, 650, 2348, 815, 261, 787, 475, 2070, 493, 170, 2025, 298, 1529, 763, 1560],
[854, 2512, 1436, 2264, 491, 0, 322, 569, 2429, 1306, 752, 868, 966, 2151, 984, 661, 2516, 789, 2020, 682, 1641],
[1176, 2190, 1114, 1942, 403, 322, 0, 247, 2751, 984, 430, 1190, 722, 2473, 662, 521, 2194, 467, 1698, 360, 1963],
[1291, 2075, 999, 1827, 650, 569, 247, 0, 2998, 869, 677, 1437, 969, 2720, 547, 768, 2079, 352, 1583, 127, 2210],
[1707, 1923, 2905, 1411, 2348, 2429, 2751, 2998, 0, 2369, 2321, 1561, 2029, 278, 2553, 2230, 1663, 2646, 2189, 3111, 788],
[2160, 1206, 536, 958, 815, 1306, 984, 869, 2369, 0, 554, 1458, 340, 2091, 322, 645, 1210, 517, 714, 742, 1581],
[1606, 1760, 684, 1512, 261, 752, 430, 677, 2321, 554, 0, 904, 292, 2043, 232, 91, 1764, 325, 1268, 790, 1533],
[702, 2664, 1588, 2416, 787, 868, 1190, 1437, 1561, 1458, 904, 0, 1118, 1283, 1136, 813, 2668, 1085, 2172, 1550, 1793],
[1820, 1546, 876, 1298, 475, 966, 722, 969, 2029, 340, 292, 1118, 0, 1751, 524, 305, 1550, 617, 1054, 1082, 1241],
[1985, 1645, 2627, 1133, 2070, 2151, 2473, 2720, 278, 2091, 2043, 1283, 1751, 0, 2275, 1952, 1385, 2368, 1911, 2833, 510],
[1838, 1528, 452, 1280, 493, 984, 662, 547, 2553, 322, 232, 1136, 524, 2275, 0, 323, 1532, 195, 1036, 558, 1765],
[1515, 1851, 775, 1603, 170, 661, 521, 768, 2230, 645, 91, 813, 305, 1952, 323, 0, 1855, 416, 1359, 881, 1442],
[3370, 376, 1358, 252, 2025, 2516, 2194, 2079, 1663, 1210, 1764, 2668, 1550, 1385, 1532, 1855, 0, 1727, 642, 1952, 875],
[1643, 1723, 647, 1475, 298, 789, 467, 352, 2646, 517, 325, 1085, 617, 2368, 195, 416, 1727, 0, 1231, 465, 1858],
[2874, 492, 716, 778, 1529, 2020, 1698, 1583, 2189, 714, 1268, 2172, 1054, 1911, 1036, 1359, 642, 1231, 0, 1456, 1401],
[1418, 1948, 872, 1700, 763, 682, 360, 127, 3111, 742, 790, 1550, 1082, 2833, 558, 881, 1952, 465, 1456, 0, 2323],
[2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323, 0]]

import sys

def nearest_neighbor_algorithm(cost_matrix, start_node):
    n = len(cost_matrix)
    visited = [False] * n
    path = [start_node]
    total_distance = 0

    for _ in range(n - 1):
        current_node = path[-1]
        min_distance = sys.maxsize
        next_node = -1

        for neighbor in range(n):
            if not visited[neighbor] and cost_matrix[current_node][neighbor] < min_distance:
                min_distance = cost_matrix[current_node][neighbor]
                next_node = neighbor

        path.append(next_node)
        total_distance += min_distance
        visited[next_node] = True

    total_distance += cost_matrix[path[-1]][start_node]
    path.append(start_node)

    path.remove(start_node)
    return path, total_distance

start_node = 20
optimal_path, optimal_distance = nearest_neighbor_algorithm(n2, start_node)

optimal_path1 = []
for x in optimal_path:
    y = 'n'
    y += str(x)
    optimal_path1.append(y)

for z in range(len(optimal_path1)):
    if(optimal_path1[z] == 'n20'):
        optimal_path1[z] = 'r0' 

print(f"The optimal path is {optimal_path1}.")
print(f"The optimal distance is {optimal_distance}.")

'''import json
result_dict = {"v0": {"path": optimal_path1}}

result_json = json.dumps(result_dict, indent=2)

with open("level0_output.json", "w") as json_file:
    json_file.write(result_json)'''

# Level 1A
print("----------------------------------------")
print("Level 1A")
print("----------------------------------------")

import json
from python_tsp.heuristics import solve_tsp_local_search, solve_tsp_simulated_annealing

'''data = {
    "neighbourhoods": {
        "n0": {"order_quantity": 70, "distances": [0, 2953, 1170, 1677, 1318, 2055, 591, 3050, 2626, 1864, 277, 2499, 769, 1463, 2006, 2516, 2394, 997, 1099, 421, 797]},
        "n1": {"order_quantity": 70, "distances": [2953, 0, 1783, 1276, 1635, 898, 2458, 97, 423, 1089, 3026, 664, 2280, 1600, 1057, 535, 559, 2182, 2208, 2532, 2156]},
        "n2": {"order_quantity": 90, "distances": [1170, 1783, 0, 507, 148, 885, 675, 1880, 1456, 694, 1447, 1697, 497, 2633, 2090, 1346, 1224, 2167, 2269, 953, 563]},
        "n3": {"order_quantity": 50, "distances": [1677, 1276, 507, 0, 359, 752, 1182, 1373, 1325, 187, 1750, 1566, 1004, 2502, 1959, 839, 717, 2036, 2138, 1256, 880]},
        "n4": {"order_quantity": 70, "distances": [1318, 1635, 148, 359, 0, 737, 823, 1732, 1310, 546, 1391, 1551, 645, 2487, 1944, 1198, 1076, 2021, 2123, 897, 521]},
        "n5": {"order_quantity": 90, "distances": [2055, 898, 885, 752, 737, 0, 1560, 995, 573, 939, 2128, 814, 1382, 1750, 1207, 461, 339, 1284, 1386, 1634, 1258]},
        "n6": {"order_quantity": 110, "distances": [591, 2458, 675, 1182, 823, 1560, 0, 2555, 2131, 1369, 868, 2004, 178, 2054, 1511, 2021, 1899, 1588, 1690, 374, 302]},
        "n7": {"order_quantity": 70, "distances": [3050, 97, 1880, 1373, 1732, 995, 2555, 0, 424, 1186, 3123, 665, 2377, 1601, 1058, 534, 656, 2279, 2305, 2629, 2253]},
        "n8": {"order_quantity": 110, "distances": [2626, 423, 1456, 1325, 1310, 573, 2131, 424, 0, 1512, 2699, 241, 1953, 1177, 634, 958, 608, 1855, 1881, 2205, 1829]},
        "n9": {"order_quantity": 70, "distances": [1864, 1089, 694, 187, 546, 939, 1369, 1186, 1512, 0, 1937, 1753, 1191, 2689, 2146, 652, 904, 2223, 2325, 1443, 1067]},
        "n10": {"order_quantity": 70, "distances": [277, 3026, 1447, 1750, 1391, 2128, 868, 3123, 2699, 1937, 0, 2572, 1046, 1536, 2079, 2589, 2467, 844, 822, 494, 884]},
        "n11": {"order_quantity": 110, "distances": [2499, 664, 1697, 1566, 1551, 814, 2004, 665, 241, 1753, 2572, 0, 1826, 1036, 493, 1199, 849, 1728, 1754, 2078, 1702]},
        "n12": {"order_quantity": 110, "distances": [769, 2280, 497, 1004, 645, 1382, 178, 2377, 1953, 1191, 1046, 1826, 0, 2232, 1689, 1843, 1721, 1766, 1868, 552, 162]},
        "n13": {"order_quantity": 90, "distances": [1463, 1600, 2633, 2502, 2487, 1750, 2054, 1601, 1177, 2689, 1536, 1036, 2232, 0, 543, 2135, 1785, 692, 718, 1680, 2070]},
        "n14": {"order_quantity": 50, "distances": [2006, 1057, 2090, 1959, 1944, 1207, 1511, 1058, 634, 2146, 2079, 493, 1689, 543, 0, 1592, 1242, 1235, 1261, 1585, 1527]},
        "n15": {"order_quantity": 90, "distances": [2516, 535, 1346, 839, 1198, 461, 2021, 534, 958, 652, 2589, 1199, 1843, 2135, 1592, 0, 350, 1745, 1771, 2095, 1719]},
        "n16": {"order_quantity": 70, "distances": [2394, 559, 1224, 717, 1076, 339, 1899, 656, 608, 904, 2467, 849, 1721, 1785, 1242, 350, 0, 1623, 1649, 1973, 1597]},
        "n17": {"order_quantity": 110, "distances": [997, 2182, 2167, 2036, 2021, 1284, 1588, 2279, 1855, 2223, 844, 1728, 1766, 692, 1235, 1745, 1623, 0, 102, 1214, 1604]},
        "n18": {"order_quantity": 90, "distances": [1099, 2208, 2269, 2138, 2123, 1386, 1690, 2305, 1881, 2325, 822, 1754, 1868, 718, 1261, 1771, 1649, 102, 0, 1316, 1706]},
        "n19": {"order_quantity": 70, "distances": [421, 2532, 953, 1256, 897, 1634, 374, 2629, 2205, 1443, 494, 2078, 552, 1680, 1585, 2095, 1973, 1214, 1316, 0, 390]}
    },
    "restaurants": {"r0": {"neighbourhood_distance": [797, 2156, 563, 880, 521, 1258, 302, 2253, 1829, 1067, 884, 1702, 162, 2070, 1527, 1719, 1597, 1604, 1706, 390, 0]}},
    "vehicles": {"v0": {"capacity": 600}}
}'''

data = json.load('level1a.json')
print(data)

'''def delivery_algorithm(data):
    neighborhoods = data['neighbourhoods']
    capacity = data['vehicles']['v0']['capacity']

    remaining_neighborhoods = list(neighborhoods.keys())[1:]
    vehicle_paths = {"v0": {}}
    current_capacity = 0
    current_path = ['r0']

    for neighborhood in remaining_neighborhoods:
        if current_capacity + neighborhoods[neighborhood]['order_quantity'] <= capacity:
            current_capacity += neighborhoods[neighborhood]['order_quantity']
            current_path.append(neighborhood)
        else:
            current_path.append('r0')
            vehicle_paths["v0"]["path" + str(len(vehicle_paths["v0"]) + 1)] = current_path
            current_capacity = neighborhoods[neighborhood]['order_quantity']
            current_path = ['r0', neighborhood]
    current_path.append('r0')
    vehicle_paths["v0"]["path" + str(len(vehicle_paths["v0"]) + 1)] = current_path
    return vehicle_paths

result = delivery_algorithm(data)
print(result)

output_file_path = 'level1a_output.json'
with open(output_file_path, 'w') as output_file:
    json.dump(result, output_file, indent=2)'''


# Level 1B
print("----------------------------------------")
print("Level 1B")
print("----------------------------------------")



