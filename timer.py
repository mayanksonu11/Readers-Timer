# import the time module
import os 
import time
from playsound import playsound
  
def countdown(t): 
    if t<=0:
        print("You have lost the game!")
    p = time.localtime()
    current_time = time.strftime("%H:%M:%S", p)
    print(current_time)
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    playsound('1.wav')

t = input("Welcome to the readers challenge game. Please enter the initial time in seconds: ")
k =0
while 1: 
    countdown(k*120+int(t)) 
    print("Giving you break of 1 minutes")
    countdown(60)
    c = input("Could you remain focused in last session? (y/n) ")
    if c=='Y' or c=='y':
        k=k+1
    else:
        print("Decreasing your time slab!!")
        k=k-1
