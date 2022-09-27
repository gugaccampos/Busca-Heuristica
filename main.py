from tokenize import String
from Lines import lines_and_distances
from Neighbours import neighbours_general

lines = {  # Dicionário para representar a qual linha as estações pertencem
    "red line": ["E11", "E9", "E3", "E13"],
    "blue line": ["E1", "E2", "E3", "E4", "E5", "E6"],
    "green line": ["E12", "E8", "E4", "E13", "E14"],
    "yellow line": ["E10", "E2", "E9", "E8", "E5", "E7"]
}

actual_line_color = ''
first_time = True

class general_frontiers:
    # Descobrir qual a linha em que as duas estações se conectam
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

    # Função geral dos cálculos
    def frontier(start, destination):
        global actual_line_color
        global first_time
        is_ch_lines = 0

        # Veririca se chegou ao destino
        if (start == destination):
            return 1

        # Verifica qual a linha da estação atual
        color = general_frontiers.color_from_frontier(stations_dic_dir[start], start)
        if color != actual_line_color and color != None:
            actual_line_color = color

        # Recebe a distância heurística dos vizinhos
        neighbours = neighbours_general.get_inline_order_neighbours(start, destination, lines, actual_line_color, first_time)  # all neighbours

        order_neighbours = [i[0] for i in neighbours] #Ordena os vizinhos

        # Verifica quais vizinhos são elegíveis
        for i in neighbours:
            if not first_time: # Garante que não há uma linha definida para os primeiros vizinhos
                if i[0] in lines[actual_line_color]:
                    is_ch_lines = 0
                else:
                    is_ch_lines = 4

            # Pega a distância real da estação atual e seus vizinhos
            new_value = round((lines_and_distances.get_real_distance(start, i[0]) * 2 + is_ch_lines + stations_dic_real_distance[start]), 1)
            
            # Verifica quais vizinhos são elegíveis a partir do ponto inicial
            if new_value < stations_dic_real_distance[i[0]]:
                stations_dic_real_distance[i[0]] = new_value
                stations_dic_line_distance[i[0]] = i[1]
                stations_dic_visted[i[0]] = True
                stations_dic_dir[i[0]] = start
            else:
                order_neighbours.remove(i[0])

        stations_dic_visted[start] = False
        first_time = False

        stations = {key: value for key, value in stations_dic_visted.items() if value == True}  # Vizinhos visitados
        station_heuristic = [(i, stations_dic_line_distance[i]) for i in stations]  # Custo heurísticos das estações
        station_real = [(i, stations_dic_real_distance[i]) for i in stations] # Custo real das estações
        min_value = (sorted(station_heuristic, key=lambda x: x[1]))[0]  # Vizinho com custo heurístico mínimo

        print(f'Estamos em {start}')
        print("Distâncias fronteira real:")
        print(station_real)
        print('Distâncias fronteira eurística:')
        print(station_heuristic, '\n')

        general_frontiers.frontier(min_value[0], destination)  # Visita o vizinho com custo mínimo


# Função principal
def call_function(start, destination):
    global stations_dic_real_distance

    # Dicionário para armazenas as distâncias reais
    stations_dic_real_distance = {"E1": 99999, "E2": 99999, "E3": 99999, "E4": 99999, "E5": 99999, "E6": 99999, "E7": 99999,
                    "E8": 99999, "E9": 99999,
                    "E10": 99999, "E11": 99999, "E12": 99999, "E13": 99999, "E14": 99999}

    global stations_dic_line_distance

    # Dicionário para armazenar as distâncias heurísticas
    stations_dic_line_distance = {"E1": 99999, "E2": 99999, "E3": 99999, "E4": 99999, "E5": 99999, "E6": 99999,
                                  "E7": 99999,
                                  "E8": 99999, "E9": 99999,
                                  "E10": 99999, "E11": 99999, "E12": 99999, "E13": 99999, "E14": 99999}

    global stations_dic_dir

    # Dicionário para armazenar as fronteiras que levaram até uma determinada estação
    stations_dic_dir = {"E1": "", "E2": "", "E3": "", "E4": "", "E5": "", "E6": "", "E7": "", "E8": "", "E9": "",
                        "E10": "", "E11": "", "E12": "", "E13": "", "E14": ""}

    global stations_dic_visted

    # Dicionário para armazenar quais estações foram ou não visitadas
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

    # Chamando função para iniciar os cálculos
    general_frontiers.frontier(start, destination)

    print(f'Chegamos em {destination}')
    print(f"custo: {stations_dic_real_distance[destination]}")
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