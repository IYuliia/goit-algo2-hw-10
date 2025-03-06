import random
import time
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr) 
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0] 
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return deterministic_quick_sort(less) + equal + deterministic_quick_sort(greater)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

array_sizes = [10_000, 50_000, 100_000, 500_000]
random_arrays = {size: [random.randint(1, 1000000) for _ in range(size)] for size in array_sizes}

randomized_times = []
deterministic_times = []

for size in array_sizes:
    arr = random_arrays[size]

    randomized_time = sum(measure_time(randomized_quick_sort, arr) for _ in range(5)) / 5
    randomized_times.append(randomized_time)
    
    deterministic_time = sum(measure_time(deterministic_quick_sort, arr) for _ in range(5)) / 5
    deterministic_times.append(deterministic_time)

for size, randomized_time, deterministic_time in zip(array_sizes, randomized_times, deterministic_times):
    print(f"Array Size: {size}")
    print(f"   Randomized QuickSort: {randomized_time:.4f} seconds")
    print(f"   Deterministic QuickSort: {deterministic_time:.4f} seconds")


plt.figure(figsize=(10, 6))

plt.plot(array_sizes, randomized_times, label='Randomized QuickSort', marker='o')
plt.plot(array_sizes, deterministic_times, label='Deterministic QuickSort', marker='o')

plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Randomized vs Deterministic QuickSort')
plt.legend()

plt.grid(True)
plt.show()

print("\nAnalysis and Conclusion:")

for size, randomized_time, deterministic_time in zip(array_sizes, randomized_times, deterministic_times):
    print(f"\nFor Array Size: {size}")
    print(f"   Randomized QuickSort time: {randomized_time:.4f} seconds")
    print(f"   Deterministic QuickSort time: {deterministic_time:.4f} seconds")
    
    if randomized_time < deterministic_time:
        print("   Randomized QuickSort is slightly faster, as expected due to better pivot selection avoiding worst-case scenarios.")
    elif randomized_time > deterministic_time:
        print("   Deterministic QuickSort is slightly faster, which could be due to random fluctuations or the array structure.")
    else:
        print("   Both algorithms are performing similarly in this case.")

print("\nConclusion:")
print("As array size increases, both algorithms show similar time complexities, which is expected with average case O(n log n) time complexity.")
print("However, in real-world scenarios, Randomized QuickSort tends to be more efficient on average, because it avoids worst-case performance (O(n^2)) that can occur in Deterministic QuickSort when the pivot selection is poor.")
print("The performance difference between the two algorithms is not very significant for the array sizes tested, but Randomized QuickSort has a better chance of avoiding performance degradation in specific cases.")
