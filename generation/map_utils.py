TILE_FLOOR = 0
TILE_FLOOR_CHAR = " "

TILE_WALL = 1
TILE_WALL_CHAR = "#"

def map_height(map: list) -> int:
    return len(map)

def map_width(map: list) -> int:
    return len(map[0])

def print_map(map: list):
    for y in range(map_height(map)):
        row = ""
        for x in range(map_width(map)):
            if map[y][x] == TILE_WALL:
                row += TILE_WALL_CHAR
            else:
                row += TILE_FLOOR_CHAR
        print(row)