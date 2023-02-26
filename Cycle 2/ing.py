def check(s):

    if(s[-3:]=='ing'):
        
        print(s[:len(s)-3 ]+'ly')

    else:

        print(s+'ing')    


s = input("Enter a string")

check(s)