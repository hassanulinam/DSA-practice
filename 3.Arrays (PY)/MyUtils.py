def swap(arr, i, j):
    arr[i] += arr[j]
    arr[j] = arr[i] - arr[j]
    arr[i] -= arr[j]


def reverse_array(arr, left=0, right=-1):
    if right == -1:
        right = len(arr) - 1
    while left < right:
        swap(arr, left, right)
        left += 1
        right -= 1


def rotate_arr_rtl(arr, k):
    """Rotate array element from right to left"""
    """reverse entire array, divide array into two parts with k%N (n=arr.length), and the just reverse those parts"""
    N = len(arr)
    k = k % N
    if k > 0:
        reverse_array(arr)
        reverse_array(arr, 0, k - 1)
        reverse_array(arr, k, N - 1)


def rotate_arr_ltr(arr, k):
    """Rotate array elements from left to right"""
    N = len(arr)
    k = k % N
    if k > 0:
        reverse_array(arr)
        reverse_array(arr, 0, N - k - 1)
        reverse_array(arr, N - k, N - 1)


def get_prefix_sum_arr(arr, step=1):
    current = arr[0]
    result = [current] * step
    i = step
    while i < len(arr):
        current += arr[i]
        i += step
        j = 0
        while j < step:
            result.append(current)
            j += 1

    return result
