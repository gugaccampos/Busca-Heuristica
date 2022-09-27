
inline_distance = [  # Tabela 1 - Distância em linha reta
    [10, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29.8],
    [8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10, 3.5, 15.5, 20.9, 19.1, 21.8],
    [6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6],
    [12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4],
    [3, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9],
    [3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2],
    [20, 23, 27.3, 34.2, 25.7, 12.4, 15.6],
    [8.2, 20.3, 16.1, 6.4, 22.7, 27.6],
    [13.5, 11.2, 10.9, 21.2, 26.6],
    [17.6, 24.2, 18.7, 21.2],
    [14.2, 31.5, 35.5],
    [28.8, 33.6],
    [5.1]
]

real_distances = {  # Tabela 2 -  Distância real
    "E1:E2": 10,
    "E2:E3": 8.5,
    "E2:E9": 10,
    "E2:E10": 3.5,
    "E3:E4": 6.3,
    "E3:E9": 9.4,
    "E3:E13": 18.7,
    "E4:E5": 13,
    "E4:E8": 15.3,
    "E4:E13": 12.8,
    "E5:E6": 3,
    "E5:E7": 2.4,
    "E5:E8": 30,
    "E8:E9": 9.6,
    "E8:E12": 6.4,
    "E9:E11": 12.2,
    "E13:E14": 5.1
}

class lines_and_distances:

    # Função que pega a distância real entre duas estações.
    def get_real_distance(station_a, station_b) -> float:
        """to get the real distance in km from one station to the other"""
        num1 = int(station_a[1:]) - 1
        num2 = int(station_b[1:]) - 1
        try:
            value = round(real_distances[str(station_a + ":" + station_b)], 1) if num1 < num2 else\
            round(real_distances[str(station_b + ":" + station_a)], 1)
        except:
            value = -1
        return value

    # Função que pega a distância em linha entre a fronteira e a estação final.
    def get_inline_distance(station_a, station_b) -> float:
        """inline distance"""
        num1 = int(station_a[1:]) - 1
        num2 = int(station_b[1:]) - 1
        value = -1
        try:
            if num1 < num2:
                value = round(inline_distance[num1][num2 - num1 - 1], 1)
            elif num1 > num2:
                value = round(inline_distance[num2][num1 - num2 - 1], 1)
            else:
                value = 0
        except:
            value = -1
        return value