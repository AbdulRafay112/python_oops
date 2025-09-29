from datetime import datetime
from bank import Bank
from branch import Branch 
from customer import Customer 
from account import Account
from employee import Employee
from transaction import Transaction
def main():
    # === ubl ===
    branch_1 = Branch("main branch" , "saddar")
    branch_2 = Branch("karimabad branch" , "karimabad")
    ubl = Bank("ubl")
    ubl.add_branch(branch_1)
    ubl.add_branch(branch_2)
    rafay_customer = Customer(39393 , "rafay" , "R9383 sharifabad" , "rafayrafay922@gmail.com" , "dkdihdi")
    branch_1.add_customer(rafay_customer)
    rafay_current_Account = Account(93833 , 3838883 , "current" , "rafay")
    rafay_saving_account = Account(9384884 , 39932 , "saving" , "rafay")
    branch_1.add_account(rafay_current_Account)
    branch_1.add_account(rafay_saving_account)
    rafay_customer.add_account(rafay_current_Account)
    rafay_customer.add_account(rafay_saving_account)

    # === meezan bank ===
    meezan = Bank("Meezan")
    meezan_branch_1 = Branch("Main" , "sharifabad")
    meezan.add_branch(meezan_branch_1)
    meezan_branch_2 = Branch("waterpump" , "waterpump")
    meezan.add_branch(meezan_branch_2)
    customer_1 = Customer("293883" , "Faheem" , "Liaqatabad" , "faheem@gmail.com" , "83838")
    customer_1_current_account = Account("9499494" , 948488 , "current" , "Faheem")
    customer_1_saving_account = Account("3993939" , '29283' , "saving" , "Faheem")
    customer_1.add_account(customer_1_current_account)
    customer_1.add_account(customer_1_saving_account)
    meezan_branch_1.add_account(customer_1_saving_account)
    meezan_branch_1.add_account(customer_1_current_account)
    meezan_branch_1.add_customer(customer_1)
    print(meezan)
    


    

if __name__== "__main__":
    main()


