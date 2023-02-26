class bank:
    
    balance = 0

    def __init__(self):

        self.account_number = int(input("Enter Account Number"))

        self.name  = input("Enter Account User's Name")

        self.account_type = input("Enter Account Type")

        self.balance = 0

    def display(self):

        print(f"{self.name,self.account_number,self.account_type,self.balance}")

    def deposit(self,amount):

        self.balance = self.balance + amount

        print(f"New Balance = {self.balance}")

    def withdraw(self,amount):

        if(amount < self.balance):
         
            self.balance = self.balance - amount

            print(f"New balance = {self.balance}")

        else:

            print("Insuffiecient balance")        

ob1 = bank()

while(1):

    print("1.Deposit Amount \n 2.Withdraw \n 3.Exit")

    option = int(input("Enter your choice"))

    if(option == 1):

        amount = int(input("Enter the amount to be deposited"))

        ob1.deposit(amount)

    elif(option == 2):

        amount = int(input("Enter the amount to be withdrawn"))

        ob1.withdraw(amount)

    else:

        break   


    