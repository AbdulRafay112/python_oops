class Branch:
    """branch of the bank"""
    def __init__(self , branch_name , branch_location):
        self.branch_name = branch_name 
        self.branch_location = branch_location 
        self.employees = [] 
        self.customers = []  
        self.accounts = []   
    def add_account(self , new_account):
        """Add new account in the branch"""
        self.accounts.append(new_account)
    def add_customer(self , new_customer):
        """add new customer in the branch"""
        self.customers.append(new_customer) 
    def add_employee(self , new_employee):
        """add new employee in the branch"""
        self.employees.append(new_employee)
    def show_customers(self):
        """show all customers in the branch"""
        return [customer for customer in self.customers]
    def show_employee(self):
        """show employees in the branch"""
        return [employee for employee in self.employees]
    def show_account(self):
        """show accounts in that particular branch"""
        return [account for account in self.accounts]
    def __str__(self):
        return (
            f"Branch Name : {self.branch_name}\n"
            f"Location    : {self.branch_location}\n"
            f"Employees   : {len(self.employees)}\n"
            f"Customers   : {len(self.customers)}\n"
            f"Accounts    : {len(self.accounts)}\n"
        )
    def __repr__(self):
          return (
            f"Branch Name : {self.branch_name}\n"
            f"Location    : {self.branch_location}\n"
            f"Employees   : {len(self.employees)}\n"
            f"Customers   : {len(self.customers)}\n"
            f"Accounts    : {len(self.accounts)}\n"
        )





