def binary_search(search_list, element):
    left, right = 0, len(search_list) - 1
    mid = (left + right) // 2
    while left <= right:
        if search_list[mid] < element:
            left = mid + 1
        elif search_list[mid] > element:
            right = mid - 1
        else:
            return mid
        mid = (left + right) // 2
    raise ValueError
