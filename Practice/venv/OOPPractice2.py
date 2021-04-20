print("This is OOP Practice Exercise 2 Script")

class BankAccount():

    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance


    def deposit(self,deposit_amount):

        prev_balance = self.balance
        self.balance = self.balance + deposit_amount
        current_balance = self.balance

        print("Deposit Accepted")
        print("Previous Balance: " + f"{prev_balance}")
        print("Current Balance: " + f"{current_balance}")


    def withdraw(self,withdraw_amount):

        if withdraw_amount <= self.balance:

            prev_balance = self.balance
            self.balance = self.balance - withdraw_amount
            current_balance = self.balance

            print("Withdrawal Done")
            print("Previous Balance: " + f"{prev_balance}")
            print("Current Balance: " + f"{current_balance}")
        else:
            print("Sorry! You have Insufficient Balance")


    def __str__(self):
        result = "Account Owner: " + self.owner + "\n" + "Account Balance: " + f"{self.balance}"
        return result




# -----------------------------------------------

