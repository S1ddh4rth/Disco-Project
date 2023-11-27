def read():
    # Reading from input file
    import csv  
    # csv_path = "InputFile.csv"
    csv_path = "AdjustedInput.csv"
    input = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in list(reader)[2:]:
           #Omitting the header Rows
           if row!=[]:
            input.append(row)
    return input

def DisplayInput(List):
    #Display Input in Readable manner
    for line in List:
        print("  ".join(map(str, line)))

# print(read())

