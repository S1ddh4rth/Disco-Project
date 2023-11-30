from ProfessorsAndCourses import *
import numpy as np 
from Electives import *

def Matrix(Penalty):
    # print(electivesSem1)
    all_cases=[]
    Matrix = []
    ele_penalties=[]
    no_profs=len(Penalty)
    no_courses=len(Penalty[1])
    for row in Penalty:
        matrix_row=[]
        ele_matrix_row=[]
        for assignment in row:
            if assignment[0][0:5]=="FDCDC" or assignment[0][0:5]=="HDCDC":
                matrix_row.append(assignment[1])
            else:
                ele_matrix_row.append(assignment[1])
        Matrix.append(matrix_row)
        ele_penalties.append(ele_matrix_row)
        Base=np.array(Matrix)
        extra=no_profs-22
    ElectivesCombination = PermuteElectives(extra)
    for i in ElectivesCombination:
        Base=np.array(Matrix)
        for j in range(extra):
            to_be_added=[]
            for k in ele_penalties[electivesSem1.index(i[j])]:
                to_be_added.append([k])
            Base = np.append(Base,np.array(to_be_added),axis=1)

        all_cases.append(np.array(Base))
    return all_cases,ElectivesCombination
