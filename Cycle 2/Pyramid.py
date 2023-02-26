def pyramid(lines):

    for i in range(lines):

        for j in range(1,i+1):

            print(f" {j*i}", end = " ")
            
        print("\n")

#Driver

a =int(input("Enter the no of lines"))

pyramid(a)