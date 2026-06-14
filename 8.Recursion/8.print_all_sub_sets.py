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


def print_subarrays2(arr: list[int]):
    N = len(arr)
    temp = []

    def backtrack(i: int):
        if i == N:
            return
        temp.append(arr[i])
        print(temp)
        backtrack(i + 1)
        temp.pop()
        backtrack(i + 1)

    backtrack(0)


arr = list(map(int, input("Enter arr: ").split()))
# print_subarrays(arr, len(arr), 0, [])
print_subarrays2(arr)
