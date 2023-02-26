a =[int(x) for x in input("Enter an integer").split()]

print([ x if x < 100 else "over" for x in a ])

