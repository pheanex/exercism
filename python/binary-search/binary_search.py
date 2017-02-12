def binary_search(list, element):
    if not list:
        raise ValueError
    left, right = 0, len(list) - 1
    mid = (left + right) // 2
    while not list[mid] == element:
        if list[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
        if left > right:
            raise ValueError
        mid = (left + right) // 2
    return mid
