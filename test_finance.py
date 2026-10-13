from finance import add_income,add_expense,calculate_balance

def test_add_income():
    transactions = []

    add_income(transactions,"Salary",25000)
    add_income(transactions,"Trading",15000)

    assert len(transactions) == 2
    assert transactions[0]["type"] == "income"
    assert transactions[0]["amount"] == 25000
    assert transactions[1]["type"] == "income"
    assert transactions[1]["amount"] == 15000

def test_add_expenses():
    transactions = []

    add_expense(transactions,"Food",2000)

    assert len(transactions) == 1
    assert transactions[0]["type"] == "expense"
    assert transactions[0]["amount"] == 2000

def test_calculate_balance():
    transactions =[]

    add_income(transactions,"Salary",25000)
    add_income(transactions,"Trading",15000)
    add_expense(transactions,"Food",2000)
    add_expense(transactions,"Travel",1000)

    result = calculate_balance(transactions)
    assert result == 37000