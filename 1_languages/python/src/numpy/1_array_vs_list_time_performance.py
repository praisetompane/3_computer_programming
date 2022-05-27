import numpy as np
import time
from typing import List

def run_simulation(size):
    print(f'running simulation for {size} elements.\n')
    SECONDS_and_MILISECONDS_RATIO = 1000

    def calculate_time_difference(starttime, endtime):
        return (time.time() - start_time) * SECONDS_and_MILISECONDS_RATIO

    def print_result(data_structure: str, endtime: float):
        print(f'{data_structure} took: {end_time} seconds.\n')

    print('adding numbers using python native list.\n')
    list_1 = list([i for i in range(size)])
    list_2 = list([i for i in range(size)])
 
    start_time = time.time()
    _ = list_1 + list_2  
    end_time = calculate_time_difference(start_time, time.time())
    print_result('python list', end_time)

    print('adding numbers using numpy array.\n')
    np_array_1 = np.arange(size)
    np_array_2 = np.arange(size)

    start_time = time.time()
    _ = np_array_1 + np_array_2
    end_time = calculate_time_difference(start_time, time.time())
    print_result('numpy array', end_time)


def run_trial(trials: int, element_sizes: List[int]):
    for i in range(trials):
        for size in element_sizes:
            run_simulation(size)


run_trial(1, [100, 1000000, 10000000, 100000000])
