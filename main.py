import json
import time

import requests
import concurrent.futures


# Sending requests to the pages
def send_request(index):
    response = requests.get(f'https://dummyjson.com/products/{index}')
    api_data = response.json()
    return api_data


def threads(index_range):
    thread_list = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        thread_results = list(executor.map(send_request, range(*index_range)))  # here I give any range of page to map function which take any argument and forms it into list
        thread_list.extend(thread_results)  # Here I'm extending size of thread_list with results
    return thread_list


def process():
    ranges = [(1, 21), (20, 41), (40, 61), (60, 81), (80, 101)]  # range where threads should move
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = list(executor.map(threads, ranges))  # Convert it to list
    return result


if __name__ == '__main__':
    start_time = time.time()  # Start measuring time

    with open('response.json','w') as file_json:  # here I opened response.json file where will be written response of 100 api data
        json.dump(process(), file_json, indent=3)

    elapsed_time = time.time() - start_time  # Calculate elapsed time
    print(f"Execution time: {elapsed_time} seconds")
