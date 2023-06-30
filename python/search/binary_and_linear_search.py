# Complexity O(n(log(n)))
# Constraint: the array must be sorted
def binary_search(values, key):
    values.sort()
    top = len(values) - 1
    bot = 0
    while top > bot:
        mid = (top  + bot) // 2
        if values[mid] == key:
            return True
        elif values[mid] > key:
            bot = mid + 1
        else:
            top = mid - 1
    return False

# Complexity O(n)
def search(values, key):
    for value in values:
        if value == key:
            return True
    return False

numbers = [10,9,8,7,6,5,4,3,2,1]
print('\n\nTest1: All results should be true:')
for value in numbers:
    result_linear = search(numbers, value)
    result_binary = search(numbers, value)
    print(f'Linear Search result: {result_linear}')
    print(f'Binary Search result: {result_binary}')

print('\n\nTest2: All results should be false:')
for value in numbers:
    result_linear = search(numbers, value + 100)
    result_binary = search(numbers, value + 100)
    print(f'Linear Search result: {result_linear}')
    print(f'Binary Search result: {result_binary}')