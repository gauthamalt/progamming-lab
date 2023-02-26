def strings():

    a = input("Enter a string ")

    s ={}

    for i in set(a):

        s[i] = a.count(i)

    return(s)

print(strings())
