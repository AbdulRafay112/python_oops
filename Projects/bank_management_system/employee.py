from branch import Branch
class Employee:
    """Employee of the bank"""
    def __init__(self , name , employee_id , role , salary , branch):
        self.name = name 
        self.employee_id = employee_id
        self.role = role 
        self.__salary = salary 
        self.branch = branch  
    @property
    def salary(self):
        return self.__salary
    @salary.setter 
    def salary(self , new_salary):
        self.__salary = new_salary 
    def assign_branch(self , new_branch):
        """Assign employee a new branch"""
        if isinstance(new_branch , Branch):
            self.branch = new_branch
        else:
            raise TypeError("new branch must be of Branch type")
    def change_salary(self , new_salary):
        self.salary = new_salary # calling setter 
    def __str__(self):
        return (
            f"Employee Name : {self.name}\n"
            f"ID            : {self.employee_id}\n"
            f"Role          : {self.role}\n"
            f"Salary        : {self.salary}\n"
            f"Branch        : {self.branch}\n"
    )
    def __repr__(self):
          return (
            f"Employee Name : {self.name}\n"
            f"ID            : {self.employee_id}\n"
            f"Role          : {self.role}\n"
            f"Salary        : {self.salary}\n"
            f"Branch        : {self.branch}\n"
    )
