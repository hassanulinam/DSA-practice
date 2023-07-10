// rotated array:- [3, 4, 5, 6, 0, 1, 2]
import { question } from "readline-sync";

function getIndexOfTargetFromBS(
  arr: number[],
  target: number,
  start: number,
  end: number
): number {
  let mid: number;
  let index = -1;
  while (start <= end) {
    mid = Math.floor((start + end) / 2);

    const midElement = arr[mid];
    if (midElement === target) {
      index = mid;
      end = mid - 1;
    } else if (midElement > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return index;
}

// Find pivot element rotated array with duplicates
function findPivotWithDuplicates(arr: number[]): number {
  let start = 0,
    end = arr.length - 1,
    mid: number;

  while (start <= end) {
    mid = Math.floor((start + end) / 2);

    if (arr[mid] > arr[mid + 1]) {
      return mid;
    }

    console.log({ start, end, mid, midEl: arr[mid] });

    if (arr[start] === arr[mid] && arr[end] === arr[mid]) {
      // should check if the start is pivot before skipping it
      if (arr[start] > arr[start + 1]) {
        return start;
      }
      start++;

      // check if end is pivot before skipping it
      if (arr[end] < arr[end - 1]) {
        return end - 1;
      }
      end--;
    }
  }
  return -1;
}

function findPivot(arr: number[]): number {
  let left = 0;
  let right = arr.length - 1;

  // Handle edge case where array is not rotated
  if (arr[left] <= arr[right]) {
    return arr[left];
  }

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] > arr[mid + 1]) {
      // If the next element is smaller than the current element, then we've found the pivot
      return arr[mid];
    } else if (arr[mid] === arr[left] && arr[mid] === arr[right]) {
      // If left, mid and right elements are same, we can't determine which way to go
      // So move both pointers towards center
      left++;
      right--;
    } else if (
      arr[left] < arr[mid] ||
      (arr[left] === arr[mid] && arr[mid] > arr[right])
    ) {
      // If left half is sorted, search right half
      left = mid + 1;
    } else {
      // If right half is sorted, search left half
      right = mid - 1;
    }
  }

  // The pivot was not found
  return -1;
}

function searchInRotatedArray(arr: number[], target: number): number {
  const pivot = findPivot(rotatedArr);
  console.log({ pivot });

  const firstPart = { start: 0, end: pivot };
  const indexInFirstPart = getIndexOfTargetFromBS(
    arr,
    target,
    firstPart.start,
    firstPart.end
  );
  if (indexInFirstPart !== -1) {
    return indexInFirstPart;
  }

  const secondPart = { start: pivot + 1, end: arr.length - 1 };
  const indexInSecondPart = getIndexOfTargetFromBS(
    arr,
    target,
    secondPart.start,
    secondPart.end
  );
  return indexInSecondPart;
}

// ex: [2, 9, 2, 2, 2, 2]
const rotatedArr = question("Enter rotated array with duplicates :\n")
  .split(" ")
  .map((s: string) => parseInt(s));
const target = parseInt(question("Enter target: "));
const targetIndex = searchInRotatedArray(rotatedArr, target);
console.log({ targetIndex });
