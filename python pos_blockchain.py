import hashlib
import random

class Block:
    def __init__(self, index, previous_hash, transactions, stake_amount):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.stake_amount = stake_amount
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.previous_hash) + str(self.transactions) + str(self.stake_amount)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.validators = {}
        self.transactions = []

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", 0)

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def add_validator(self, validator, stake):
        self.validators[validator] = stake

    def select_validator(self):
        total_stake = sum(self.validators.values())
        r = random.uniform(0, total_stake)
        current = 0
        for validator, stake in self.validators.items():
            current += stake
            if current >= r:
                return validator

    def create_block(self, validator):
        previous_block = self.get_last_block()
        new_block = Block(
            len(self.chain),
            previous_block.hash,
            self.transactions,
            self.validators[validator]
        )
        self.chain.append(new_block)
        self.transactions = []
        return new_block

# Example usage:

blockchain = Blockchain()



# Adding validators with stakes
blockchain.add_validator("Validator_1", 10)
blockchain.add_validator("Validator_2", 40)
blockchain.add_validator("Validator_3", 20)

# Adding a transaction
blockchain.add_transaction("Transaction_1")

# Selecting a validator based on PoS
selected_validator = blockchain.select_validator()
print(f"Selected Validator: {selected_validator}")

# Creating a new block
new_block = blockchain.create_block(selected_validator)
print(f"New Block Hash: {new_block.hash}")
