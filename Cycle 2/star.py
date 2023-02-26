def pyramid(lines):

    for i in range(1, lines+1):

        print(f"{'*'*i}")

    for i in range(lines-1, 0, -1):

        print(f"{'*'*i}")

#Driver

a = int(input("Enter the no of lines"))

pyramid(a)