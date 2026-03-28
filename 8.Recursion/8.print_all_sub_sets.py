# backtracking example
def print_subarrays(arr: list[int], N: int, i: int, temp: list[int]) -> None:
    if i == N:
        print(temp)
        return

    temp.append(arr[i])
    print_subarrays(arr, N, i + 1, temp)
    temp.pop()
    print_subarrays(arr, N, i + 1, temp)
    return


arr = list(map(int, input("Enter arr: ").split()))
print_subarrays(arr, len(arr), 0, [])
