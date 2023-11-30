from ProfessorsAndCourses import *
from itertools import *
def PermuteElectives(n):    
    if (( n%2 == 0 )and (n <= 24)):
    # n is no of prof slots
        #profElectives = profELEC(read())
        Electives = CoursesInSem(1)[1]
        all_sublists = list(permutations(Electives, n//2))
        all_electives = []
        for sublist in all_sublists:
            all_electives.append([f"{x}_p{y}" for x in sublist for y in range(1,3)])
        return all_electives
# print(PermuteElectives(2))