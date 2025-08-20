from Range import Range 
if __name__ == "__main__":
    try:
        # implement default constructor logic 
        r1 = Range(5)
        # implement copy constructor logic
        r2 = Range(r1)
        # implementing parameterized constructor case 
        r3 = Range(3 , 10 , 4)
        # implementing the __getitem__ dunder method 
        print(r2[4])
        # implementing the __len__ method 
        print(len(r3))
    except Exception as e :
        print(e)




