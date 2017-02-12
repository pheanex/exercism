def binary_search(list, element):
    left, right = 0, len(list) - 1
    mid = (left + right) // 2
    while left <= right:
        if list[mid] < element:
            left = mid + 1
        elif list[mid] > element:
            right = mid - 1
        else:
            return mid
        mid = (left + right) // 2
    raise ValueError
