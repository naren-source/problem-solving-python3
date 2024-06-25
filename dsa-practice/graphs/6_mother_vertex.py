class Vertex:
    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.connectedTo = {}

class DirectedGraph:
    def __init__(self):
        self.size = 0
        self.verticesList = {}
        self.vertexMap = {}

    def createVertex(self, data):
        if data not in self.verticesList:
            newVertex = Vertex(data, self.size)
            self.verticesList[data] = newVertex
            self.vertexMap[newVertex.data] = newVertex.index
            self.size += 1

    def setEdge(self, source, destination, weight=1):
        if source not in self.verticesList and destination not in self.verticesList:
            return
        sourceVertex = self.verticesList[source]
        sourceVertex.connectedTo[destination] = weight

    def dfs(self, start, visited):
            visited.add(start)
            for neighbour in self.verticesList[start].connectedTo:
                if neighbour not in visited:
                    self.dfs(neighbour, visited)

    def findMotherVertex(self):
        for vertex in self.verticesList:
            visited = set()
            self.dfs(vertex, visited)
            if len(visited) == len(self.verticesList):
                print(vertex, end=" ")


dGraph = DirectedGraph()
verticesList = ['0', '1', '2', '3', '4']
for vertex in verticesList:
    dGraph.createVertex(vertex)
edgesList = [
    ('0', '3'),
    ('0', '2'),
    ('1', '0'),
    ('2', '1'),
    ('3', '4')
]
for src, dest in edgesList:
    dGraph.setEdge(src, dest)
dGraph.findMotherVertex()
