import time
import random

r = random.randint(1,10)
OPC = None
Playing = 1


def loading():
  ss = 0
  print("loading...")
  r = random.randint(1,10)
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
loading()
r = random.randint(1,5)
if r == 1:
 print("Failed")
 time.sleep(1)
 print("retrying")
 time.sleep(0.5)
 loading()
 print("Succsess")
else:
    print("Succsess")
print('type "help" to find out what to do')
while Playing == 1:
 OPC = input("|>>>")
 if OPC == "help":
     print("FP = Enter Floppy Disc")
     print("M = Calculator")
     print("P = print message")
     print("S = Settings")
     print("A = Account settings")
     print("Q = Quit")
     print("any others will not be invalid")
 elif OPC == "FP":
     print("1.pick a number")
     time.sleep(0.5)
     print(" ")
     time.sleep(0.5)
     print("2.tick tack toe")
     time.sleep(0.5)
     print(" ")
     time.sleep(0.5)
     print("3.BlackJack")
     OPC = input("which one >>")
     if OPC == "1":


