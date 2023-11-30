from InputFile import *
import numpy as np

electivesSem1 = [f"FDELEC_F1{x}_p{y}" for x in range(1,13) for y in [1,2]]
def profCDC(List):
    #CDC list for all the professors
    profCDCList=[]
    for prof in List:
        profcdc = [prof[0],prof[1]]  
        #Details of the Professors
        for Course in prof[2:]:
            #if (Course.strip(" ")[0:5] == "FDCDC" or Course.strip(" ")[0:5] == "HDCDC") : 
                #checking if its a CDC
            profcdc.append(Course)
        profCDCList.append(profcdc)
    # print(len(profCDCList))
    #print(np.array(profCDCList))
    return np.array(profCDCList)

def CoursesInSem(sem):
    coursesSem1 = [f"FDCDC_F1{x}_p{y}" for x in range(1,12) for y in [1,2]] 
    # coursesSem1 = [f"FDCDC_F1{x}" for x in range(1,12)]
    electivesSem1 = [f"FDELEC_F1{x}" for x in range(1,13)] 
    coursesSem2 = [f"FDCDC_F2{x}_p{y}" for x in range(1,12) for y in [1,2]]
    electivesSem2 = [f"FDELEC_F2{x}" for x in range(1,13)]

    if (sem == 1):return (coursesSem1,electivesSem1)
    else:return (coursesSem2,electivesSem2)

def assignPenaltyCDC(List):
    # assigning cost for CDCs depending on preference order submitted by professors
    penalty = []
    # print(len(List))

    for Prof_preference_list in List:
        # penaltytemp=[]
        penalty_prof=[]
        assignedCDCs=[]
        assignedELEs=[]
        penaltytemp={}
        pen_value=1
        pen_value_ele=1
        for preference in Prof_preference_list[2::]:
            if preference[0:5]=="FDCDC" or preference[0:5]=="HDCDC":
                penaltytemp[preference]=pen_value
                assignedCDCs.append(preference)
                if preference[-1]=="2":
                    pen_value+=1
            else:
                penaltytemp[preference]=pen_value_ele
                assignedELEs.append(preference)
                if preference[-1]=="2":
                    pen_value_ele+=1
        # penaltytemp.append(list(zip(Prof_preference_list[2:],[x for x in range(1,len(Prof_preference_list[2:])+1)])))
        for CDC in CoursesInSem(1)[0]:
            if CDC in assignedCDCs:
                value=penaltytemp[CDC]
                penalty_prof.append((CDC,value))
            else:
                penalty_prof.append((CDC,1000))
        for ELE in electivesSem1:
            if ELE in assignedELEs:
                value=penaltytemp[ELE]
                penalty_prof.append((ELE,value))
            else:
                penalty_prof.append((ELE,1000))
        penalty.append(penalty_prof)
    #print(penalty)
    return penalty #returns a list of lists containing corresponding penalties for all CDCs in a semester

# print(assignPenaltyCDC(profCDC(read())))
# print(CoursesInSem(1))
# print(profCDC(read()))

# def profELE(List):
#     #ELE list for all the professors
#     profELEList=[]
#     for prof in List:
#         profELE = [prof[0],prof[1]]  
#         #Details of the Professors
#         for Course in prof[2:]:
#             if (Course.strip(" ")[0:5] == "FDELE" or Course.strip(" ")[0:5] == "HDELE") : 
#                 #checking if its a ELE
#                 profELE.append(Course)
#         profELEList.append(profELE)
#     # print(len(profELEList))

#     return np.array(profELEList)

# def assignPenaltyELE(List):
#     # assigning cost for ELEs depending on preference order submitted by professors
#     penalty_ele = []
#     # print(len(List))

#     for Prof_preference_list in List:
#         penalty_eletemp=[]
#         penalty_ele_prof=[]
#         assignedELEs=Prof_preference_list[2:]
#         penalty_eletemp={}
#         pen_value=1
#         for preference in Prof_preference_list[2::]:
#             penalty_eletemp[preference]=pen_value
#             if preference[-1]=="2":
#                 pen_value+=1
#             # pen_value+=1
#         # penalty_eletemp.append(list(zip(Prof_preference_list[2:],[x for x in range(1,len(Prof_preference_list[2:])+1)])))
#         for ELE in CoursesInSem(1)[0]:
#             if ELE in assignedELEs:
#                 value=penalty_eletemp[ELE]
#                 penalty_ele_prof.append((ELE,value))
#             else:
#                 penalty_ele_prof.append((ELE,1000))
#         penalty_ele.append(penalty_ele_prof)
#     return penalty_ele #returns a list of lists containing corresponding penalties for all ELEs in a semester
