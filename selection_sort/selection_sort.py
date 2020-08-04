def _smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest_index = _smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr

if __name__ == '__main__':
    assert sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
    assert sort([]) == []
    assert sort([1, 1]) == [1, 1]
