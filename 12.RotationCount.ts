import { question } from "readline-sync";

function findPivot(arr: number[]) {
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
    console.log({ start, end, mid });
  }

  return -1;
}

const rotatedArray = question("Enter rotated Array:\n")
  .split(" ")
  .map((s: string) => parseInt(s));

const pivot = findPivot(rotatedArray);
const rotationsCount = pivot + 1;
console.log({ rotationsCount });
