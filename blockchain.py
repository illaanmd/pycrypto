'''simple blockchain transaction menu and blockchain integrity checker'''
MINING_REWARD = 15000
GENESIS_BLOCK = {"previous_hash": "", "index": 0, "transactions": []}
blockchain = [GENESIS_BLOCK]
open_transactions = []
owner = "owner1"
participants = {"owner1"}


def get_last_blockchain_value():
    '''returns blockchain last value'''
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1000):
    '''adds a new value to the blockchain

    Arguments:
        sender: The sender wallet address
        recipient: The recipient wallet address
        amount: transaction amount default = 10000
    '''
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
        }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def hash_block(block):
    '''gets the hash for the last block'''
    return "-".join(str([block[key] for key in block]))


def mine_block():
    '''hashes a block and appends it to the
     blockchain with the new transactions'''
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {"sender": "BLOCK_REWARD",
                          "recipient": owner,
                          "amount": MINING_REWARD
                          }
    open_transactions.append(reward_transaction)
    block = {"previous_hash": hashed_block,
             "index": len(blockchain),
             "transactions": open_transactions
            }
    blockchain.append(block)
    return True


def get_balance(participant):
    transaction_sender = [[tx["amount"] for tx in block["transactions"] if
                           tx["sender"] == participant] for block in blockchain]
    open_tx_sender = [tx["amount"] for tx in open_transactions if tx["sender"] == participant]
    transaction_sender.append(open_tx_sender) 
    amount_sent = 0
    for transaction in transaction_sender:
        if len(transaction) > 0:
            amount_sent += transaction[0]
    return amount_sent


def verify_transaction(transaction):
    sender_balance = get_balance(transaction["sender"])
    return sender_balance >= transaction["amount"]


def get_transaction_value():
    '''return user input as a tuple containing the transaction info'''
    transaction_recipient = input("Enter the recipient address:  ")
    transaction_amount = int(input("enter the transaction amount:  "))
    return (transaction_recipient, transaction_amount)


def verify_blockchain():
    '''verifies the blockchain'''
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True


def choose_option():
    '''select input option for the while loop'''
    user_input = input("Option:  ")
    return user_input

def print_blockchain():
    '''prints the full blockchain'''
    for block in blockchain:
        print(block)


get_last_blockchain_value()

expecting_input = True

while expecting_input:
    print("enter order")
    print("1: Add a new transaction value")
    print("2: Output blockchain")
    print("3: Mine a new block")
    print("4: Output participants")
    print("q: Quit")
    user_choice = choose_option()
    if user_choice == "1":
        transaction_data = get_transaction_value()
        recipient, amount = transaction_data
        if add_transaction(recipient, amount=amount):
            print("Added transaction")
        else:
            print("Transaction failed")
        print(open_transactions)
    elif user_choice == "2":
        print_blockchain()
    elif user_choice == "3":
        if mine_block():
            open_transactions = []
    elif user_choice == "4":
        print(participants)
    elif user_choice == "q":
        expecting_input = False
    else:
        print("Invalid input. pick a value from the list, please")
    if not verify_blockchain():
        print("Invalid blockchain")
        break
    print(get_balance("owner1"))
