from storage import save_transactions,load_transactions

def test_save_load_transactions(tmp_path):
    file_path = tmp_path / "transactions.json"

    transactions = [
        {"type":"income","name":"Salary","amount":25000},
        {"type":"expense","name":"food","amount":2000},
        {"type":"income","name":"Trading","amount":15000},
        {"type":"expense","name":"Travel","amount":1000}
    ]

    import json

    with open(file_path,"w") as file:
        json.dump(transactions,file)
    with open(file_path,"r") as file:
        loaded_data = json.load(file)

        assert loaded_data == transactions
        assert loaded_data[0]["amount"] == 25000
        assert loaded_data[1]["amount"] == 2000