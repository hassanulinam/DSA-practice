# Kadene's algo

arr = list(map(int, input("Enter arr: ").split()))
N = len(arr)

sub_array_start_index = 0
ps = None

current_sum = 0
max_sum = 0
for i in range(N):
    current_sum += arr[i]
    if current_sum > max_sum:
        max_sum = current_sum
        ps = (sub_array_start_index, i)
    if current_sum < 0:
        current_sum = 0
        sub_array_start_index = i + 1

print(max_sum)
print(ps)
