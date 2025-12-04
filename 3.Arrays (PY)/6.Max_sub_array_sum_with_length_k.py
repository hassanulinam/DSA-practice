# Sliding window technique


arr = [int(x) for x in input("Enter arr: ").split()]
k = int(input("Enter K: "))
N = len(arr)

# sum(arr[1:5]) = sum(arr[0:4]) + arr[5] - arr[0]
# For each transition of index, you just keep your counter updated with calculating changes by adding what's being introduced, and discarding the very last item
# sum(arr[i : j]) = sum(arr[i-1 : j-1]) + arr[j] - arr[i]


current_sum = sum(arr[:k])
max_sum = current_sum
positions = (0, k)

for i in range(k, N - 1):
    current_sum += arr[i] - arr[i - k]
    if current_sum > max_sum:
        max_sum = current_sum
        positions = (i, i - k)

print(max_sum)
print(positions)
