class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def transfer(self, receiver, amount):
        if amount <= self.balance:
            self.balance -= amount
            receiver.balance += amount
            print(f"Transfer of {amount} successful")
            print(f"New balance: {self.balance}")
        else:
            print("Insufficient funds.")        

    def check_balance(self):
        print(f"{self.name}'s balance is: {self.balance}")


# Store accounts in memory
accounts = {}


def create_account():
    name = input("Enter account name: ")
    
    if name in accounts:
        print("Account already exists!")
        return

    account = BankAccount(name)
    accounts[name] = account
    print(f"Account created for {name}")


def deposit_money():
    name = input("Enter account name: ")
    
    if name not in accounts:
        print("Account not found")
        return

    amount = float(input("Enter amount to deposit: "))
    accounts[name].deposit(amount)


def withdraw_money():
    name = input("Enter account name: ")
    
    if name not in accounts:
        print("Account not found")
        return

    amount = float(input("Enter amount to withdraw: "))
    accounts[name].withdraw(amount)


def transfer_money():
    sender_name = input("Enter your account name: ")

    if sender_name not in accounts:
        print("Sender account not found")
        return
    
    receiver_name = input("Enter receiver account name: ")

    if receiver_name not in accounts:
        print("Receiver account not found")
        return
    
    amounts = float(input("Enter amount to transfer: "))

    sender = amounts[sender_name]
    receiver = amounts[receiver_name]


    if amounts <= sender.balance:
        sender.transfer(amounts)

      

        print("Transfer successful")
        print(f"{sender_name}'s new balannce: {sender. balance}")
        print(f"{receiver_name}'s new balance: {receiver.balance}")
    else:
        print("Insufficient funds")    


def check_balance():
    name = input("Enter account name: ")

    if name not in accounts:
        print("Account not found")
        return

    accounts[name].check_balance()


def show_menu():
    print("\n===== BANK SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            transfer_money()
        elif choice == "5":    
            check_balance()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()