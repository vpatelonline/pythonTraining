class Account():

    def __init__(self,owner,balance=0):

        self.owner=owner
        self.balance=balance

    def deposit(self,dep_amt):
        self.balance += dep_amt
        print(f"Added {dep_amt} to the balance. Total amount is {self.balance}")

    def withdrawal(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print(f"Withdrawal of ${wd_amt} is accepted")
        else:
            print(f"Sorry, You don't have enough fund, You have {self.balance} in your account.")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}\n"

a=Account("Sam",10000)
print(a)

a.deposit(1000)
print(a)

a.withdrawal(100)
print(a)

a.withdrawal(11000)
print(a)