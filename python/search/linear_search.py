# Complexity O(n)
def binary_search(values, key):
    values.sort()
    top = len(values) - 1
    bot = 0
    while top > bot:
        mid = (top  + bot) // 2
        if values[mid] == key:
            return True
        elif values[mid] > key:
            bot = mid
        else:
            top = mid

    return False
# Complexity O(log(n))
def search(values, key):
    for value in values:
        if value == key:
            return True
    return False

numbers = [10,9,8,7,6,5,4,3,2,1]
for value in numbers:
    result_linear = search(numbers, value)
    result_binary = search(numbers, value)
    print(f'Linear Search result: {result_linear}')
    print(f'Binary Search result: {result_binary}')