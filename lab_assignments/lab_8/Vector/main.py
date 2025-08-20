from Vector import Vector 

if __name__ == "__main__":
    try:
        # implement default constructor case
        v1 = Vector()
        #implement parameterized constructor case 
        v2 = Vector(3)
        #implement copy constructor case 
        v3 = Vector(v1)
        # implement __setitem__ dunder method 
        j = 1 
        for i in range(3):
            v1[i] = 1 * j  
            v2[i] = 2 * j  
            v3[i] = 3 * j 
            j+=2
        # implement __getitem__ dunder method 
        print(v3[2])
        # implement addition __add__ of two vectors 
        v4 = v1 + v2
        # implement substraction
        v10 = v1 - v2 
        # implement __eq__ method 
        print(v4 == v2)
        # implement __ne__ method 
        print(v4 != v2)

    except Exception as e :
        print(e)

