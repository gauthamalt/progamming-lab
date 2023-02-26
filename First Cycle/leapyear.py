a = int(input("Enter the starting year"))

n = int(input("Enter the ending year"))

for i in range(a,n):

    if(i % 400 == 0 and i % 100 == 0):
        
        print(i) 
        
    elif(i % 4 == 0 and i % 100 != 0):
        
        print(i)
