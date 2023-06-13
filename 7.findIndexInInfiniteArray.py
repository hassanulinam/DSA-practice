def get_index_in_infinite_array(arr, target):
    start = 0
    end = 1

    try:
        while arr[end] < target:
            start = end
            end *= 2
    except:
        return -1

    while start <= end:
        mid = (start + end) // 2
        current_number = arr[mid]

        if current_number == target:
            return mid
        elif current_number > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1

given_nums = [1, 2, 3, 4, 5, 6, 7, 8]
target_number = int(input("Enter the target number: "))
index = get_index_in_infinite_array(given_nums, target_number)
print({"index": index})
