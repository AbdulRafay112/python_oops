from Range import Range 
if __name__ == "__main__":
    try:
        r1 = Range(4 , 10 , 2)
        r2 = range(4 , 10 ,2)
        r4 = Range(r2)
        r3 = range(r2)
        print(r3)
    
    except Exception as e:
        print(e)

        