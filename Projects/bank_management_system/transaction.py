class Transaction:
    def __init__(self , transaction_id , amount , account , transaction_type , date_time):
        self.transaction_id = transaction_id
        self.amount = amount 
        self.account = account 
        self.transaction_type = transaction_type
        self.date_time = date_time
        
    def __str__(self):
        return (
            f"Transaction ID   : {self.transaction_id}\n"
            f"Amount           : {self.amount}\n"
            f"Type             : {self.transaction_type}\n"
            f"Account Number   : {self.account.account_number}\n"
            f"Transaction Time : {self.date_time}\n"
        )
