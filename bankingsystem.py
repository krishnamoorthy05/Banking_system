class bank:
    bank_name = "nation bank"
    branch ="chennai"
    def __init__(self,c_name,acc_no,balance):
        self.c_name=c_name
        self.acc_no=acc_no
        self.balance=balance
    def main(self):
        print()
        msg=int(input(' Enter 1 to display account details : \n Enter 2 to Check Balance : \n Enter 3 to Deposit  : \n Enter 4 to withdraw : \n Enter 5 to Quit : '))
        if msg==1:
            self.display()
            self.main()
        elif msg==2:
            self.balances()
            self.main()
        elif msg==3:
            self.deposit()
            self.main()
        elif msg==4:
            self.withdraw()
            self.main()
        elif msg==5:
            print("Thank for Banking with us!!")
            return
        else:
            print("invalid input")
            self.main()
    def display(self):                                             # to display the details of the bank 
        print(f'BankName :{bank.bank_name}',f'Branck :{bank.branch}',f'Name : {self.c_name}',f'Account number : {self.acc_no}',sep="\n")
    def balances(self):                                            # to check for the balance
        print(f'Account Balance : {self.balance}')
    def deposit(self):                                             # for adding amount into the account
        amount=int(input("Enter the amount to be deposited :Rs "))
        self.balance=self.add(self.balance,amount)
        print(f'Rs {amount} added successfull current balance :Rs {self.balance}')
    def withdraw(self):                                            # to withdraw amount from account
        amount=int(input("Enter the amount to withdraw :Rs "))
        if self.balance >= amount :                                 # check for the balance
            self.balance=self.sub(self.balance,amount)
            print(f'Rs {amount} withdraw successfull current balance :Rs {self.balance}')
        else:
            print(f'Your Balance is {self.balance} : insufficient balance to withdraw {amount}')
    @staticmethod                                                    # static method to add values
    def add(a,b):
        return a+b
    @staticmethod                                                    # static method to substract value
    def sub(a,b):
        return a-b
c1=bank('krishna',200054586123,1000)
c1.main()
        
