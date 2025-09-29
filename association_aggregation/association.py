class Teacher:
    def __init__(self , name):
        self.name = name 
    def teach(self):
        return f"{self.name} is teaching! "
    def __str__(self):
        return self.name
class Student:
    def __init__(self , name):
        self.name = name 
    def learn(self , teacher: Teacher):
        return f"{self.name} is learning from {teacher}"

t1 = Teacher("Zeeshan usmani ")
s1 = Student("Rafay")
print(s1.learn(t1))
s2 = Student("moiz")
print(s2.learn(t1))

## association example 2 very very goood 
class PaymentGateway:
    def __init__(self , name):
        self.name = name 
    def process_payment(self , amount):
        return f"payment of {amount} has processed via {self.name}"
class Customer:
    def __init__(self , name):
        self.name = name 
    def make_payment(self , amount , gateway):
        print(f"{self.name} wants to pay {amount}")
        print(gateway.process_payment(amount))
paypal = PaymentGateway("paypal")
lady_bug = Customer("lady bug")
lady_bug.make_payment("1000" , paypal)        
