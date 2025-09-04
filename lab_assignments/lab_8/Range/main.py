from Range import Range 
if __name__ == "__main__":
    try:
        r1 = Range(4 , 10 , 2)
        r2 = range(4 , 10 ,2)
        for i in r1:
            print(i)
        print("-" * 23)
        for i in r2:
            print(i)
    
    except Exception as e:
        print(e)