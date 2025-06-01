##mutithreading with thread pool executor 

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers():
    time.sleep(1)
    return f"Numbers :{numbers}"
numbers=[1,2,3,4,5]
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor,map(print_numbers,numbers)
    
for result in results:
    print(results)
    

 