import time
import random
import guessanumber
import calculator

r = random.randint(1,10)
OPC = None
Playing = 1


def loading(N1,N2):
  ss = 0
  print("loading...")
  r = random.randint(N1,N2)
  while ss != r:
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    ss = ss + 1

input()
print("booting up...")
time.sleep(1)
loading(1,10)
r = random.randint(1,5)
if r == 1:
 print("Failed")
 time.sleep(1)
 print("retrying")
 time.sleep(0.5)
 loading(1,10)
 print("Succsess")
else:
    print("Succsess")
print('type "help" to find out what to do')
while Playing == 1:
 OPC = input("|>>>")
 if OPC == "help":
     print("G = Games")
     print("M = Calculator")
     print("P = print message")
     print("S = Settings")
     print("A = Account settings")
     print("Q = Quit")
     print("any others will be invalid")
 elif OPC == "G":
     print("1.pick a number")
     time.sleep(0.5)
     print(" ")
     time.sleep(0.5)
     print("2.")
     time.sleep(0.5)
     print(" ")
     time.sleep(0.5)
     print("3.")
    #looking for some simple text game ideas
     OPC = input("which one >>")
     if OPC == "1":
         loading(1,2)
         guessanumber.GAN()
     elif OPC == "2":
         loading(1,5)
         print("In progress...")
     elif OPC == "3":
         print(" ")
 elif OPC == "M":
     calculator.CAL()
