def checklen(l):
    
    if(len(l)== 0):
        
        return "no common elements"
    return l

a = [int(value) for value in input("Enter the first list ").split()]

b = [int(value) for value in input("Enter the second  list ").split()]

print(f"Whether the strings are of sam length: {len(a) == len(b)}")

print(f"Whether the sum of the lists are same: {sum(a) == sum(b)}")

print(checklen([x for x in a if x in b]))










