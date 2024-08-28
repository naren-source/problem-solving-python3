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
            self.verticesList[dest].connected_to[src] = weight

    def countNodesAtLevel(self, root, targetLevel):
        queue = [(root, 0)]
        countNodes = 0
        visited = set()
        while queue:
            node, level = queue.pop(0)
            visited.add(node)
            if level == targetLevel:
                countNodes += 1
            for neighbour in self.verticesList[node].connected_to:
                if neighbour not in visited:
                    queue.append((neighbour, level+1))
        return countNodes


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

target_level = 2
print(f"Number of nodes at level {target_level}: {graph.countNodesAtLevel('a', target_level)}")
