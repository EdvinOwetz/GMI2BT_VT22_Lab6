# Main-fil för lösnordsknäckaren

import multiprocessing
import concurrent.futures
import secrets
import psutil
from random import randint
import time

#import sys # endast för sys.maxsize() max av en int

global START_VALUE

START_VALUE=4294967 # 22 sec @ 8 cores



# __init__ global variables for processes
def init_globals(key_not_found,sec_key):
    global KEY_NOT_FOUND
    KEY_NOT_FOUND = key_not_found
    global HIDDEN_KEY
    HIDDEN_KEY = sec_key



# multiprocess function, notice small v in .value
def crack_something(cpu, cur_key, end_key):
    print(f'CPU: {cpu} keyspace start at {cur_key} and end at {end_key}')
    while KEY_NOT_FOUND.value and (cur_key <= end_key):
        
        if cur_key == HIDDEN_KEY.value:
            KEY_NOT_FOUND.value=False
            return f"CPU: {cpu} found secret key: {cur_key}"
        cur_key+=1
        #print(cur_key)
    return f"CPU: {cpu} reached key : {cur_key}"

def main():
    # share variable between processes, notice large V in .Value
    key_not_found = multiprocessing.Value('i', True)
    
    secret_key = multiprocessing.Value('i',randint(1, START_VALUE))
    

    # definera listor
    cpu_count =  psutil.cpu_count(logical=True)# int
    print("CPU (process) count is: " , cpu_count)
    cpus = []
    for i in range(cpu_count):
        cpus.append(i)
    print("CPU (process) list is: " , cpus)
    start_keys=[]
    for i in range(cpu_count):
        start_keys.append(int((i)*(START_VALUE/cpu_count)))
    print("Start keyspace offsets: " , start_keys)
    
    end_keys=list(start_keys)
    end_keys.remove(end_keys[0])
    end_keys.append(START_VALUE)
    print("End keyspace offsets: " , end_keys)
    
    print(f"Secret key: {secret_key.value}")

    with concurrent.futures.ProcessPoolExecutor(max_workers = cpu_count, initializer = init_globals, initargs = (key_not_found,secret_key)) as executor:
        for result in executor.map(crack_something, cpus, start_keys, end_keys):
            print(result)

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')