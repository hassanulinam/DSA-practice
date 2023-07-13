import { question } from "readline-sync";

function orderAgnosticBS(
  arr: number[],
  target: number,
  start: number,
  end: number
): number {
  let mid: number;
  const isAsc = arr[start] < arr[end];

  while (start <= end) {
    mid = Math.floor((start + end) / 2);

    const currentNumber = arr[mid];

    if (currentNumber === target) {
      return mid;
    }

    if (isAsc) {
      if (currentNumber > target) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    } else {
      if (currentNumber > target) {
        start = mid + 1;
      } else {
        end = mid - 1;
      }
    }
  }

  return -1;
}

function getPeakIndexInMountain(arr: number[]): number {
  let start = 0,
    end = arr.length - 1,
    mid: number;

  while (start < end) {
    mid = Math.floor((start + end) / 2);

    if (arr[mid] > arr[mid + 1]) {
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  console.log({ start, end });
  return start;
}

function searchTargetInMountain(arr: number[], target: number): number {
  const peak = getPeakIndexInMountain(arr);

  // search in increasing part
  const indexInIncreasingPart = orderAgnosticBS(arr, target, 0, peak);
  if (indexInIncreasingPart !== -1) {
    return indexInIncreasingPart;
  }

  // search in decreasing part
  const start = peak + 1,
    end = arr.length - 1;
  const indexInDecreasingPart = orderAgnosticBS(arr, target, start, end);
  return indexInDecreasingPart;
}

const givenMountainArray = question("Enter mountain arr: ")
  .split(" ")
  .map((s: string) => parseInt(s));

const target = parseInt(question("Enter target: "));
const targetIndex = searchTargetInMountain(givenMountainArray, target);
console.log({ targetIndex });
