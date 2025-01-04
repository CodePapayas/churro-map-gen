def process_grid(grid):
    """
    Processes the grid and prints it with color coding based on the terrain types.

    Args:
        grid (list[list[int]]): 2D grid of integers representing terrain types.
    """
    def color_tile(value):
        """
        Maps a terrain type to its corresponding color for display.

        Args:
            value (int): Terrain type value.

        Returns:
            str: Colored representation of the tile using ANSI escape codes.
        """
        # Using 256-color code for beige ground:
        # \033[38;5;187m can appear as a light tan/beige on many terminals.
        color_map = {
            0: "\033[38;5;187m",  # Beige for Ground
            1: "\033[1;36m",      # Bold Cyan for River
            2: "\033[1;34m",      # Bold Blue for Lake
            3: "\033[90m",        # Dark Gray for Mountain
            4: "\033[92m",        # Light Green for Forest
            5: "\033[33m",        # Yellow/Brown for Bridge
        }
        reset = "\033[0m"
        return f"{color_map.get(value, reset)}{value}{reset}"

    for row in grid:
        print(" ".join(color_tile(tile) for tile in row))


def print_key():
    """
    Prints the key legend for the grid with color-coded terrain types.
    """
    print("\nGrid Key:")
    print("\033[38;5;187m0: Ground (Beige)\033[0m")
    print("\033[1;36m1: River\033[0m")
    print("\033[1;34m2: Lake\033[0m")
    print("\033[90m3: Mountain\033[0m")
    print("\033[92m4: Forest\033[0m")
    print("\033[33m5: Bridge\033[0m")
