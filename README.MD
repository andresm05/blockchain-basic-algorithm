# Blockchain Representation Program

## Purpose

This program simulates the core functionalities of a blockchain system. It allows you to create and manage transactions, mine blocks with a specified difficulty, and view the current state of the blockchain, transactions and wallets. The blockchain is represented using a Merkle tree to ensure data integrity and security.

## Features

- **Transaction Management**: Add transactions between different wallets.
- **Block Mining**: Mine new blocks with a customizable difficulty level.
- **Blockchain Display**: Print the current state of the blockchain, including details of each block.
- **Wallet Management**: View the balances and transaction history of each wallet.
-**Transactions Managment**: View transaction history in the Blockchain.

## Requirements

- Python 3.x
- `pandas` library
- `colorama` library

You can install the required libraries using:
```bash
pip install pandas colorama
```

## Run the Program

To run the program, follow these steps:

1. **Open the Colab Notebook**: Click on the [link](https://colab.research.google.com/drive/13J038qaUhUEiwaop6-0PwM8aZ_UFgMxE?usp=sharing) to open the notebook in Google Colab.
2. **Execute Cells**: Run each cell in the notebook sequentially. This will set up the blockchain environment and make the program ready for interaction.
3. **Interact with the Program**: Once the setup is complete, you can start using the program by following the menu options provided.

## Menu Options

After starting the program, you will be presented with a menu with the following options:

1. **Add Transaction**: 
   - **Description**: Add a new transaction to the blockchain.
   - **Inputs Required**: Sender's name, receiver's name, and the amount to be transferred.

2. **Mine Block**: 
   - **Description**: Mine a new block with the pending transactions.
   - **Inputs Required**: Mining difficulty, which determines the number of leading zeros required in the block hash.

3. **Print Blockchain**: 
   - **Description**: Display the details of each block in the blockchain.
   - **Details Shown**: Nonce, root hash, previous hash, and block hash.

4. **Print Wallets**: 
   - **Description**: Show the current state of each wallet.
   - **Details Shown**: Wallet name, balance, and last transaction ID.

5. **Print Transactions**:
   - **Description**: Show transactions that have been added to the Blockchain, along with the corresponding block in which each transaction is stored.
   - **Details Shown**: id, from, to, refundTo, amount, block.

6. **Exit**: 
   - **Description**: Exit the program.

## Code Overview

- **Hash Calculation**: `get_hash(dato)` calculates the SHA-256 hash of the input data.
- **Merkle Tree Construction**: `build_merkle_tree(info)` constructs a Merkle tree to summarize the transactions in a block.
- **Block Mining**: `mintBlock(data, min)` mines a new block by finding a nonce that meets the difficulty requirement.
- **Transaction Checking**: `checkTransaction(data)` verifies and processes a transaction, updating the relevant wallets.
- **Printing Information**: `print_network()`, `print_wallets()` and `print_transactions()` display the blockchain, wallet and transactions information respectively.

## Example Usage

- **Adding a Transaction**:
  - **Input**: Sender: Juan, Receiver: Esteban, Amount: 10
  - **Output**: Transaction completed successfully.

- **Mining a Block**:
  - **Input**: Difficulty: 2
  - **Output**: Block successfully mined.

-**Printing transactions**
   -**Output**: Displays all transactions that have been added to the Blockchain so far.

- **Printing Blockchain**:
  - **Output**: Displays the details of each block.

- **Printing Wallets**:
  - **Output**: Displays the current state of all wallets.
