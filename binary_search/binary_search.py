def search(l, item):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = l[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

if __name__ == '__main__':
    assert search([1, 2, 3, 6, 7, 9], 3) == 2
    assert search([1, 2, 3, 6, 7, 9], 1) == 0
    assert search([1, 2, 3, 6, 7, 9], 12) == None
