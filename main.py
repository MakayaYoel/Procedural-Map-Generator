import random
import copy

def generate_noise_map(width: int, height: int, fill_percentage: int) -> list:
    grid = []

    for i in range(height):
        grid.append([])
        for j in range(width):
            # Generate wall (1)
            if random.randint(1, 100) <= fill_percentage:
                grid[i].append(1)
            else:
                # Generate floor (0)
                grid[i].append(0)
    
    return grid



def add_cellular_automata(grid: list, iterations: int):
    current_iter = 0

    while current_iter < iterations:
        temp_grid = copy.deepcopy(grid)
        y = 0
        x = 0

        while y < height(grid):
            while x < width(grid):
                neighbour_count = get_neighbour_count(x, y, temp_grid)

                if neighbour_count > 4:
                    grid[y][x] = 1
                else:
                    grid[y][x] = 0

                x += 1
            x = 0
            y += 1
        
        current_iter += 1
    
    return grid

def height(grid) :
    return len(grid)

def width(grid) :
    return len(grid[0])

def get_neighbour_count(pos_x: int, pos_y:int, grid:list) -> int:
    count = 0

    for y in range(pos_y - 1, pos_y + 2):
        for x in range(pos_x - 1, pos_x + 2):
            if y >= 0 and y < height(grid) and x >= 0 and x < width(grid):
                if(y != pos_y or x != pos_x):
                    count += grid[y][x]
            else:
                count += 1
    
    return count

def print_grid(agrid):
    for row in agrid:
        actual_row = ""
        for i in row:
            if i == 1:
                actual_row += "#"
            else:
                actual_row += " "

        print(actual_row)

noise_grid = generate_noise_map(100, 25, 60)

while True:
    iterations = int(input("\nNext Amount of Iterations: "))
    acopy = copy.deepcopy(noise_grid)
    automata_grid = add_cellular_automata(acopy, iterations)
    print("\nNOISE:")
    print_grid(noise_grid)
    print("\nAUTOMATA:")
    print_grid(automata_grid)