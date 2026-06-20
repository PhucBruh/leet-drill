def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def sum_1_to_N(n):
    if n == 0:
        return 0
    return n + sum_1_to_N(n - 1)


def is_power_of_2(n):
    if n < 1:
        return False
    elif n == 1:
        return True
    else:
        return is_power_of_2(n // 2)


def reverse_string(s, i=0):
    if i == len(s):
        return ""

    return reverse_string(s, i + 1) + s[i]


def count_occurrences(arr, target, i=0):
    if i == len(arr):
        return 0

    if arr[i] == target:
        return count_occurrences(arr, target, i + 1) + 1

    return count_occurrences(arr, target, i + 1)


def sum_of_digits(n):
    if n < 10:
        return n
    return sum_of_digits(n // 10) + n % 10


def palidrome(s, l, r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return palidrome(s, l + 1, r - 1)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def count_zeros(n):
    if n < 10:
        if n == 0:
            return 1
        return 0
    if n % 10 == 0:
        return count_zeros(n // 10) + 1

    return count_zeros(n // 10)


def first_index(arr, target, i=0):
    if i == len(arr):
        return None

    if arr[i] == target:
        return i

    return first_index(arr, target, i + 1)


# result = factorial(5)
# result = sum_1_to_N(5)
# result = is_power_of_2(16)
# result = reverse_string("hello")
# result = count_occurrences([1, 2, 3, 2, 1, 5, 2, 8, 3], 3)

# s = "level"
# result = palidrome(s, 0, len(s) - 1)

result = count_zeros(10)

# result = first_index([1, 3, 2, 1, 5, 2, 8, 3], 2)
print(result)
