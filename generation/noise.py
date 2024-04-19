import random
from generation import map_utils

def generate_noise_map(width: int, height: int, fill_percentage: int) -> list:
    noise_map = []

    for y in range(height):
        noise_map.append([])
        for x in range(width):
            # Generate wall if random number <= fill_percentage
            if random.randint(1, 100) <= fill_percentage:
                noise_map[y].append(map_utils.TILE_WALL)
            else:
                # Generate floor if random number > fill_percentage
                noise_map[y].append(map_utils.TILE_FLOOR)
    
    return noise_map