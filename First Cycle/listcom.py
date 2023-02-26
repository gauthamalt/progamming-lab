a = [int(x) for x in input("Enter tha values of the  list").split()]

print(f"The positive integers are: {[x for x in a if x > 0]}")

print(f"The square of number is: {[x**2 for x in a]}")

b = [x for x in input("Enter a word ")]

# print(b)

c =['a','e','i','o','u','A','E','I','O','U']

print([x for x in b if x in c])

print([ord(x) for x in b])