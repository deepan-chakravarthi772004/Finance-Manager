def add_income(transactions,name,amount):
    transaction = {
        "type":"income",
        "name":name,
        "amount":amount
    }
    transactions.append(transaction)

def add_expense(transactions,name,amount):
    transaction = {
        "type":"expense",
        "name":name,
        "amount":amount
    }
    transactions.append(transaction)

def calculate_balance(transactions):
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"]for t in transactions if t["type"] == "expense")

    return income-expense

def get_amount():
    while True:
        try:
            amount = float(input("Enter amount:"))
            if amount <= 0:
                print("Amount must be greater than zero!!")
                continue

            return amount

        except ValueError:
            print("Invalid input,please give valid input.")