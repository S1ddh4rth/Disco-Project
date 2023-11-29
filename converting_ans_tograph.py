import csv
# from kthAssignment import no_profs
csvpath="Answer.csv"
with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile)
    x=[j for i,j in enumerate(list(reader)) if j!=[]]
    solutions=[x[i:i+23] for i in range(0, len(x), 23)]
    ans=solutions
    # print(ans)

