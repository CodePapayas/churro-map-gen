import random

def process_neighbor(grid, y, x, new_y, new_x):
    """
    Processes the neighbor tile of the grid and determines its type based on the current tile and rules.

    Args:
        grid (list[list[int]]): 2D grid representing terrain.
        y (int): Y-coordinate of the current tile.
        x (int): X-coordinate of the current tile.
        new_y (int): Y-coordinate of the neighbor tile.
        new_x (int): X-coordinate of the neighbor tile.
    """
    def is_bridge_nearby(grid, y, x):
        """
        Checks if a bridge exists within a 5x5 area around the given coordinates.

        Args:
            grid (list[list[int]]): 2D grid representing terrain.
            y (int): Y-coordinate to check.
            x (int): X-coordinate to check.

        Returns:
            bool: True if a bridge is nearby, False otherwise.
        """
        rows = len(grid)
        cols = len(grid[0])
        for i in range(max(0, y - 2), min(rows, y + 3)):
            for j in range(max(0, x - 2), min(cols, x + 3)):
                if grid[i][j] == 5:  # If a bridge is found in the 5x5 area
                    return True
        return False

    def is_valid_bridge(grid, y, x):
        """
        Checks if a bridge satisfies the condition of having either both a 1 tile on top and bottom
        or a 1 tile on the left or right, but never both. Additionally, ensures that bridges start
        and end in either land (0) or forest (4) tiles.

        Args:
            grid (list[list[int]]): 2D grid representing terrain.
            y (int): Y-coordinate of the bridge.
            x (int): X-coordinate of the bridge.

        Returns:
            bool: True if the bridge satisfies the condition, False otherwise.
        """
        rows = len(grid)
        cols = len(grid[0])

        has_top_bottom = (y > 0 and grid[y - 1][x] == 1) and (y < rows - 1 and grid[y + 1][x] == 1)
        has_left_right = (x > 0 and grid[y][x - 1] == 1) and (x < cols - 1 and grid[y][x + 1] == 1)

        if has_top_bottom:
            left_valid = (x > 0 and grid[y][x - 1] in [0, 4])
            right_valid = (x < cols - 1 and grid[y][x + 1] in [0, 4])
            return left_valid and right_valid
        elif has_left_right:
            top_valid = (y > 0 and grid[y - 1][x] in [0, 4])
            bottom_valid = (y < rows - 1 and grid[y + 1][x] in [0, 4])
            return top_valid and bottom_valid

        return False

    def ensure_vertical_river(grid, y, x):
        """
        Ensures that rivers spawn in at least lines of 3 vertically.

        Args:
            grid (list[list[int]]): 2D grid representing terrain.
            y (int): Y-coordinate to start the check.
            x (int): X-coordinate to check.
        """
        rows = len(grid)
        if y + 2 < rows:
            if grid[y + 1][x] != 1:
                grid[y + 1][x] = 1
            if grid[y + 2][x] != 1:
                grid[y + 2][x] = 1

    weights = {
        0: [70, 3, 3, 7, 17],  # Land
        1: [85, 15],            # River
        2: [70, 17],            # Lake
        3: [7, 70],             # Mountain
        4: [17, 70, 3]          # Forest
    }

    current_tile = grid[y][x]

    if current_tile == 0:  # Land
        grid[new_y][new_x] = random.choices(
            [0, 1, 2, 3, 4],  # Land, River, Lake, Mountain, Forest
            weights[0]  # Weights
        )[0]
    elif current_tile == 1:  # River
        if new_y > y:  # Ensure the river flows downward
            if not is_bridge_nearby(grid, new_y, new_x):
                grid[new_y][new_x] = random.choices(
                    [1, 5],  # River, Bridge
                    weights[1]  # Weights
                )[0]
                if grid[new_y][new_x] == 1:
                    ensure_vertical_river(grid, new_y, new_x)
                if grid[new_y][new_x] == 5 and not is_valid_bridge(grid, new_y, new_x):
                    grid[new_y][new_x] = 1
            else:
                grid[new_y][new_x] = 1
    elif current_tile == 2:  # Lake
        grid[new_y][new_x] = random.choices(
            [2, 4],  # Lake, Forest
            weights[2]  # Weights
        )[0]
    elif current_tile == 3:  # Mountain
        grid[new_y][new_x] = random.choices(
            [3, 0],  # Mountain, Land
            weights[3]  # Weights
        )[0]
    elif current_tile == 4:  # Forest
        grid[new_y][new_x] = random.choices(
            [4, 0, 1],  # Forest, Land, River
            weights[4]  # Weights
        )[0]
