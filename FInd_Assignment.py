from HungarianAlgorithm import *
from ProfessorCourseGraph import *
from scipy.optimize import linear_sum_assignment
from Graph import *
from Splitting_profs_courses import *

adjust(read1())
answers=[]
vals=[]
if read()==None:
     exit()
matrix , PermutaedElectives = Matrix(assignPenaltyCDC(profCDC(read())))
for i in range(len(matrix)):
    row,col = linear_sum_assignment(matrix[i])
    cost = matrix[i][linear_sum_assignment(matrix[i])[0],linear_sum_assignment(matrix[i])[1]].sum()
    #print(row,col)
    v1,v2 =[],[]
    for j in row:
       if read()[j][0][-2]=="p":
            v1.append(read()[j][0][:-3:])
       else :
            v1.append(read()[j][0])
    
    for j in col:
        if j >=22 :
                v2.append(PermutaedElectives[i][j-22][:-3:])
        else:
                v2.append(CoursesInSem(1)[0][j][:-3:])

    #print(v2)

    graph = BipartiteGraph(v1,v2)
    graph.DisplayGraph()
    print()




