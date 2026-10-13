from finance import add_income,add_expense,calculate_balance,get_amount
from storage import save_transactions,load_transactions

def main():
    transactions = load_transactions()

    while True:
        print("\n=====PERSONAL FINANCE MANAGER")

        print("1.Add Income")
        print("2.Add Expenses")
        print("3.View Expenses")
        print("4.Check Balance")
        print("5.Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            name = input("Enter income name:")
            amount = get_amount()

            add_income(transactions,name,amount)

            save_transactions(transactions)

            print("Income added successfully")

        elif choice == "2":
            name = input("Enter expense name:")
            amount = get_amount()

            add_expense(transactions,name,amount)

            save_transactions(transactions)

            print("Expenses added successfully")

        elif choice == "3":
            if not  transactions:
                print("There is no transactions!!")

            else:
                for transaction in transactions:
                    print(f"{transaction['type'].title()}|"
                          f"{transaction['name']}|"
                          f"${transaction['amount']}")

        elif choice == "4":
            balance = calculate_balance(transactions)

            print(f"Current balance : ${balance}")

        elif choice == "5":
            print("Thank For Using Finance Manager")
            break

        else:
            print("Invalid Choice Please Try Again")

if __name__ == "__main__":
    main()