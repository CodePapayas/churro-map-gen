import random
from app import process_neighbor
from grid_printer import process_grid, print_key

def gridMaker(cols, rows):
    """
    Generates a grid of specified dimensions with randomized terrain types and processes neighboring tiles.

    Args:
        cols (int): The number of columns in the grid.
        rows (int): The number of rows in the grid.

    Returns:
        list[list[int]]: A 2D grid with terrain types assigned to each tile.
    """
    tile_type = [
        0,  # Land
        1,  # River
        2,  # Lake
        3,  # Mountain
        4,  # Forest
        5   # Bridge
    ]

    # Initialize the grid with default terrain type (0 - Land)
    arr = [[0 for i in range(cols)] for j in range(rows)]

    # Start with a random terrain type at the center of the grid
    x_center = cols // 2
    y_center = rows // 2
    arr[y_center][x_center] = random.choice(tile_type)

    # Generate a list of all coordinates and shuffle them
    coords = [(x, y) for y in range(rows) for x in range(cols)]
    random.shuffle(coords)

    # Process each tile and its neighbors
    for x, y in coords:
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        for dy, dx in directions:
            # Calculate neighbor coordinates
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < rows and 0 <= new_x < cols:
                process_neighbor(arr, y, x, new_y, new_x)

    return arr

# Create and process a 15x15 grid
grid = gridMaker(15, 15)
process_grid(grid)
print_key()
