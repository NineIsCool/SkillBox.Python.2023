def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while (l <= r):
        m = (l + r) // 2
        if (arr[m] == x):
            return m
        elif (arr[m] < x):
            l = m + 1
        else:
            r = m - 1
    return -1