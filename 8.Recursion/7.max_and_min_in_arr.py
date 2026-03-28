def max_min(arr: list[int], N: int) -> tuple[int, int]:
    if N == 0:
        raise ValueError("Empty array given")
    if N == 1:
        return arr[0], arr[0]

    sub_max_min = max_min(arr[1:], N - 1)
    mx = max(arr[0], sub_max_min[0])
    mn = min(arr[0], sub_max_min[1])
    return (mx, mn)


arr = list(map(int, input("Enter Arr: ").split()))
print(f"(Max, Min): {max_min(arr, len(arr))}")
