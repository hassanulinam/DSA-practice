// rotated array:- [3, 4, 5, 6, 0, 1, 2]
import { question } from "readline-sync";

export function getIndexOfTargetFromBS(
  arr: number[],
  target: number,
  start: number,
  end: number
): number {
  let mid: number;
  while (start <= end) {
    mid = Math.floor((start + end) / 2);

    const midElement = arr[mid];
    if (midElement === target) {
      return mid;
    } else if (midElement > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return -1;
}

export function findPivotElementInRotatedArray(arr: number[]): number {
  let start = 0,
    end = arr.length - 1,
    mid: number;

  while (start <= end) {
    mid = Math.floor((start + end) / 2);

    if (arr[mid] > arr[mid + 1]) {
      return mid;
    } else if (arr[start] > arr[mid]) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return -1;
}

export function searchInRotatedArray(arr: number[], target: number): number {
  const pivot = findPivotElementInRotatedArray(arr);
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

const rotatedArr = question("Enter rotated array:\n")
  .split(" ")
  .map((s: string) => parseInt(s));
const target = parseInt(question("Enter target: "));
const targetIndex = searchInRotatedArray(rotatedArr, target);
console.log({ targetIndex });
