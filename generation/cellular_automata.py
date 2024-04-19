import copy
from generation import map_utils

def apply_cellular_automata(noise_map: list, iterations: int):
    for _ in range(iterations):
        temp_grid = copy.deepcopy(noise_map)

        for y in range(map_utils.map_height(noise_map)):
            for x in range(map_utils.map_width(noise_map)):
                neighbour_count = get_neighbour_count(x, y, temp_grid)

                if neighbour_count > 4:
                    noise_map[y][x] = map_utils.TILE_WALL
                else:
                    noise_map[y][x] = map_utils.TILE_FLOOR
        

    return noise_map


def get_neighbour_count(x: int, y: int, map: list) -> int:
    count = 0

    # Get surrounding neighbours.
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            # Check for valid index.
            if i >= 0 and i < map_utils.map_height(map) and j >= 0 and j < map_utils.map_width(map):
                # Check if we're currently not on the sent x and y tile
                if i != y or j != x:
                    if map[i][j] == map_utils.TILE_WALL:
                        count += 1
            else:
                count += 1

    return count