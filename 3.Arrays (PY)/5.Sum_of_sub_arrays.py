arr = [int(x) for x in input("Enter arr: ").split()]

# N = lenght, k = current element at index 'k'
# contribution of k:
# # # #  no.of subarrays ending with 'k' = [0, i] --> i-0+1 = i+1
# # # # no.of subarray starting with 'k' = [i, N-1] --> (N-1)-i+1 = N-i
# # # # total occurences of k = (i + 1) * (N - i)

total = 0
N = len(arr)
for i in range(N):
    total += arr[i] * (i + 1) * (N - i)

print(total)
