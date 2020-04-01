'''simple blockchain transaction menu and blockchain integrity checker'''

blockchain = []

def get_last_value():
    '''returns blockchain last value'''
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_value, last_value=[0]):
    '''adds a new value to the blockchain'''
    if last_value is None:
        last_value = [0]
    blockchain.append([last_value, transaction_value])


def add_first_value():
    '''add the FIRST value to the blockchain'''
    first_value = int(input("Enter first value:  "))
    add_value(first_value)


def verify_blockchain():
    '''verifies the blockchain'''
    block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index = block_index + 1
    return is_valid


def add_transaction_value():
    '''add a transaction to the blockchain'''
    transaction_value = int(input("Enter transaction amount:  "))
    add_value(transaction_value, get_last_value())


def choose_option():
    '''select input option for the while loop'''
    user_input = input("Option:  ")
    return user_input

def print_blockchain():
    '''prints the full blockchain'''
    for block in blockchain:
        print(block)


add_first_value()

expecting_input = True

while expecting_input:
    print("enter order")
    print("1: Add a new transaction value")
    print("2: Output blockchain")
    print("q: Quit")
    user_choice = choose_option()
    if user_choice == "1":
        add_transaction_value()
    elif user_choice == "2":
        print_blockchain()
    elif user_choice == "q":
        expecting_input = False
    else:
        print("Invalod input. pick a value from the list, please")
    if not verify_blockchain():
        print("Invalid blockchain")
        break
