// Find first and last indices of the target element in the list, using binary search.
function getIndex(arr: number[], target: number, shouldFindFirstIndex = true) {
  let start = 0,
    end = arr.length - 1,
    index = -1,
    mid: number;

  while (start <= end) {
    mid = Math.floor((start + end) / 2);
    const midNumber = arr[mid];

    if (midNumber === target) {
      index = mid;
      if (shouldFindFirstIndex) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    } else if (midNumber > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }

  return index;
}

const givenArray = [1, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9, 10];
const target = parseInt(process.argv[2]);
const firstIndex = getIndex(givenArray, target);
const lastIndex = getIndex(givenArray, target, false);

console.log({ firstIndex, lastIndex });
