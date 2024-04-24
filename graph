class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_max_degree(self):
        return max(len(adj_list) for adj_list in self.graph)

    def is_safe(self, v, color, colored):
        for i in self.graph[v]:
            if colored[i] == color:
                return False
        return True

    def graph_coloring_util(self, colors, colored, v):
        if v == self.vertices:
            return True

        for color in colors:
            if self.is_safe(v, color, colored):
                colored[v] = color
                if self.graph_coloring_util(colors, colored, v + 1):
                    return True
                colored[v] = None

    def graph_coloring(self):
        max_degree = self.get_max_degree()
        num_colors = min(max_degree + 1, 7)  # Use all 7 colors of the rainbow if possible
        colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
        colored = [None] * self.vertices
        if not self.graph_coloring_util(colors[:num_colors], colored, 0):
            print("Solution does not exist")
            return False

        used_colors = set(colored)
        print("Colors used:", used_colors)

        print("Solution exists and the coloring is as follows:")
        for i in range(self.vertices):
            print("State", i, "is colored with", colored[i])
        return True

# Taking user input for the number of states
num_states = int(input("Enter the number of states: "))
australia_map = Graph(num_states)

# Taking user input for the number of edges
num_edges = int(input("Enter the number of edges: "))
print("Enter the edges (separated by space):")
for _ in range(num_edges):
    u, v = map(int, input().split())
    australia_map.add_edge(u, v)

australia_map.graph_coloring()
