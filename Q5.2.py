import time
import random

def get_account_number():
    while True:
        try:
            account_no = int(input("\nEnter your card number: \n"))
            if 10000000 <= account_no <= 99999999:
                return account_no
            else:
                print("Account number should be of 8 numbers.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def withdraw_money(balance):
    while True:
        try:
            money = float(input("\nEnter the money you want to withdraw ₹"))
            if money > balance:
                print("\nYour balance is lower than the amount you want to withdraw")
            elif money < 100:
                print("Minimal amount should be ₹100")
            else:
                return money
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def deposit_money(balance):
    while True:
        try:
            money = float(input("\nEnter the amount you want to deposit ₹"))
            balance += money
            return balance
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def transfer_money(balance, account_no):
    while True:
        try:
            money = float(input("\nEnter the amount you want to transfer: ₹"))
            ac = int(input("\nEnter the account you want to transfer to: "))
            if ac == account_no:
                print("\nCan't send money to yourself, can you?\n")
            elif not (10000000 <= ac < 99999999):
                print("\nAccount no. should be of 8 digits\n")
            elif money > balance or money < 100:
                if money > balance:
                    print("Not enough money in your account\n")
                else:
                    print("Minimal transfer amount is ₹100\n")
            else:
                time.sleep(2)
                balance -= money
                print(f"\nTransferred amount ₹{money:.3f} to Account with account no: {ac}\n")
                print(f"Your bank now has ₹{balance:.3f}")
                return balance
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def main():
    c = random.randint(1000, 10000)
    account_no = get_account_number()
    print("\nChecking your card status, please wait :)\n")
    time.sleep(2)
    print("\nWELCOME TO ATM\n")
    
    while True:
        print("\nWhat would you like to do?\n1. Withdrawal\n2. Check balance\n3. Deposit money\n4. Transfer money\n5. Cancel\n")
        n = int(input())
        
        if n == 1:
            c -= withdraw_money(c)
            time.sleep(2)
        elif n == 2:
            print(f"\nYour account has ₹{c:.3f}\n")
        elif n == 3:
            c = deposit_money(c)
            print("Successfully deposited\n")
        elif n == 4:
            c = transfer_money(c, account_no)
        elif n == 5:
            print("\nTHANK YOU FOR CHOOSING US :)\n\n")
            return
        else:
            print("\nInvalid option :)\n")

if __name__ == "__main__":
    main()
