from datetime import datetime

wallets = {1: 1000, 2: 500}
transactions = []

def get_balance(user_id):
    return wallets.get(user_id, 0)

def add_money(user_id, amount):
    if user_id not in wallets or amount <= 0:
        print("Invalid request")
        return

    wallets[user_id] += amount
    transactions.append({
        "type": "ADD",
        "user": user_id,
        "amount": amount,
        "time": str(datetime.now())
    })
    print("Money added successfully")

def transfer(sender, receiver, amount):
    if sender not in wallets or receiver not in wallets:
        print("Wallet not found")
    elif sender == receiver or amount <= 0:
        print("Invalid transfer")
    elif wallets[sender] < amount:
        print("Insufficient balance")
    else:
        wallets[sender] -= amount
        wallets[receiver] += amount

        transactions.append({
            "type": "TRANSFER",
            "from": sender,
            "to": receiver,
            "amount": amount,
            "time": str(datetime.now())
        })
        print("Transfer successful")

def transaction_history():
    for transaction in transactions:
        print(transaction)

# Main program
print("Initial balance:", get_balance(1))
add_money(1, 500)
transfer(1, 2, 300)

print("Sender balance:", get_balance(1))
print("Receiver balance:", get_balance(2))

print("Transaction History:")
transaction_history()