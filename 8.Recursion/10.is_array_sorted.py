def is_array_sorted(arr: list[int]) -> bool:

    if len(arr) < 2:
        return True

    if len(arr) == 2:
        return arr[0] < arr[1]

    return arr[0] < arr[1] and is_array_sorted(arr[1:])


arr = list(map(int, input("Enter arr: ").split()))
print(is_array_sorted(arr))
