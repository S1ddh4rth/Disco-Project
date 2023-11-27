from ProfessorsAndCourses import *
def Matrix(CDCList,Penalty):
    Matrix = []
    for cdc in CDCList:
        for Prof in Penalty:
            for Cdc,penalty in Prof:
                if Cdc == cdc:
                    Matrix.append((list([cdc,penalty])))
    return Matrix

print((Matrix(CoursesInSem(1)[0],assignPenaltyCDC(profCDC(read())))))
