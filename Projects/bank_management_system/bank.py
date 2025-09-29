class Bank:
    """simple bank class"""
    def __init__(self , bank_name):
        self.bank_name = bank_name 
        self.branches = []
    def add_branch(self , new_branch):
        """Add new branch to the bank branches list """
        self.branches.append(new_branch) # aggregation -> bank has contain branches  
    def show_all_branches(self):
        """show all branches of the bank"""
        return [branch for branch in self.branches]
    def __str__(self):
        """String representation of the bank class"""
        return f"{self.bank_name} has branches: {self.show_all_branches()}"