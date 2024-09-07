import hashlib
from colorama import Fore, Style
import pandas as pd

transactionId = 0
blocks = []
currentTransactions = []
transactions = []
wallets = [
    {
        "name": "Juan",
        "amount": 100,
        "lastTransaction": None
    },
    {
        "name": "Esteban",
        "amount": 100,
        "lastTransaction": None
    },
    {
        "name": "Pedro",
        "amount": 100,
        "lastTransaction": None
    },
    {
        "name": "Maria",
        "amount": 100,
        "lastTransaction": None
    }
]

# Function to calculate the hash of a data
def get_hash(dato):
    return hashlib.sha256(dato.encode()).hexdigest()

#Function to build the merkle tree
def build_merkle_tree(info):

    #Get the hash for each leave
    leaves = [get_hash(str(data["id"]) +
                           data["from"] + 
                           data["to"] + 
                           str(data["amount"]) + 
                           data["refundTo"]) for data in info]

    # Build the tree recursively
    while len(leaves) > 1:

        # In case the amount of leaves is odd, the last leave will be duplicated
        if len(leaves) % 2 != 0:
            leaves.append(leaves[-1])

        # Group the hashes in pairs and get the new hash
        leaves = [get_hash(leaves[i] + leaves[i+1]) for i in range(0, len(leaves), 2)]

    # return the root of the tree
    return leaves[0]

#Mine the block
def mintBlock(data, min):
    root_hash = build_merkle_tree(data)
    nonce = 0

    #If there are no blocks, the previous hash will be a hash of zeros (0)
    if len(blocks) == 0:
        previous_hash = get_hash("0" * 64)
    else:
        previous_hash = blocks[-1]["hash"]

    # Get the hash for the whole block
    new_block_hash = get_hash(root_hash + str(nonce) + previous_hash)

    amount_zeros = "0" * min

    #Find the nonce that makes the hash of the block to have the required amount of zeros
    while(new_block_hash[:min] != amount_zeros):
        nonce +=1
        new_block_hash = get_hash(root_hash + str(nonce) + previous_hash)

    #Build the block
    new_blolck = {
        "root_hash": root_hash,
        "nounce": nonce,
        "previous_hash": previous_hash,
    }

    blocks.append({
        "block": new_blolck,
        "hash": new_block_hash
    })
    
    #Save the list of transactions for the block
    transactions.append(data)
    currentTransactions.clear()

    print(Fore.GREEN + "\nBlock succesfully mint\n"+ Style.RESET_ALL)

def checkTransaction(data):
    
    global transactionId
    
    #Search the wallet of the sender
    sender = next((wallet for wallet in wallets if wallet["name"].lower() == data["from"].lower()), None)
    if sender is None:
        print(Fore.RED + "\nSender not found\n" + Style.RESET_ALL)
        return

    if sender["amount"] < data["amount"]:
        print(Fore.RED + "\nInsufficient funds\n" + Style.RESET_ALL)
        return
    
    #Search the wallet of the receiver
    receiver = next((wallet for wallet in wallets if wallet["name"].lower() == data["to"].lower()), None)
    if receiver is None:
        print(Fore.RED + "\nReceiver not found\n" + Style.RESET_ALL)
        return
    
    #Update the amount of the sender and receiver in the wallet
    for wallet in wallets:
        if wallet["name"].lower() == data["from"].lower():
            wallet["amount"] -= data["amount"]
            wallet["lastTransaction"] = data["id"] + 1
        elif wallet["name"].lower() == data["to"].lower():
            wallet["amount"] += data["amount"]
            wallet["lastTransaction"] = data["id"] + 1
    
    #Add the transaction to the list
    currentTransactions.append(data)
    
    transactionId += 1
    
    print(Fore.GREEN + "\nTransaction completed successfully\n" + Style.RESET_ALL)

#Print the Blockchain
def print_network():
    # Create a list to store the data of each block
    data = []

    if(len(blocks) == 0):
      print(Fore.RED + "\nFirst a block should be mint\n" + Style.RESET_ALL)
      return

    for i, block_data in enumerate(blocks):
        block = block_data["block"]
        data.append({
            "Nonce": block["nounce"],
            "Root Hash": block["root_hash"],
            "Previous Hash": block["previous_hash"],
            "Hash": block_data["hash"]
        })

    # Create a DataFrame from the list of data
    df = pd.DataFrame(data)

    # Display the Dataframe
    display(df)

#Print the wallets
def print_wallets():

  wallets_df = pd.DataFrame(wallets)
  display(wallets_df)

#Menu for the user to add transactions
def menu():
    while True:
        print("1. Add transaction")
        print("2. Mine block")
        print("3. Print blockchain")
        print("4. Print wallets")
        print("5. Exit")
        option = input("Choose an option: ")
        if option == "1":
            sender = input("Enter the sender: ")
            receiver = input("Enter the receiver: ")
            amount = int(input("Enter the amount: "))
            data = {
                "id": transactionId,
                "from": sender,
                "to": receiver,
                "refundTo": sender,
                "amount": amount
            }
            checkTransaction(data)
        elif option == "2":
            difficulty = int(input("Enter the difficulty: "))
            if(len(currentTransactions) == 0):
              print(Fore.RED + "\nThere must be at least one transaction to mine the block\n" + Style.RESET_ALL)
            else:
              mintBlock(currentTransactions, difficulty)
        elif option == "3":
            print_network()
        elif option == "4":
            print_wallets()
        elif option == "5":
            break
        else:
            print("Invalid option")

#Execute the app
menu()