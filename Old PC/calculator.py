def CAL():
    import math

    O = 1
    N1 = 1
    N2 = 1
    A = 1

    print("addition = A")
    print("subtraction = S")
    print("multiplication = M")
    print("division = D")
    O = input("which math symbol>>>")
    if O == "A":
        N1 = input("N1>>>")
        N2 = input("N2>>>")
        print(N1,"+",N2,"=")
        A = int(N1) + int(N2)
        print(A)
    elif O == "S":
        N1 = input("N1>>>")
        N2 = input("N2>>>")
        print(N1,"-",N2,"=")
        A = int(N1) - int(N2)
        print(A)
    elif O == "M":
        N1 = input("N1>>>")
        N2 = input("N2>>>")
        print(N1,"×",N2,"=")
        A = int(N1) * int(N2)
        print(A)
    elif O == "D":
        N1 = input("N1>>>")
        N2 = input("N2>>>")
        print(N1,"÷",N2,"=")
        A = int(N1) // int(N2)
        print(A)
    else:
        print("invalid")