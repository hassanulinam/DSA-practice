// Find the peak (maximum) in the Bitonic array.
// Example bitonic array: [1, 2, 3, 4, 3, 2] (assume no duplicates will occur)
function getPeakIndex(arr: number[]): number {
  let start = 0,
    end = arr.length - 1,
    mid: number,
    peak = 0;

  while (start <= end) {
    mid = Math.floor((start + end) / 2);

    if (arr[mid] > arr[mid + 1]) {
      // we are in decreasing part
      peak = mid;
      end = mid - 1;
    } else {
      // we are in increasing part
      peak = mid + 1;
      start = mid + 1;
    }
  }

  return peak;
}

const givenBitonicArray = [-1, 0, 1, 2, 3, 4, 5, 2, 1];
const peakIndex = getPeakIndex(givenBitonicArray);
console.log({ peakIndex });
