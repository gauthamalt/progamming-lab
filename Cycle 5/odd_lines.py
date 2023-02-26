f1 = open('sample2.txt', 'r')
f2 = open('sample3.txt','w')

File_lines = f1.readlines()

type(File_lines)

for i in range(0,len(File_lines)):

    if(i % 2 != 0):

        f2.write(File_lines[i])

    else:

        pass

f2.close()

f3 = open('sample3.txt', 'r')

print([x.strip() for x in f3.readlines()])
