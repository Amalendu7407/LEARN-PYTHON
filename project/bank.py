# Banking System Project Using Basic Functions

accounts = {}
transactions = {}


# Create New Account
def create_account():

    acc_no = int(input("Enter Account Number : "))

    if acc_no in accounts:
        print("\nAccount Already Exists")

    else:
        name = input("Enter Name : ")
        balance = float(input("Enter Initial Balance : "))

        accounts[acc_no] = [name, balance]
        transactions[acc_no] = []

        print("\nAccount Created Successfully")


# Deposit Money
def deposit_money():

    acc_no = int(input("Enter Account Number : "))

    if acc_no in accounts:

        amount = float(input("Enter Amount : "))

        accounts[acc_no][1] += amount

        transactions[acc_no].append(f"Deposited : {amount}")

        print("\nAmount Deposited Successfully")

    else:
        print("\nAccount Not Found")


# Withdraw Money
def withdraw_money():

    acc_no = int(input("Enter Account Number : "))

    if acc_no in accounts:

        amount = float(input("Enter Amount : "))

        if amount > accounts[acc_no][1]:

            print("\nInsufficient Balance")

        else:

            accounts[acc_no][1] -= amount

            transactions[acc_no].append(f"Withdrawn : {amount}")

            print("\nAmount Withdrawn Successfully")

    else:
        print("\nAccount Not Found")


# Display Account Details
def display_account():

    acc_no = int(input("Enter Account Number : "))

    if acc_no in accounts:

        print("\nAccount Number :", acc_no)
        print("Name           :", accounts[acc_no][0])
        print("Balance        :", accounts[acc_no][1])

    else:
        print("\nAccount Not Found")


# Delete Account
def delete_account():

    acc_no = int(input("Enter Account Number : "))

    if acc_no in accounts:

        del accounts[acc_no]
        del transactions[acc_no]

        print("\nAccount Deleted Successfully")

    else:
        print("\nAccount Not Found")


# Show Last 5 Transactions
def show_transactions():

    acc_no = int(input("Enter Account Number : "))

    if acc_no in accounts:

        print("\nLast 5 Transactions :")

        if len(transactions[acc_no]) == 0:

            print("No Transactions Yet")

        else:

            for t in transactions[acc_no][-5:]:
                print(t)

    else:
        print("\nAccount Not Found")


# Main Program
while True:

    print("\n====== BANKING SYSTEM ======")

    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account")
    print("5. Delete Account")
    print("6. Show Last 5 Transactions")
    print("7. Exit")

    choice = int(input("\nEnter Choice : "))

    if choice == 1:
        create_account()

    elif choice == 2:
        deposit_money()

    elif choice == 3:
        withdraw_money()

    elif choice == 4:
        display_account()

    elif choice == 5:
        delete_account()

    elif choice == 6:
        show_transactions()

    elif choice == 7:
        print("\nThank You")
        break

    else:
        print("\nInvalid Choice")