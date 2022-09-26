from tokenize import String
from Lines import lines_and_distances
from Neighbours import neighbours_general

lines = {  # to discovery line changes
    "red line": ["E11", "E9", "E3", "E13"],
    "blue line": ["E1", "E2", "E3", "E4", "E5", "E6"],
    "green line": ["E12", "E8", "E4", "E13", "E14"],
    "yellow line": ["E10", "E2", "E9", "E8", "E5", "E7"]
}

actual_line_color = ''
first_time = True

class general_frontiers:
    # what_color_connect_this_lines
    def color_from_frontier(station_a, station_b):
        is_a_red = station_a in lines['red line']
        is_a_blue = station_a in lines['blue line']
        is_a_green = station_a in lines['green line']
        is_a_yellow = station_a in lines['yellow line']
        is_b_red = station_b in lines['red line']
        is_b_blue = station_b in lines['blue line']
        is_b_green = station_b in lines['green line']
        is_b_yellow = station_b in lines['yellow line']

        if is_a_red and is_b_red:
            return "red line"
        elif is_a_blue and is_b_blue:
            return "blue line"
        elif is_a_green and is_b_green:
            return "green line"
        elif is_a_yellow and is_b_yellow:
            return "yellow line"

    def frontier(start, destination):
        global actual_line_color
        global first_time
        is_ch_lines = 0

        if (start == destination):
            return 1

        color = general_frontiers.color_from_frontier(stations_dic_dir[start], start)
        if color != actual_line_color and color != None:
            actual_line_color = color

        nei = neighbours_general.get_inline_order_neighbours(start, destination, lines, actual_line_color, first_time)  # all neighbours

        order_nei = [i[0] for i in nei]  # the nest process is to have only the eligible neighbours:
        for i in nei:
            if not first_time:
                if i[0] in lines[actual_line_color]:
                    is_ch_lines = 0
                else:
                    is_ch_lines = 4
            new_value = lines_and_distances.get_real_distance(start, i[0]) * 2 + is_ch_lines + stations_dic_real_distance[start]
            # which neighbours are an option comming from 'start'?
            if new_value < stations_dic_real_distance[i[0]]:
                stations_dic_real_distance[i[0]] = new_value
                stations_dic_line_distance[i[0]] = i[1]
                stations_dic_visted[i[0]] = True
                stations_dic_dir[i[0]] = start
            else:
                order_nei.remove(i[0])

        stations_dic_visted[start] = False
        first_time = False

        st = {key: value for key, value in stations_dic_visted.items() if value == True}  # places i've not visited yet
        st2 = [(i, stations_dic_line_distance[i]) for i in st]  # those places cost
        min_value = (sorted(st2, key=lambda x: x[1]))[0]  # the min cost

        print(f'Estamos em {start}')
        print("fronteira atual:")
        print(st2, '\n')

        general_frontiers.frontier(min_value[0], destination)  # go to that min cost place

def call_function(start, destination):
    global stations_dic_real_distance
    stations_dic_real_distance = {"E1": 99999, "E2": 99999, "E3": 99999, "E4": 99999, "E5": 99999, "E6": 99999, "E7": 99999,
                    "E8": 99999, "E9": 99999,
                    "E10": 99999, "E11": 99999, "E12": 99999, "E13": 99999, "E14": 99999}

    global stations_dic_line_distance
    stations_dic_line_distance = {"E1": 99999, "E2": 99999, "E3": 99999, "E4": 99999, "E5": 99999, "E6": 99999,
                                  "E7": 99999,
                                  "E8": 99999, "E9": 99999,
                                  "E10": 99999, "E11": 99999, "E12": 99999, "E13": 99999, "E14": 99999}

    global stations_dic_dir
    stations_dic_dir = {"E1": "", "E2": "", "E3": "", "E4": "", "E5": "", "E6": "", "E7": "", "E8": "", "E9": "",
                        "E10": "", "E11": "", "E12": "", "E13": "", "E14": ""}

    global stations_dic_visted
    stations_dic_visted = {"E1": False, "E2": False, "E3": False, "E4": False, "E5": False, "E6": False,
                           "E7": False,
                           "E8": False, "E9": False,
                           "E10": False, "E11": False, "E12": False, "E13": False, "E14": False}
    global route
    route = []

    print('\n'"===========================================================")
    print(f"teste do {start} até o {destination}")
    stations_dic_real_distance[start] = 0
    stations_dic_line_distance[start] = 0
    stations_dic_visted[start] = True

    general_frontiers.frontier(start, destination)

    print(f'Chegamos em {destination}')
    print(f"custo: {stations_dic_real_distance[destination]:.1f}")
    print("rota final:")
    way = destination  # do you know the way
    while way != start:
        way = stations_dic_dir[way]
        route.append(way)
    route.reverse()
    route.append(destination)
    print(route)
    print("==========================================================="'\n')


cord1 = input()
cord2 = input()

call_function(cord1, cord2)

