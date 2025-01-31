import random
import time

def randomized_quicksort(arr):
    stack = [(0, len(arr) - 1)] # Initialize stack, in charge of keeping track of the sub-arrays
    
    while stack:
        low, high = stack.pop()
        if low < high:
            # Select a random pivot and swap with last element
            pivot_index = random.randint(low, high) # using the random library to get a random index value between start and end indeces
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            # Partition the array
            pi = partition_and_sort(arr, low, high)
            # Push left and right subarrays to stack
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

def deterministic_quicksort(arr):
    stack = [(0, len(arr) - 1)] # Initialize stack ot keep track of sub-arrays
    
    while stack:
        low, high = stack.pop()
        if low < high:
            # Partition using last element as pivot -> Our pivot will always pick the same index
            pi = partition_and_sort(arr, low, high)
            # Push left and right subarrays to stack
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

def partition_and_sort(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# method to generate a randomized array, where n is the size and m the max possible value
def generate_random_array(n, m): 
    return [random.randint(0, m) for _ in range(n)]

# method to generate a sorted array of size n
def generate_sorted_array(n):
    return list(range(n))

# method to generate a reverse-sorted array of size n
def generate_reverse_sorted_array(n):
    return list(range(n, 0, -1))

def get_performance(func, arr):
    start_time = time.time()  # start
    func(arr)  # Call the function
    end_time = time.time()  # end
    return (end_time - start_time)

arr = generate_random_array(1000, 1200)
time_taken_deterministic = get_performance(deterministic_quicksort, arr)
time_taken_randomized = get_performance(randomized_quicksort, arr)

print("Randomize Array performance: \n Deterministic Quicksort: ", time_taken_deterministic, "\n Randomized Quicksort: ", time_taken_randomized)
