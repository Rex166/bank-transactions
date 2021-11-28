import time

class Bank:
    balance = {
        'niklas': 4000,
        'jannis': 1890,
        'annika': 6500,
    }

    def withdraw(self):
        if self.balance - amount < 0:
            print("You don't have sufficient money for this transaction on your account.")
        else:
            self.balance -= amount
            return self.balance, amount

    def deposit(self):
        self.balance += amount
        return self.balance, amount

    def transaction_txt(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        transaction = open(f"{name}_transaction_{timestr}.txt", 'w')
        if withdraw_money == 'y':
            transaction.write(f"Amount withdrawn: {amount}\nOld account balance: {old_balance}\nNew account balance: {self.balance}")
        else:
            transaction.write(f"Amount deposited: {amount}\nOld account balance: {old_balance}\nNew account balance: {self.balance}")

name = input("What is your name?: ").lower()
account = Bank() 

if name in Bank.balance:
    account.balance = Bank.balance.get(name)
    transfer = True

    while transfer:
        print(f"You currently have {account.balance} money on your account.")

        withdraw_money = input("Do you want to withdraw money? (y/n): ")

        if withdraw_money == 'y':
            amount = float(input("How much money do you want to withdraw?: "))
            old_balance = account.balance
            account.withdraw()
            if old_balance == account.balance:
                continue
            
            else:
                print (account.balance)
                account.transaction_txt()
        
        else:
            deposit_money = input("Do you want to deposit money? (y/n): ")

            if deposit_money == 'y':
                amount = float(input("How much money do you want to deposit?: "))
                old_balance = account.balance
                account.deposit()
                print (account.balance)
                account.transaction_txt()

        new_transaction = input("Do you want to make another transaction? (y/n): ")
        if new_transaction != 'y':
            transfer = False
else:
    print("You don't have an account in our system.")