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
    for j in range(11-no_profs):
        Matrix.append([1000]*no_courses)

    return np.array(Matrix)

print(Matrix(assignPenaltyCDC(profCDC(read()))))
