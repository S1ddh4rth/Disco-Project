import csv
class BipartiteGraph:
    # Constructor
    def _init_(self,V1,V2):
        self.adjList = []
        for (src, dest) in sorted(zip(V1,V2)):
            # allocate node in adjacency list from src to dest
            self.adjList.append((src,dest))
    def DisplayGraph(self):
        prev = "Random"
        for i in range(len(self.adjList)):
        # print current vertex and all its neighboring vertices
            if(self.adjList[i][0] != prev):
                print()
            print(f'({self.adjList[i][0]} -> {self.adjList[i][1]}) ', end='')
            prev = self.adjList[i][0]
            
    
def conMatrixToGraph(Matrix):
    v1,v2 = [],[]
    for Prof in range(len(Matrix)):
        for Course in range(len(Matrix[Prof])):
            if (0<Matrix[Prof][Course]<1000):
                v1.append(Prof),v2.append(Course)
    
    return v1,v2

def ProfCourseGraph(v1,v2):
    graph = BipartiteGraph(v1,v2)
    graph.DisplayGraph()