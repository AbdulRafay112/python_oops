# here is a has a relation ship between professor and department , department has own professor 
class Professor:
    def __init__(self , name):
        self.name = name 
    def __str__(self):
        return self.name 
class Department:
    def __init__(self , dept_name):
        self.dept_name = dept_name 
        self.professors = []
    def add_professor(self , professor):
        self.professors.append(professor)
    def __str__(self):
        list =  [prof for prof in self.professors]
        return str(list) 
    
ubit = Department("ubit")
ubit.add_professor("jamshed aziz")
print(ubit)

# aggregation example 2 === 
class Product:
    def __init__(self , product_name , price):
        self.product_name = product_name 
        self.price = price 
    def __str__(self):
        return f"product_name: {self.product_name} , product_price: {self.price}"
class OrderItem:
    def __init__(self , product , quantity):
        self.product = product 
        self.quantity = quantity 
    def get_total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return f"product: {self.product} , quantity: {self.quantity} , total = {self.get_total()}"
    def __repr__(self):
        return f"product: {self.product} , quanitity: {self.quantity} , total = {self.get_total()}"
    
class Order:
    def __init__(self , order_id):
        self.order_id = order_id
        self.items = []
    def add_item(self , order_item):
        self.items.append(order_item)
    def calculate_total(self):
        return sum(item.get_total() for item in self.items)
    def __str__(self):
        return f"order_id: {self.order_id} has total is {self.calculate_total()}"
    
p1 = Product("Ricoh" , 1800)
order_item = OrderItem(p1 , 4)
order_1 = Order(12345)
order_1.add_item(order_item)
p2 = Product("Xerox" , 400)
order_item_2 = OrderItem(p2 , 3)
order_2 = Order(45678)
order_2.add_item(order_item_2)
print(p1)
print(order_item)
print(order_1)
