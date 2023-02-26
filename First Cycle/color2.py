a = list(input("Enter the first list of color").split())

b = list(input("Enter the second list of color").split())

print([x for x in a if x not in b])