import { question } from "readline-sync";

// Find the peak (maximum) in the Bitonic array.
// Example bitonic array: [1, 2, 3, 4, 3, 2] (assume no duplicates will occur)
function getPeakIndex(arr: number[]): number {
  let start = 0,
    end = arr.length - 1,
    mid: number;

  while (start < end) {
    // start, end will eventually overlap at peak index. Hence using `<` instead of `<=`
    mid = Math.floor((start + end) / 2);

    if (arr[mid] > arr[mid + 1]) {
      // this may be possible answer, but go look left
      end = mid; // we should consider mid index as it is greater one. (rather than mid-1)
    } else {
      // here we need not consider mid index as it is smaller one.
      start = mid + 1;
    }
  }
  // after the loop, start and end pointers will point to a same index which is the peak one.
  console.log({ start, end });
  return start;
}

const givenBitonicArray = question("Enter mountain array:\n")
  .split(" ")
  .map((s: string) => parseInt(s));
const peakIndex = getPeakIndex(givenBitonicArray);
console.log({ peakIndex });
