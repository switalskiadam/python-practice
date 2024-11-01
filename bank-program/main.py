

def show_balance(balance):
    print('\n')
    print(f"Your balance is ${balance:.2f}")
    print('\n')

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print('\n')
        print("That's not a valid amount.")
        print('\n')
        return 0 ## prevents program crash on invalid input
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print('\n')
        print("Insufficient funds.")
        print('\n')
        return 0 ## prevents program crash on invalid input
    elif amount < 0:
        print('\n')
        print("Amount must be greater than 0")
        print('\n')
        return 0 ## prevents program crash on invalid input
    else:
        return amount


def main():
    balance = 0
    ## used to exit program
    is_running = True

    while is_running:
        print('*******************')
        print("Banking program")
        print('*******************')
        print("1 - Show balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Exit")
        print('*******************')

        choice = input("Enter your choice (1-4): ") ## choice is stored as a str

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('\n')
            print("That is not a valid entry.")
            print('\n')

    print("Thank you, have a nice day!")

if __name__ == '__main__':
    main()