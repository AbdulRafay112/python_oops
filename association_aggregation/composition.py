class Engine:
    def __init__(self , model):
        self.model = model 
class Car:
    def __init__(self , name):
        self.name = name 
        self.engine = Engine("toyota_engine") # car has own engine 