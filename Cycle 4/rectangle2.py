class rectangle:

	def __init__(self,a,b):

		self.__length=a

		self.__breadth=b

	def area(self):

		self.area1 = self.__length * self.__breadth

		return self.area1

	def __lt__(self,other):

		if(self.area1<other.area1):

			return 1

		else:

			return 0

l1 = int(input("Enter length of first rectangle"))

b1 = int(input("Enter breadth of first rectangle"))

l2 = int(input("Enter length of second rectangle"))

b2 = int(input("Enter length of second rectangle"))

r1 = rectangle(l1,b1)

r2 = rectangle(l2,b2)

if(r1<r2):

	print("Rectangle 2 is larger")

else:

	print("Rectangle 1 is larger ")
	
