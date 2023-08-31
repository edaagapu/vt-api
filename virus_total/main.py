

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
from gui import App
from facade import ExcelFacade

if __name__ == '__main__':
  app = App(facade=ExcelFacade())
  app.mainloop()