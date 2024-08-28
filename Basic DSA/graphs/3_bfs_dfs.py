class Vertex:
    def __init__(self, data):
        self.data = data
        self.connected_to = {}


class Graph:
    def __init__(self):
        self.verticesList = {}

    def addVertex(self, data):
        if data not in self.verticesList:
            self.verticesList[data] = Vertex(data)

    def addEdge(self, src, dest, weight=1):
        if src in self.verticesList and dest in self.verticesList:
            self.verticesList[src].connected_to[dest] = weight
            self.verticesList[dest].connected_to[src] = weight  # Assuming undirected graph

    def bfs(self, start):
        queue = [start]
        visited = set()
        while queue:
            first = queue.pop(0)
            visited.add(first)
            print(first, end=" ")
            for neighbour in self.verticesList[first].connected_to:
                if neighbour not in visited:
                    queue.append(neighbour)

    def dfs(self, start, visited=set()):
        print(start, end=" ")
        visited.add(start)
        for neighbour in self.verticesList[start].connected_to:
            if neighbour not in visited:
                self.dfs(neighbour, visited)


graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')

graph.addEdge('a', 'b')
graph.addEdge('a', 'c')
graph.addEdge('b', 'd')
graph.addEdge('b', 'e')
graph.addEdge('c', 'f')


graph.bfs('a')
print()
graph.dfs('a')
