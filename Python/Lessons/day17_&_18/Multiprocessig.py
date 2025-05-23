import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

def cpu_task(power):
    count = 0
    for i in range(10**power):
        count += 1
    return count

if __name__ == "__main__":
    num_tasks = 2
    power = 3

    print("Comparing Multithreading vs. Multiprocessing (CPU-bound Task)")

    # Multithreading
    start_time_thread = time.time()
    with ThreadPoolExecutor(max_workers=num_tasks) as executor:
        results_thread = list(executor.map(cpu_task, [power]*num_tasks))
    end_time_thread = time.time()
    time_taken_thread = end_time_thread - start_time_thread
    print(f"Multithreading Time Taken: {time_taken_thread:.4f} seconds")
    print(f"Thread Results (first few): {results_thread[:2]}\n")

    # Multiprocessing
    start_time_process = time.time()
    with Pool(processes=num_tasks) as pool:
        results_process = list(pool.map(cpu_task, [power]*num_tasks))
    end_time_process = time.time()
    time_taken_process = end_time_process - start_time_process
    print(f"Multiprocessing Time Taken: {time_taken_process:.4f} seconds")
    print(f"Process Results (first few): {results_process[:2]}\n")

    print("Comparison:")
    if time_taken_process < time_taken_thread:
        speedup = time_taken_thread / time_taken_process
        print(f"Multiprocessing was significantly faster, achieving a speedup of {speedup:.2f}x.")
    elif time_taken_thread < time_taken_process:
        slowdown = time_taken_process / time_taken_thread
        print(f"Multiprocessing was slower by a factor of {slowdown:.2f}x.")
    else:
        print("Multithreading and Multiprocessing performance was similar.")