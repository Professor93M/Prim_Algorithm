from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        visited = set()
        mst = []
        start_vertex = next(iter(self.graph))
        visited.add(start_vertex)

        while len(visited) < len(self.graph):
            min_edge = None
            for vertex in visited:
                for neighbor, weight in self.graph[vertex]:
                    if neighbor not in visited and (min_edge is None or weight < min_edge[1]):
                        min_edge = (neighbor, weight, vertex)

            mst.append(min_edge)
            visited.add(min_edge[0])

        return mst

    def total_cost(self, mst):
        return sum(edge[1] for edge in mst)

# Define the graph
g = Graph()
g.add_edge('San Francisco', 'New York', 2000)
g.add_edge('San Francisco', 'Chicago', 1200)
g.add_edge('San Francisco', 'Denver', 900)
g.add_edge('San Francisco', 'Atlanta', 2200)
g.add_edge('Chicago', 'Denver', 1300)
g.add_edge('Chicago', 'New York', 1000)
g.add_edge('Chicago', 'Atlanta', 700)
g.add_edge('New York', 'Denver', 1600)
g.add_edge('New York', 'Atlanta', 800)
g.add_edge('Denver', 'Atlanta', 1400)

# Compute Minimum Spanning Tree using Prim's Algorithm
mst = g.prim_mst()

# Print the Minimum Spanning Tree edges and total cost
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge[2], '->', edge[0], '=', edge[1], '$')

total_cost = g.total_cost(mst)
print("Total cost of the Minimum Spanning Tree:", total_cost, "$")
