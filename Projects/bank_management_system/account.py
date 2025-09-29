class Account:
    """Account of the customer of the bank"""
    def __init__(self , account_number , balance , account_type , customer_name):
        self.customer_name = customer_name 
        self.account_number = account_number 
        self.balance = balance 
        self.account_type = account_type
        self.transactions = [] # transaction is composed from account 
    def deposit(self , amount):
        """method for deposit money in the account"""
        self.balance += amount
    def with_draw(self , amount):
        """Method for withdrawing from an account"""
        if amount <= self.balance:
            self.balance -= amount 
        else:
            raise ValueError("amount must be less than aur equal to balance")
    def process_transaction(self , transaction):
        """pass transaction class instance here"""
        self.transactions.append(transaction)
        if transaction.transaction_type == "deposit":
            self.deposit(transaction.amount)
        elif transaction.transaction_type == "withdraw":
            self.with_draw(transaction.amount)
        else:
            raise ValueError("choose deposit or withdraw | invalid transaction type")

    def __str__(self):
        """String representation of an account"""
        return (
            f"Account Holder : {self.customer_name}\n"
            f"Account Number : {self.account_number}\n"
            f"Account Type   : {self.account_type}\n"
            f"Balance        : {self.balance}\n"
        )
    
    def __repr__(self):
          return (
            f"Account Holder : {self.customer_name}\n"
            f"Account Number : {self.account_number}\n"
            f"Account Type   : {self.account_type}\n"
            f"Balance        : {self.balance}\n"
        )
