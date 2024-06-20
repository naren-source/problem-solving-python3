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
        self.totalPathCount = 0
        self.visitedMap = set()

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

    def countTotalPathUtil(self, source, destination, visitedMap):
        visitedMap.add(source)
        if source == destination:
            self.totalPathCount += 1
        for neighbours in self.verticesList[source].connectedTo:
                if neighbours not in visitedMap:
                    self.countTotalPathUtil(neighbours, destination, visitedMap)
        visitedMap.remove(source)

    def countTotalPath(self, source, destination):
        self.totalPathCount = 0
        self.visitedMap = set()
        self.countTotalPathUtil(source, destination, self.visitedMap)
        return self.totalPathCount


dGraph = DirectedGraph()
verticesList = ['a', 'b', 'c', 'd', 'e']
for vertex in verticesList:
    dGraph.createVertex(vertex)
edgesList = [
    ('a', 'b'),
    ('a', 'c'),
    ('a', 'e'),
    ('b', 'd'),
    ('b', 'e'),
    ('c', 'e'),
    ('d', 'c')
]
for src, dest in edgesList:
    dGraph.setEdge(src, dest)
print(dGraph.countTotalPath('a', 'e'))
