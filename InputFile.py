# import numpy as np
def read():
    # Reading from input file
    import csv  
    # csv_path = "InputFile.csv"
    csv_path = "AdjustedInput.csv"
    input = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in list(reader)[0::]:
           #Omitting the header Rows
           if row!=[]:
            input.append(row)
    # print(len(input))
    no_prof_slots=len(input)
    if no_prof_slots%2==1:
        print("CRASH: INVALID ASSIGNMENT - Odd number of professor slots, Indicating that alteast 1 course will be half assigned")
    else:
        if no_prof_slots>=22 and no_prof_slots<=46:
            return input
        elif no_prof_slots<22:
            print("CRASH: INVALID ASSIGNMENT - Cannot assign CDCs to all professors since number of slots that professors can teach is less than what is needed")
        elif no_prof_slots>46:
            print("CRASH: INVALID ASSIGNMENT - Not enough courses to fill all prof slots, some professors will not complete necessary number of courses depending on their category (X1,x2,x3) ")
        
def DisplayInput(List):
    #Display Input in Readable manner
    for line in List:
        print("  ".join(map(str, line)))

# print(read())
def read_ele():
    # Reading from input file
    import csv  
    # csv_path = "InputFile.csv"
    csv_path = "InputFile.csv"
    input = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in list(reader)[2::]:
           #Omitting the header Rows
           if row!=[]:
            input.append(row)
    # print(len(input))
    return input

# print(np.array(read()))
