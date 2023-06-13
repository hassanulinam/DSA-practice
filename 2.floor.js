const closest_floor = (arr, target) => {
    let mid, start = 0
    let end = arr.length - 1

    while (start <= end) {
        mid = Math.floor((start + end)/2)
        console.log({start, end, mid})

        if (arr[mid] < target) {
            start = mid + 1
        } else if(arr[mid] > target) {
            end = mid - 1
        } else {
            return arr[mid]
        }
    }
    return arr[end]
}


const given_list = [1, 2, 3, 5, 6, 8, 9, 11, 14, 26, 45, 56, 67, 89]
const target = parseInt(process.argv[2])
console.log("\n==== Result:", closest_floor(given_list, target) ?? "Not found")


