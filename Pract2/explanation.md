1. **Importing `PriorityQueue`**: The code imports the `PriorityQueue` class from the `queue` module. A priority queue is used to store and retrieve elements based on their priority.

2. **Defining the Goal State**: The variable `GOAL_STATE` is defined as a 2D list representing the desired arrangement of tiles in the 8-puzzle. In this case, it represents the puzzle solved.

3. **`calculate_distance` Function**: This function calculates the Manhattan distance heuristic for a given state. It iterates over each tile in the puzzle, computing the Manhattan distance of each tile from its goal position and summing them up.

4. **`get_possible_moves` Function**: This function returns a list of possible moves that can be made from a given state. It identifies the position of the blank tile (represented by 0) and checks the neighboring positions to determine valid moves.

5. **`perform_move` Function**: This function applies a move to a given state. It takes the current state and a move as input, swaps the position of the blank tile with the tile in the specified direction, and returns the new state.

6. **`a_star_search` Function**: This is the implementation of the A* search algorithm. It takes an initial state as input and performs the search to find a solution. It uses a priority queue to prioritize states based on their Manhattan distance heuristic. It iteratively explores states, expanding them by applying valid moves until the goal state is reached or all states are explored.

7. **Main Logic**: The code defines an initial state for the 8-puzzle and calls the `a_star_search` function to find a solution. If a solution is found, it prints the steps required to reach the goal state. Otherwise, it prints a message indicating that no solution was found.