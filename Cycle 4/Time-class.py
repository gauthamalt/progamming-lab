class Time:
    def __init__(self,hour,minute,second):

        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__ (self,other):

        hour = self.__hour + other.__hour
        if(hour>=24):

            hour = hour%24

        minute = self.__minute + other.__minute

        if(minute>=60):

            hour+=1    
            minute = minute % 60

        second = self.__second + other.__second

        if(second>=1):

            minute += 1
            second = second %60
        
        return Time(hour,minute,second)

    def viewTime(self):

        print(f"Time : {self.__hour}:{self.__minute}:{self.__second}")

t1 = [int(time) for time in input("Enter The first Time").split(":")]        
t2 = [int(time) for time in input("Enter The Second Time").split(":")]  

Time1 = Time(t1[0],t1[1],t1[2])
Time2 = Time(t2[0],t2[1],t2[2])

timeSum = Time1 + Time2

print("Time 1 :")
Time1.viewTime()

print("Time 2 :")
Time2.viewTime()

print("Added Time :")
timeSum.viewTime()
