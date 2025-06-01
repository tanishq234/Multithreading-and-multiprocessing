##multithreading 
##when to use multithreading
##I/O=bound task:Tasks that spends more time watching for i/o operation (e.g. file operations,network request)
##concurrent execution:when you want to improve throughput of your application by performing multiple operation concurrently

import threading
import time

def print_numbers():
    for i in range (5):
        time.sleep(2)
        print(f"Numbers:{i}")
        
def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")
        
##create two threads

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t=time.time()

##start the thread
t1.start()
t2.start()

#wait fro thread to complete

t1.join()
t2.join()

#print_numbers()
#print_letters()
finished_time=time.time()-t
print(finished_time)
        
                
        