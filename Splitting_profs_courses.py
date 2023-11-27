import csv

def read1():
    # Reading from input file
    import csv  
    csv_path = "InputFile.csv" 
    input = []
    adjusted=[]
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in list(reader)[2:]:
           #Omitting the header Rows
           input.append(row)
    for row in input:
        newset=[]
        newrow=[]
        for course in row[2::]:
            newrow.append(course+"_p1")
            newrow.append(course+"_p2")
            row[2::]=newrow
        if row[1]=='x1':
            adjusted.append(row)
        elif row[1]=='x2':
            temp=row[0]
            temp+="_p1"
            old=row[1::]
            row=[temp]+old
            adjusted.append(row)
            temp=temp[:-3:]
            temp+="_p2"
            old=row[1::]
            row=[temp]+old
            adjusted.append(row)
        else:
            temp=row[0]
            temp+="_p1"
            old=row[1::]
            row=[temp]+old
            adjusted.append(row)
            temp=temp[:-3:]
            temp+="_p2"
            old=row[1::]
            row=[temp]+old
            adjusted.append(row)
            temp=temp[:-3:]
            temp+="_p3"
            old=row[1::]
            row=[temp]+old
            adjusted.append(row)
    return adjusted

def adjust(adjusted):
    csv_path2 = "AdjustedInput.csv"
    with open(csv_path2, 'w+') as csvfile2:   
                csvwriter = csv.writer(csvfile2)
                csvwriter.writerows(adjusted)
adjust(read1())


    

