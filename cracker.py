# Main-fil för lösnordsknäckaren

import multiprocessing
import concurrent.futures
import psutil

import sys # endast för sys.maxsize() max av en int


# init global variables for processes
# def init_globals(key_not_found):
#     global KEY_NOT_FOUND
#     KEY_NOT_FOUND = key_not_found

# # share variable between processes, notice large V in .Value
# key_not_found = multiprocessing.Value('i', True)
# with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count,
# initializer=init_globals, initargs=(key_not_found,)) as executor:
# for result in executor.map(crack_something, cpus, start_keys,
# end_keys):
# print(result)

# # multiprocess function, notice small v in .value
# def crack_something(cpu, cur_key, end_key):
#  print(f'CPU: {cpu} keyspace start at {cur_key} and end at
# {end_key}')

#  while KEY_NOT_FOUND.value and (cur_key <= end_key):