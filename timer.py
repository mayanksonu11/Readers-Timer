import time
from tkinter import *
from tkinter import messagebox
import threading
from playsound import playsound
from tkinter import simpledialog

timer=""
def digitalclock():
   label2.config(text=timer)
   label2.after(200, digitalclock)
   

def showMessage(msg,t):
   top = Toplevel()
   top.title('Info')
   Message(top, text=msg,font=("Courier", 12, 'bold'),bg="silver", padx=20, pady=20,bd =10).pack()
   top.after(t, top.destroy)


def countdown(t,f):
   if t<0:
      messagebox.showinfo("Info","End of the game!!")
      t = 0
   p = time.localtime()
   current_time = time.strftime("%H:%M:%S", p)
   print(current_time)
   global timer
   while t: 
      mins, secs = divmod(t, 60) 
      timer = '{:02d}:{:02d}'.format(mins, secs) 
      print(timer, end="\r")
      time.sleep(1) 
      t -= 1
   if f==1:
      playsound('1.wav')
   else:
      playsound('2.wav')

def caller(t):
   k =0
   brk = 60
   while 1: 
    #thread banana hai and global flag set karna hai 
      global flag_info
      countdown(k*120+int(t),1) 
      print("Giving you break of 1 minute")
      showMessage("1 minute break",brk*1000)
      countdown(brk,0)
      # c = input("Could you remain focused in last session? (y/n) ")
      c = messagebox.askyesnocancel("Alert", "Could you remain focused in last session?")
      print(c)
      if c=="yes" or c==True:
         print("Congrats you did well in last session I am taking you to next level time slab...")
         showMessage("Congrats you did well in last session",5000)
         k=k+1
      elif c=='no' or c==False:
         print("Decreasing your time slab!!")
         showMessage("Sad, you didn't concentrate",5000)
         # messagebox.showinfo("Info", "Sad, you didn't concentrate")
         k=k-1
      else:
         print("Keeping the timeslab constant!!")
         showMessage("Ok will keep it same!!",5000)


master = Tk()
master.title("Digital Clock")
master.resizable(1,1)
t = simpledialog.askinteger("Input", "Please enter time (in seconds) ",parent=master)
threads = list()
x = threading.Thread(target=caller,args=(t,))
threads.append(x)
x.start()

label2 = Label(master, font=("Courier", 45, 'bold'), bg="blue", fg="white",bd=20)
label2.pack()


digitalclock()
master.mainloop()

# print("Mayank")
