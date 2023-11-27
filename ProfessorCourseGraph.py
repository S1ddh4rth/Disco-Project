from ProfessorsAndCourses import *
import numpy as np 

def Matrix(Penalty):
    Matrix = []
    no_profs=len(Penalty)
    no_courses=len(Penalty[1])
    for row in Penalty:
        matrix_row=[]
        for assignment in row:
            matrix_row.append(assignment[1])
        Matrix.append(matrix_row)
        np.array(Matrix)
    for j in range(no_profs-22):
        column=[[1000]]*no_profs
        Matrix=np.append(Matrix,column,axis=1)
    print(no_profs)

    return np.array(Matrix)

print(Matrix(assignPenaltyCDC(profCDC(read()))))
