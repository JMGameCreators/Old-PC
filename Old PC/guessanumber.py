import random

def GAN():

    N1 = 1
    N2 = 1
    G = 1
    P = 1
    N = 1
    PA = 1

    while P == 1:
        N1 = input("Enter your first number >>")
        N2 = input("Enter your second number >>")
        #N = random.randint(1,15)
        N = random.randint(int(N1),int(N2))
        G = input("First guess >>")
        if int(G) == N:
            print("Correct!")
        else:
            print("wrong, try again")
            if N > int(G):
                print("Higher")
            else:
                print("Lower")
            G = input("Second guess >>")
            if int(G) == N:
                print("Correct!")
            else:
                print("wrong, last try")
                if N > int(G):
                 print("Higher")
                else:
                 print("Lower")
                G = input("Third & Final guess >>")
                if int(G) == N:
                    print("Correct!")
                else:
                    print("sorry you got it wrong, the number was",N)
        PA = input("do you want to play again(Y/N) >>")
        if PA == "Y":
            print("okay continuing")
        elif PA == "y":
            print("okay continuing")
        else:
            print("okay then")
            P = 0
