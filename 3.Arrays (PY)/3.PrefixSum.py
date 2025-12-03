# Given an array of N integers and Q queries. For each query calculate the
# sum of elements in the range - [ L , R ]


from MyUtils import get_prefix_sum_arr

arr = [int(x) for x in input("Enter Arr: ").split()]
N = int(input("No.Of Queries: "))

prefix_sum_arr = get_prefix_sum_arr(arr)

for i in range(N):
    L, R = [int(x) for x in input(f"{i + 1}). Enter indices range: ").split()]
    if L > 0:
        print(prefix_sum_arr[R] - prefix_sum_arr[L - 1])
    else:
        print(prefix_sum_arr[R])
