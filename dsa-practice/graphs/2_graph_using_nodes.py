class Vertex:
    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.connected_to = {}

class Graph:
    def __init__(self):
        self.vertexSize = 0
        self.verticesList = {}
        self.adjacencyMatrix = []
        self.adjacencyList = []
    
    def setVertex(self, data):
        if data not in self.verticesList:
            nVertex = Vertex(data, self.vertexSize)
            self.verticesList[data] = nVertex
            self.vertexSize += 1
        
    def setEdge(self, src, dest, weight):
        sVertex = self.verticesList[src]
        sVertex.connected_to[dest] = weight
        dVertex = self.verticesList[dest]
        dVertex.connected_to[src] = weight        
        
    def generateAdjacencyMatrix(self):
        self.adjacencyMatrix = [ [-1] * self.vertexSize for _ in range(self.vertexSize)]        
        for vKey, vertex in self.verticesList.items():
            for secondaryVertex in self.verticesList.values():
                if vertex.connected_to.get(secondaryVertex.data) is not None:
                    self.adjacencyMatrix[vertex.index][secondaryVertex.index] = vertex.connected_to[secondaryVertex.data]
        return self.adjacencyMatrix

    def generateAdjacencyList(self):
        self.adjacencyList = [ [] for _ in range(self.vertexSize)]
        for vName, vertex in self.verticesList.items():
            for cVertex, cWeight in vertex.connected_to.items():
                adjL = (
                    cVertex,
                    cWeight
                )
                self.adjacencyList[vertex.index].append(adjL)
        return self.adjacencyList

        
graph = Graph()
graph.setVertex('a')
graph.setVertex('b')
graph.setVertex('c')
graph.setVertex('d')
graph.setVertex('e')
graph.setVertex('f')
graph.setEdge('a','e',10)
graph.setEdge('a','c',20)
graph.setEdge('c','b',30)
graph.setEdge('b','e',40)
graph.setEdge('e','d',50)
graph.setEdge('f','e',60)
print("Adjacency Matrix: ", graph.generateAdjacencyMatrix())
print()
print("Adjacency List", graph.generateAdjacencyList())
print()
