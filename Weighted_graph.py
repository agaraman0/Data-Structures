class graph:
    def __init__(self,graph_dict={},weight={}):
        self.graph_dict = graph_dict
        self.weight = weight

    def get_vertex(self):
        if self.graph_dict == None:
            print(None)
        else:
            return self.graph_dict.keys()

    def get_edge(self,vertex):
        return self.graph_dict[vertex]

    def set_vertex(self,vertex):
        self.graph_dict[vertex] = []

    def set_edges(self,vertex,edge):
        if edge not in self.graph_dict.keys():
            graph().set_vertex(self,edge)
        if vertex not in self.graph_dict.keys():
            graph().set_vertex(self,vertex)
        else:
            self.graph_dict[vertex].append(edge)
            
    def printgraph(self):
        return self.graph_dict

    def addweight(self,start,end,weight):
        if start not in self.graph_dict.keys():
            graph().set_vertex(self,edge)
        if end not in self.graph_dict.keys():
            graph().set_vertex(self,vertex)
        else:
            self.weight[weight] = [start,end]

    def printweigra(self):
        return self.weight

graph().set_vertex(0)
graph().set_vertex(1)
graph().set_vertex(2)
graph().set_vertex(3)
graph().set_vertex(4)

graph().set_edges(0,1)
graph().set_edges(0,4)
graph().set_edges(1,0)
graph().set_edges(1,4)
graph().set_edges(1,2)
graph().set_edges(1,3)

graph().set_edges(2,1)
graph().set_edges(2,3)

graph().set_edges(3,1)
graph().set_edges(3,4)
graph().set_edges(3,2)

graph().set_edges(4,1)
graph().set_edges(4,0)
graph().set_edges(4,3)

graph().addweight(0,1,1)
graph().addweight(0,4,2)
graph().addweight(1,0,3)
graph().addweight(1,4,4)
graph().addweight(1,2,5)
graph().addweight(1,3,6)
graph().addweight(2,1,7)
graph().addweight(2,3,8)
graph().addweight(3,1,9)
graph().addweight(3,4,10)
graph().addweight(3,2,11)
graph().addweight(4,1,12)
graph().addweight(4,0,13)
graph().addweight(4,3,14)

print(graph().get_edge(0))
print(graph().get_edge(1))
print(graph().get_edge(2))
print(graph().get_edge(3))
print(graph().get_edge(4))

print(graph().get_vertex())

print(graph().printgraph())

print(graph().printweigra())
