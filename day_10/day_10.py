'''
looks like its a bfs soln to get steps

lets iterate through the grid
connect pipes based upon their neighbours

    -   | is a vertical pipe connecting north and south.
        -> connect (r + 1, c) to (r, c) right to this
        -> connect (r - 1, c) to (r, c) left to this
    -   - is a horizontal pipe connecting east and west.
        -> connect (r, c - 1) to (r, c) top to this
        -> connected (r, c + 1) to (r, c) bottom to this
    -   L is a 90-degree bend connecting north and east.
        -> connect (r - 1, c) to (r, c) top to this
        -> connected (r, c + 1) to (r, c) connect right to this 
    -   J is a 90-degree bend connecting north and west.
        -> connect (r - 1, c) top to this 
        -> connect (r, c - 1) left to this 
    -   7 is a 90-degree bend connecting south and west.
        -> connect (r - 1, c) left to this
        -> connect (r, c + 1) bottom to this
    -   F is a 90-degree bend connecting south and east.
        -> connect (r + 1, c) to (r, c) right to this
        -> connected (r, c + 1) to (r, c) bottom to this
    -   . is ground; there is no pipe in this tile.
        -> skip over this 
    -   S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
        -> add this to start


    start at S and then bfs around its valid neighbours, after queue is empty return timestamp

'''
import time
from collections import defaultdict, deque

# Direction dictionaries
direction_dict = {
    'right': (0, 1),
    'left': (0, -1),
    'bottom': (1, 0),
    'top': (-1, 0)
}

reverse_direction_dict = {v: k for k, v in direction_dict.items()}

direction_pipes = {
    '|': ['top', 'bottom'],
    '-': ['left', 'right'],
    'L': ['top', 'right'],
    'J': ['top', 'left'],
    '7': ['left', 'bottom'],
    'F': ['right', 'bottom']
}

# Utility functions
def is_valid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def find_start_connections(grid, start, rows, cols, graph):
    """Find connections for the starting cell."""
    r, c = start
    valid_connections = []
    
    for direction, (dr, dc) in direction_dict.items():
        next_r, next_c = r + dr, c + dc
        if is_valid(next_r, next_c, rows, cols) and grid[next_r][next_c] in direction_pipes:
            if (r, c) in graph[(next_r, next_c)]:
                valid_connections.append((next_r, next_c))
    
    return valid_connections

def bfs(start_indx, graph):
    """Breadth-First Search to compute distances and loop."""
    visited = set([start_indx])
    queue = deque([(start_indx, 0)])
    dists = {}
    max_steps = 0

    while queue:
        current_indx, steps = queue.popleft()
        max_steps = steps
        dists[current_indx] = steps

        for next_pos in graph[current_indx]:
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, steps + 1))
    
    loop = set(dists.keys())
    return max_steps, loop

def build_graph(grid, rows, cols):
    """Build a graph connecting pipes based on neighbors."""
    graph = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            char = grid[r][c]
            if char in direction_pipes:
                for direction in direction_pipes[char]:
                    dr, dc = direction_dict[direction]
                    next_r, next_c = r + dr, c + dc
                    if is_valid(next_r, next_c, rows, cols):
                        graph[(r, c)].append((next_r, next_c))
    return graph

def create_modified_grid(grid, rows, cols, loop, start_indx, valid_connections):
    """Create a modified grid with non-loop cells replaced by '.'."""
    modified_grid = [
        [cell if (r, c) in loop else '.' for c, cell in enumerate(row)]
        for r, row in enumerate(grid)
    ]
    
    start_r, start_c = start_indx

    # Calculate valid start cell directions
    valid_start_cells_directions = [
        reverse_direction_dict[(r - start_r, c - start_c)]
        for r, c in valid_connections
    ]

    # Map directions to pipe characters
    direction_to_char = {
        frozenset(['top', 'bottom']): '|',
        frozenset(['left', 'right']): '-',
        frozenset(['top', 'right']): 'L',
        frozenset(['top', 'left']): 'J',
        frozenset(['left', 'bottom']): '7',
        frozenset(['right', 'bottom']): 'F',
    }
    s_char = direction_to_char.get(frozenset(valid_start_cells_directions), None)

    # Set the start cell character
    modified_grid[start_r][start_c] = s_char

    return modified_grid

def ray_casting(grid, rows, cols):
    """Perform ray casting to count valid cells."""
    def count_inversions(r, c):
        """Count inversions in the row for a specific column."""
        count = 0
        for col in range(c):
            if grid[r][col] == ".":
                continue
            '''
                we don't check F and 7 becauase they do not contribute to a vertical crossing; they represent a horizontal crossing.
            '''
            count += grid[r][col] in {"J", "L", "|"}
        return count

    result = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == ".":
                inversions = count_inversions(r, c)
                if inversions % 2 == 1:
                    result += 1
    return result

# Main functions
def question_one():
    start_time = time.time()
    with open("day_10.txt") as f:
        grid = f.read().splitlines()
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find start position
    start_indx = next(
        ((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'S'),
        None
    )
    if not start_indx:
        print("No start found!")
        return
    
    # Build graph and find BFS result
    graph = build_graph(grid, rows, cols)
    start_connections = find_start_connections(grid, start_indx, rows, cols, graph)
    graph[start_indx] = start_connections
    res, _ = bfs(start_indx, graph)
    print(f"Question 1 Result: {res}")
    print(f"Time Taken: {time.time() - start_time:.4f} seconds")

def question_two():
    start_time = time.time()
    with open("day_10.txt") as f:
        grid = f.read().splitlines()
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Find start position
    start_indx = next(
        ((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'S'),
        None
    )
    if not start_indx:
        print("No start found!")
        return
    
    # Build graph, perform BFS, and modify the grid
    graph = build_graph(grid, rows, cols)
    start_connections = find_start_connections(grid, start_indx, rows, cols, graph)
    graph[start_indx] = start_connections
    _, loop_path = bfs(start_indx, graph)
    modified_grid = create_modified_grid(grid, rows, cols, loop_path, start_indx, start_connections)

    # Perform ray casting
    res = ray_casting(modified_grid, rows, cols)
    print(f"Question 2 Result: {res}")
    print(f"Time Taken: {time.time() - start_time:.4f} seconds")

# Execute questions
question_one()
question_two()