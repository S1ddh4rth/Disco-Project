from converting_ans_tograph import ans
from ProfessorsAndCourses import *
import csv
import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph()
# edges=[]

class BipartiteGraph:
    # Constructor
    def __init__(self,V1,V2):
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
            # edges.append((self.adjList[i][0],self.adjList[i][1]))
            prev = self.adjList[i][0]
            
    
def conMatrixToGraph(Matrix):
    v1,v2 = [],[]
    for Prof in range(len(Matrix)):
        for Course in range(len(Matrix[Prof])):
            if (0<float(Matrix[Prof][Course])<1000):
                v1.append(Prof),v2.append(Course)

    return v1,v2

def ProfCourseGraph(v1,v2):
    graph = BipartiteGraph(v1,v2)
    graph.DisplayGraph()


profs=[]
courses=CoursesInSem(1)[0]
csv_path="AdjustedInput.csv"
with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in list(reader):
            if row!=[]:   
                profs.append(row[0])

# nodes=profs+courses
# G.add_nodes_from(nodes)
# G.add_edges_from(edges)
for answer in ans:
    v1,v2=conMatrixToGraph(np.array(answer).transpose())
    v1n=[]
    v2n=[]
    for v in v1:
        if profs[v][-2]=="p":
            v1n.append(profs[v][:-3:])
        else:
            v1n.append(profs[v])
    for v in v2:
        v2n.append(courses[v][:-3:])