from Lines import lines_and_distances

class neighbours_general:

    def get_neighbours(station) -> list:
        """get all neighbours from a station"""
        neighbours = []
        for i in range(1, 15):
            station_n = str("E" + str(i))
            if lines_and_distances.get_real_distance(station, station_n) != -1:
                neighbours.append(station_n)
        return neighbours


    def get_inline_order_neighbours(actual_station, final_station, lines, actual_line_color, first_time) -> list:
        """calculate the cost function for all neighbours and return then in order"""
        neighbours = neighbours_general.get_neighbours(actual_station)

        neighbours_inline_dist = [(lines_and_distances.get_inline_distance(dist, final_station) * 2) +
                                  (lines_and_distances.get_real_distance(actual_station, dist) * 2) +
                                  (0 if not first_time and actual_station in lines[actual_line_color] else 4)
                                  for dist in neighbours]  # multiplier 2 is km/h -> min
        neighbours_zip = zip(neighbours, neighbours_inline_dist)
        neighbours_zip = sorted(neighbours_zip, key=lambda x: x[1])
        return neighbours_zip

