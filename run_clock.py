import time 
import os

def get_time():
    stop = False
    while stop == False:
        print("Time:",time.strftime('%H:%M:%S'))
        time.sleep(1)
        os.system('clear')
        

get_time()