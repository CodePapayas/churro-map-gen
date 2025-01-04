import random
from app import process_neighbor
from grid_printer import process_grid, print_key

def gridMaker(cols, rows):
	tile_type = [0, # Land
		     1, # River
		     2, # Lake
		     3, # Mountain
		     4, # Forest
		     5] # Bridge

	arr = [[0 for i in range(cols)] for j in range(rows)]
	x_center = cols // 2
	y_center = rows // 2
	arr[y_center][x_center] = random.choice(tile_type)
	
	coords = [(x, y) for y in range(rows) for x in range(cols)]
	random.shuffle(coords)

	for x, y in coords:
		directions = [(-1, 0), # Up
			      (1,0),   # Down
			      (0, -1), # Left
			      (0, 1)]  # Right
		
		for dy, dx in directions:
			#Calculate neighbors coords
			new_y, new_x = y + dy, x + dx
			if 0 <= new_y < rows and 0 <= new_x < cols:
				process_neighbor(arr, y, x, new_y, new_x)

	return arr


grid = gridMaker(15, 15)
process_grid(grid)
print_key()