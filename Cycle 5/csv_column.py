import csv
with open('department.csv','r') as File:
    reader = csv.reader(File)
    

    for r in reader:
        print(r[0],r[1],r[2])


