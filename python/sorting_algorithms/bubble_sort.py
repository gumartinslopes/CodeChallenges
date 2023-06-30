import numpy as np

# Complexity = On^2 in all three cases
def bubble_sort(values):
    result = values.copy()
    for i in range(len(result)):
        for j in range(len(result) - i-1):
            if result[j] > result[j+1]:
                aux = result[j]
                result[j] = result[j+1]
                result[j+1] = aux
    return result
random_values = np.random.randint(0, 10, 10)
print(random_values)
print(bubble_sort(random_values))