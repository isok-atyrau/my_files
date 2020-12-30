# Бинарный пойск
def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess  = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# # сортироква пузырком

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 -i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# # линейный поиск
def line_search(array, item):
    for value in enumerate(array):
        if value[1] == item:
            return value[0]
    return None

def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)


