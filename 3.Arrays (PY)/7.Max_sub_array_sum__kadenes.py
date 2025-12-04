# Kadene's algo

arr = list(map(int, input("Enter arr: ").split()))
N = len(arr)
current_sum = arr[0]
max_sum = current_sum

for i in range(1, N):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(current_sum, max_sum)

print(max_sum)
