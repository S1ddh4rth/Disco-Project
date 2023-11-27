from InputFile import *
def profCDC(List):
    #CDC list for all the professors
    profCDCList=[]
    for prof in List:
        profcdc = [prof[0],prof[1]]  
        #Details of the Professors
        for Course in prof[2:]:
            if (Course.strip(" ")[0:5] == "FDCDC" or Course.strip(" ")[0:5] == "HDCDC") : 
                #checking if its a CDC
                profcdc.append(Course)
        profCDCList.append(profcdc)

    return profCDCList

def assignPenaltyCDC(List):
    #cost for CDCs depending on preference
    penalty = []
    for Prof in List:
        penalty.append(list(zip(Prof[2:],[x for x in range(1,len(Prof[2:])+1)])))
    return penalty

def CoursesInSem(sem):
    coursesSem1 = [f"FDCDC_F1{x}" for x in range(1,12)]
    electivesSem1 = [f"ELEC_F1{x}" for x in range(1,13)]
    coursesSem2 = [f"FDCDC_F2{x}" for x in range(1,12)]
    electivesSem2 = [f"ELEC_F2{x}" for x in range(1,13)]

    if (sem == 1):return (coursesSem1,electivesSem1)
    else:return (coursesSem2,electivesSem2)