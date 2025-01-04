# Terrain Generation README

## Overview
This project provides a procedural terrain generation system for creating 2D maps. The map consists of five terrain types: land, river, lake, mountain, and forest. The terrain generation is guided by specific rules and weighted probabilities to ensure logical and diverse layouts.

## Key Features
- **Weighted Terrain Expansion:** Uses predefined weights to control the probability of each terrain type appearing.
- **Rivers:** Rivers flow vertically with a guaranteed minimum length of 3 tiles. Bridges may spawn, adhering to strict placement rules.
- **Bridges:** Bridges connect river tiles and must terminate in land or forest tiles. They follow specific proximity rules.
- **Dynamic Rules:** Custom rules ensure realistic transitions and expansions for each terrain type.

## Terrain Types
| Tile Type | Numeric Code | Description |
|-----------|--------------|-------------|
| Land      | 0            | Base terrain with a high chance of expanding to other types. |
| River     | 1            | Flows vertically and may include bridges. |
| Lake      | 2            | Expands in isolated clusters and may transition to forest. |
| Mountain  | 3            | Peaks that prioritize clustering but can transition to land. |
| Forest    | 4            | Grows near land and lakes, with occasional transitions to rivers. |
| Bridge    | 5            | Spawns on rivers under strict conditions. |

## Weight Configuration
The terrain weights are stored in a dictionary for easy modification:

```python
weights = {
    0: [70, 3, 3, 7, 17],  # Land
    1: [85, 15],            # River
    2: [70, 17],            # Lake
    3: [7, 70],             # Mountain
    4: [17, 70, 3]          # Forest
}
```

### Explanation of Weights
- **Land:** Dominates map generation, with a slight chance of transitioning to rivers, lakes, mountains, or forests.
- **River:** Rivers have a high probability of expanding vertically, with occasional bridges.
- **Lake:** Lakes form clusters with some forest expansion.
- **Mountain:** Mountains prefer self-expansion, with occasional transitions to land.
- **Forest:** Forests grow near land or lakes and may transition to rivers sparingly.

## Functions and Logic

### `process_neighbor`
Handles the assignment of terrain types to neighboring tiles.
- Inputs: Current grid, coordinates of the current and neighboring tiles.
- Outputs: Updates the neighboring tile based on weighted probabilities and terrain rules.

### `is_bridge_nearby`
Checks for the presence of bridges within a 5x5 area.
- Inputs: Grid and coordinates to check.
- Outputs: Boolean indicating if a bridge is nearby.

### `is_valid_bridge`
Validates the placement of bridges.
- Ensures bridges connect only river tiles and terminate on land or forest tiles.
- Prevents bridges from spanning rivers horizontally and vertically simultaneously.

### `ensure_vertical_river`
Guarantees rivers extend vertically for at least 3 tiles.
- Inputs: Grid and starting coordinates.
- Outputs: Updates the grid to ensure vertical continuity.

## How to Use
1. **Initialization:** Create a 2D grid initialized with base terrain.
2. **Processing:** Call `process_neighbor` for each tile to populate the map.
3. **Customization:** Adjust weights in the `weights` dictionary to modify terrain probabilities.
4. **Rendering:** Use the generated grid to render the map visually.

## Example
```python
# Example of initializing a grid and processing neighbors
grid = [[0 for _ in range(10)] for _ in range(10)]
process_neighbor(grid, 0, 0, 0, 1)
process_neighbor(grid, 0, 1, 0, 2)
```

## Future Improvements
- Enhanced biome rules to create region-specific terrains.
- Integration with graphical assets for real-time rendering.
- Optimization for larger map sizes.

## Contribution
Feel free to fork this project and contribute improvements via pull requests. Suggestions and feedback are always welcome!

---
Thank you for using the terrain generation system. Happy mapping!

