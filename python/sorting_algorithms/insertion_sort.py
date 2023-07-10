import numpy as np
'''
complexity:
  When to use: Use it when the array is almost sorted. 
  Best case: O(n) -> The array is sorted
  Worst case: O(n^2) -> The array is in reverse order
'''
def insertion_sort(arr):
   n = len(arr)
   sorted_arr = arr.copy()
   for i in range(1, n):
      temp = sorted_arr[i]
      pos = i - 1
      while pos >= 0 and sorted_arr[pos] > temp:
        sorted_arr[pos + 1] = sorted_arr[pos]
        pos = pos - 1
      sorted_arr[pos + 1] = temp
   return sorted_arr

# complexity O(n^2)
def bubble_sort(arr):
  n = len(arr)
  sorted_arr = arr.copy()
  for i in range(0, n-1):
    for j in range(i + 1, n):
      if sorted_arr[i] > sorted_arr[j]:
        aux = sorted_arr[i]
        sorted_arr[i] = sorted_arr[j]
        sorted_arr[j] = aux
  return sorted_arr

random_arr = np.random.randint(0,10,10)

print('Sorted list by bubble sort: ', bubble_sort(random_arr))
print('Sorted list by insertion sort: ', insertion_sort(random_arr))
print('Original list: ', random_arr)
