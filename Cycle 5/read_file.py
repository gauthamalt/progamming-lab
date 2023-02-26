with open("sample.txt") as f:
    list = f.readlines()

list = [x.strip() for x in list]

print(list)