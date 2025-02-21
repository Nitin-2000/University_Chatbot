import aiml
from os import system as s

kernel = aiml.Kernel()
kernel.learn("D:/aiip1/botdata/standard/*.aiml")
s("cls")
while 1:
     print(kernel.respond (input("Message-> ")))