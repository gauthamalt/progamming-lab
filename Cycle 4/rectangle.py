class rectangle:

    ar = 0

    def __init__(self):

        self.length = int(input("Enter the length"))

        self.breadth = int(input("Enter the breadth"))

    def area(self):

        self.ar = self.length * self.breadth

        print(f"Area = {self.ar}")

    def computePeri(self):

        print(f"Perimeter = {2 * (self.length + self.breadth)}")

    def compare(self,ob):

            if(self.ar > ob.ar):

                print("Area of first is greater than second")

            else:

                print("Area of second is greater than first")

#Driver

ob1 = rectangle()

ob1.area()

ob1.computePeri()

ob2 = rectangle()

ob2.area()

ob1.compare(ob2)
