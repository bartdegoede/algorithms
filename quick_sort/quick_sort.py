import random

def quicksort(array):
    if len(array) < 2:
        # base case; arrays with 0 or 1 element are already sorted
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    assert quicksort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
    assert quicksort([]) == []
    assert quicksort([1, 1]) == [1, 1]
