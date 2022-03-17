# Main-fil för lösnordsknäckaren

import multiprocessing
import concurrent.futures
import psutil
from random import randint
import time

#import sys # endast för sys.maxsize() max av en int

global STAR_VALUE

STAR_VALUE=4294967 # 22 sec @ 8 cores



# __init__ global variables for processes
def init_globals(key_not_found):
    global KEY_NOT_FOUND
    KEY_NOT_FOUND = key_not_found
    global HIDDEN_KEY
    HIDDEN_KEY = randint(1, MAX_INT)



# multiprocess function, notice small v in .value
def crack_something(cpu, cur_key, end_key):
    print(f'CPU: {cpu} keyspace start at {cur_key} and end at {end_key}')
    while KEY_NOT_FOUND.value and (cur_key <= end_key):
        
        if cur_key == HIDDEN_KEY:
            KEY_NOT_FOUND.value=False
            return f"CPU: {cpu} found secret key: {cur_key}"
        cur_key+=1
        #print(cur_key)
    return f"CPU: {cpu} reached key : {cur_key}"

def main():
    # share variable between processes, notice large V in .Value
    key_not_found = multiprocessing.Value('i', True)
    
    # definera listor
    cpu_count =  psutil.cpu_count(logical=True)# int
    print("CPU (process) count is: " , cpu_count)
    #cpus = [i for i in cpu_count] # lista
    cpus = []
    for i in range(cpu_count):
        cpus.append(i)
    print("CPU (process) list is: " , cpus)
    start_keys= []
    for i in range(cpu_count):
        start_keys.append(int((i)*(STAR_VALUE/cpu_count)))
    print("Start keyspace offsets: " , start_keys)
    
    end_keys=list(start_keys)
    end_keys.remove(end_keys[0])
    end_keys.append(STAR_VALUE)
    print("End keyspace offsets: " , end_keys)
        
        
    # [0, 1073741823, 2147483646, 3221225469]
    
    # [1073741823, 2147483646, 3221225469, 4294967295]

    with concurrent.futures.ProcessPoolExecutor(max_workers = cpu_count, initializer = init_globals, initargs = (key_not_found,)) as executor:
        for result in executor.map(crack_something, cpus, start_keys, end_keys):
            print(result)

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')