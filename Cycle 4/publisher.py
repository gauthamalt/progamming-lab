class Publisher:

	def __init__(self,publisher):

		self.publisher = publisher

	def viewDetails(self):

		print(f"Name  : {self.publisher}")

class Book(Publisher):

	def __init__(self,title,author,publisher):

		self.title = title

		self.author = author

		super().__init__(publisher)

	def viewDetails(self):

		print(f"Title  : {self.title}")

		print(f"Author  {self.author}")

		super().viewDetails()

class Python(Book):

	def __init__(self,price,no,title,author,publisher):

		self.price = price

		self.no_of_pages = no

		super().__init__(title,author,publisher)


	def viewDetails(self):

		print(f"Price :{self.price}")

		print(f"No of pages :{self.no_of_pages}")

		super().viewDetails()
		
		
obj = Python(100,200,"Python text","Littymol Sebastain","ABCD publisher")

obj.viewDetails()




