d = {}

n = int(input("Enter the dictionary length"))

for i in range(n):
	
	key = input("Enter key");

	value = input("Enter Value");
	
	d[key] = value


print("dictionary After sort by key Ascending")

print(dict(sorted(d.items())))

print("dictionary After sort by key Descending")

print(dict(sorted(d.items(), reverse= True)))

print("dictionary After sort by value Ascending")

print(dict(sorted(d.items(), key=lambda item: item[1])))

print("dictionary After sort by value Descending")

print(dict(sorted(d.items(), key=lambda item: item[1],reverse=True)))
