class BipartiteGraph:
    # Constructor
    def __init__(self,V1,V2,n):
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
            
    