from HungarianAlgorithm import *
import csv

cost_matrix = Matrix(assignPenaltyCDC(profCDC(read()))).transpose()
ans_pos = hungarian_algorithm(cost_matrix.copy())#Get the element position.
ans, ans_mat = ans_calculation(cost_matrix, ans_pos)#Get the minimum or maximum value and corresponding matrix.
ans_mat = ans_mat.transpose()

with open("Answer.csv", 'w+') as csvfile2: 
    csvwriter = csv.writer(csvfile2)
    csvwriter.writerows(ans_mat.transpose())
    csvwriter.writerow([])
    csvwriter.writerow([])
    csvwriter.writerow([])
     
for Prof in range(len(ans_mat)):
    penaltyMatrixModified = assignPenaltyCDC(profCDC(read()))
    for Course in range(len(ans_mat[Prof])):
        if(0<ans_mat[Prof][Course]<1000):
            if (Course%2):
                temp = list(penaltyMatrixModified[Prof][Course])
                temp[1]= 1000
                penaltyMatrixModified[Prof][Course] = tuple(temp)
                temp2 = list(penaltyMatrixModified[Prof][Course-1])
                temp2[1]= 1000
                penaltyMatrixModified[Prof][Course-1] = tuple(temp2)
                break
            elif(Course%2 == 0):
                temp = list(penaltyMatrixModified[Prof][Course])
                temp[1]= 1000
                penaltyMatrixModified[Prof][Course] = tuple(temp)
                temp2 = list(penaltyMatrixModified[Prof][Course+1])
                temp2[1]= 1000
                penaltyMatrixModified[Prof][Course+1] = tuple(temp2)
                break
    #print(penaltyMatrixModified)
    cost_matrix2 = Matrix(penaltyMatrixModified).transpose()
    ans_pos2 = hungarian_algorithm(cost_matrix2.copy())#Get the element position.
    ans2, ans_mat2 = ans_calculation(cost_matrix2, ans_pos2)
    csv_path2 = "Answer.csv"
    with open(csv_path2, 'a+') as csvfile2:
        for a in (ans_mat2):
            if((np.all(a==0))):
                break
        else:
        #is_all_zero = np.all((arr == 0))
            print(ans2)
            csvwriter = csv.writer(csvfile2)
            csvwriter.writerows(ans_mat2)
            csvwriter.writerow([])
            csvwriter.writerow([])
            csvwriter.writerow([])




        
        