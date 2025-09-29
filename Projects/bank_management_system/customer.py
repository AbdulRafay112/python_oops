class Customer:
    """customer of the bank"""
    def __init__(self , customer_id , name , address , email , password):
        self.customer_id = customer_id 
        self.name = name 
        self.address = address 
        self.email = email 
        self.accounts = []  # composition relation if customer object destroyed account objects should be destroyed 
        self.__password = password
    @property 
    def password(self):
        """getter for password"""
        return self.__password
    def add_account(self , new_account):
        """add new account to customer accounts"""
        self.accounts.append(new_account) 
    def show_accounts(self):
        """Show all accounts list of customer"""
        return [account for account in self.accounts]
    def __str__(self):
        return (
        f"customer_name:{self.name}, "
        f"customer_id:{self.customer_id}, "
        f"customer_address: {self.address}, "
        f"email= {self.email}, "
        f"customer accounts = {self.show_accounts()}"
    )
    def __repr__(self):
          return (
        f"customer_name:{self.name}, "
        f"customer_id:{self.customer_id}, "
        f"customer_address: {self.address}, "
        f"email= {self.email}, "
        f"customer accounts = {self.show_accounts()}"
    )
