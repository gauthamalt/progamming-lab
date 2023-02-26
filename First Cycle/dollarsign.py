s = input("enter word")

res = s[0]

res += s[1:].replace(s[0],'$')

print(res)



