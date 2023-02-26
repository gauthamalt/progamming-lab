a = [int(x) for x in input("Enter some integers").split()]

[x if x%2 != 0 else a.remove(x) for x in a]

print(a)