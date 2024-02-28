from queue import PriorityQueue

GOAL_STATE = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

def calculate_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_i, goal_j = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def get_possible_moves(state):
    i, j = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)
    possible_moves = []
    if i > 0:
        possible_moves.append((i - 1, j))
    if i < 2:
        possible_moves.append((i + 1, j))
    if j > 0:
        possible_moves.append((i, j - 1))
    if j < 2:
        possible_moves.append((i, j + 1))
    return possible_moves

def perform_move(state, move):
    i, j = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)
    new_state = [row[:] for row in state]
    new_i, new_j = move
    new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
    return new_state

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    explored = set()

    while not frontier.empty():
        _, current_state = frontier.get()
        if current_state == GOAL_STATE:
            return current_state
        
        explored.add(tuple(map(tuple, current_state)))

        for move in get_possible_moves(current_state):
            new_state = perform_move(current_state, move)
            if tuple(map(tuple, new_state)) not in explored:
                priority = calculate_distance(new_state)
                frontier.put((priority, new_state))

    return None

initial_state = [
    [1, 2, 6],
    [7, 0, 4],
    [8, 3, 5]
]

result = a_star_search(initial_state)
if result:
    print("Solution found!")
    for row in result:
        print(row)
else:
    print("No solution found.")