a = int(input("Enter first number: "))

b = int(input("Enter first number: "))

c = int(input("Enter first number: "))

if( a > b):

    if( a > c ):

        print(f"{a} is the greatest")

    elif( c > a ):

        print(f"{c} is the greatest")

elif( b > c ):

    print(f"{b} is the greatest")