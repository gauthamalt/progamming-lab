def fib(limit):

    a,b=0,1

    print(a)

    for i in range(2,limit):

        c = a + b

        print(c)

        a = b

        b = c


a = int(input("Enter a number: "))

fib(a)