#process that runs in parallel
### whem to use 
#cpu bound task:tasks that are heavy on cpu usage(e.g. matheamtical computation,datav processing,)
#parallel execution- multiple cores of the cpu

import multiprocessing 
import multiprocessing.process
import time
def squared_numbers():
    for i in range (5):
        time.sleep(1)
        print(f"square:{i*i}")
        

def cube_numbers():
    for i in range (5):
        time.sleep(1.5)
        print(f"cube:{i*i*i}")
        
        
if__name___=="__main__":
    
    
    #create two process
    
    p1=multiprocessing.process(target=squared_numbers)
    p2=multiprocessing.process(target=cube_numbers)

    #start the process

    p1.start()
    p2.start()
    t=time.time()

    #wait for the processs to response

    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)


