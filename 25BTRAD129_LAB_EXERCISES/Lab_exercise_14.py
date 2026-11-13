class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Encapsulated attribute

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.__balance += amount
            print(f"Rs. {amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Rs. {amount:.2f} withdrawn successfully.")

    def check_balance(self):
        print(f"Available balance: Rs. {self.__balance:.2f}")

account = BankAccount("Arun", 5000)

while True:
    print("\nBANK ACCOUNT MENU")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Enquiry")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        amount = float(input("Enter deposit amount: Rs. "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: Rs. "))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        print("Thank you for using the bank system.")
        break
    else:
        print("Invalid choice.")
