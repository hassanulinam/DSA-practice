// Find index of the given target in the infinite array (unknown length)
function getIndexInInfiniteArray(arr: number[], target: number): number {
  let start = 0;
  let end = 1;
  let mid: number;

  while (arr[end] < target) {
    start = end;
    end *= 2;
  }

  while (start <= end) {
    mid = Math.floor((start + end) / 2);
    const currentNumber = arr[mid];

    if (currentNumber === target) {
      return mid;
    } else if (currentNumber > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }

  return -1;
}

const givenNums = [1, 2, 3, 4, 5, 6, 7];
const targetNumber = parseInt(process.argv[2]);
const index = getIndexInInfiniteArray(givenNums, targetNumber);
console.log({ index });
