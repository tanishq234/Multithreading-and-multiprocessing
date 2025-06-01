


import multiprocessing
import math
import sys
import time

#increase maximum number of digits for integer conversion

sys.set_int_max_str_digits(100000)

#function to compute factorial of a given number

def computer_factorial(number):
    print(f"computing factorial of a {number}")
    result=math.factorial(number)
    print(f"factorial of a {number} is {result}")
    return result

if__name__=="__main__":
    numbers=[5000,6000,7000,8000]

    start_time=time.time()  
    
    #create a pool of worker
    
    with multiprocessing.pool() as pool:
        results=pool.map(computer_factorial,numbers)
        
    end_time=time.time()
    
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time}seconds")
          
    
    