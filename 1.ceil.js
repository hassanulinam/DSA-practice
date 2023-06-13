 
const ceiling = (arr, target) => {
    let start = 0
    let end = arr.length - 1
    let mid;
    while (start <= end) {
        mid = Math.floor((start + end)/2)
        // console.log("  ", {start, end, mid})
        if (arr[mid] > target) {
            end = mid - 1
        } else if (arr[mid] < target) {
            start = mid + 1
        } else {
            return arr[mid]
        }
        console.log({start, end, mid})
    }
    return arr[start]
}



const given_list = [1, 4, 6, 8, 9, 16, 34, 35, 56, 97, 105]
const target = 230


const closest_ceiling = ceiling(given_list, target)
console.log("===result:", closest_ceiling ?? "Not found")

