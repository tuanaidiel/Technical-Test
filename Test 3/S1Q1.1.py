def pyramid(n, order):
    for i in range(n, 0, -1):  
        for j in range(i):  
            print("*", end=" ")
        print()  

pyramid(5, "desc")
