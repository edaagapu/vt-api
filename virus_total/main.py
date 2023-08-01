

# import threading
# import time
# from random import randint

# NTHREADS=6
# def hilo(i):
#   print(f"[+] En hilo {i}")
#   t = randint(3,9)
#   print(f'Hilo {i}: Tiene un tiempo de dormido de: {t}')
#   time.sleep(t) 
#   print(f"[-] hilo {i} finalizado") 

# simplethread=[] 
# for i in range(NTHREADS):
#   simplethread.append(threading.Thread(target=hilo, args=[i+1])) 
#   simplethread[-1].start() 
# for i in range(NTHREADS):
#   simplethread[i].join() 

# importing only those functions
# which are needed
from tkinter import * 
from tkinter.ttk import *
from gui.components import TestButton
  
# creating tkinter window
root = Tk()
  
# Adding widgets to the root window
Label(root, text = 'GeeksforGeeks', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)
  
# Creating a photoimage object to use image
photo = PhotoImage(file = r"C:\Users\cb00244\Documents\Repositorios\API_VT\virus_total\gui\icons\logout.png")
frame = Frame(root).pack(side=TOP, pady=10)
  
# Resizing image to fit on button
photoimage = photo.subsample(10, 10)
  
# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button
TestButton(root, text='Click Me', image='logout.png').pack(side=TOP, pady=10)
  
mainloop()



if __name__ == '__main__':
  print('Hello!')