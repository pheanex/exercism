def is_palindrome(string):
    return string == string[::-1]


def palindromes(start, stop):
    return [(i * j, (i, j)) for i in range(start, stop) for j in range(start, stop) if is_palindrome(str(i * j))]


def smallest_palindrome(max_factor, min_factor=0):
    return min(palindromes(min_factor, max_factor + 1))


def largest_palindrome(max_factor, min_factor=0):
    return max(palindromes(min_factor, max_factor + 1))
