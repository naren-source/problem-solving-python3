class Graph:
    def __init__(self, size):
        self.size = size
        self.vectorMap = {}
        self.vectorList = [-1] * size
        self.edgesList = []
        self.adjacencyMatrix = [
            ([-1] * size) for x in range(size)
        ]
        self.adjacencyList = [
            [] for x in range(size)
        ]
        print()

    def setVertex(self, id, name):
        if 0>id>self.size:
            return
        self.vectorMap[name] = id
        self.vectorList[id] = name

    def setEdge(self, src, dest, weight):
        edgeFront = (
            src,
            dest,
            weight
        )
        edgeBack = (
            dest,
            src,
            weight
        )
        self.edgesList.append(edgeFront)
        self.edgesList.append(edgeBack)

    def generateAdjacencyMatrix(self):
        for src, dest, weight in self.edgesList:
            self.adjacencyMatrix[
                self.vectorMap[src]
            ][
                self.vectorMap[dest]
            ] = weight
        return self.adjacencyMatrix

    def generateAdjacencyList(self):
        for src, dest, weight in self.edgesList:
            adjacency = (
                dest,
                weight
            )
            srcVal = self.vectorMap[src]
            self.adjacencyList[
                srcVal
            ].append(
                adjacency
            )
        return self.adjacencyList

graph = Graph(6)
graph.setVertex(0,'a')
graph.setVertex(1,'b')
graph.setVertex(2,'c')
graph.setVertex(3,'d')
graph.setVertex(4,'e')
graph.setVertex(5,'f')
graph.setEdge('a','e',10)
graph.setEdge('a','c',20)
graph.setEdge('c','b',30)
graph.setEdge('b','e',40)
graph.setEdge('e','d',50)
graph.setEdge('f','e',60)
print(graph.generateAdjacencyMatrix())
print()
print(graph.generateAdjacencyList())



