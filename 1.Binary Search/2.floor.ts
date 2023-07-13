function closestFloor(arr: number[], target: number): number {
  let mid: number,
    start = 0,
    end = arr.length - 1;

  while (start <= end) {
    mid = Math.floor((start + end) / 2);
    console.log({ start, end, mid });

    if (arr[mid] < target) {
      start = mid + 1;
    } else if (arr[mid] > target) {
      end = mid - 1;
    } else {
      return arr[mid];
    }
  }
  return arr[end];
}

const givenList = [1, 2, 3, 5, 6, 8, 9, 11, 14, 26, 45, 56, 67, 89];
const targetNum = parseInt(process.argv[2]);
const floor = closestFloor(givenList, targetNum);
console.log({ floor });
