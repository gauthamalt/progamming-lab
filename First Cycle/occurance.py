a = input("Enter a sentence").split()

d = {}

for i in set(a):

    d[i] = a.count(i)

print(d)