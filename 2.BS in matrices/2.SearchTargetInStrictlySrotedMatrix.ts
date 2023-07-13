import { question } from "readline-sync";

function BSInGivenRowOfMatrix(
  matrix: number[][],
  target: number,
  row: number
): [number, number] {
  let start = 0,
    end = matrix[row].length - 1;
  while (start <= end) {
    const mid = Math.floor((start + end) / 2);
    const num = matrix[row][mid];
    if (num === target) {
      return [row, mid];
    } else if (num < target) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  return [-1, -1];
}

function searchInStrictlySortedMatrix(
  matrix: number[][],
  target: number
): [number, number] {
  const rows = matrix.length,
    cols = matrix[0].length;
  if (rows === 1) {
    return BSInGivenRowOfMatrix(matrix, target, 0);
  }

  let rStart = 0,
    rEnd = rows - 1,
    cMid = Math.floor(cols / 2);

  // iterate loop until 2 rows remains
  while (rStart < rEnd - 1) {
    const rMid = Math.floor((rStart + rEnd) / 2);
    const num = matrix[rMid][cMid];

    if (num === target) {
      return [rMid, cMid];
    } else if (num < target) {
      rStart = rMid;
    } else {
      rEnd = rMid;
    }
    console.log({ rStart, rEnd, rMid });
  }

  const row1Result = BSInGivenRowOfMatrix(matrix, target, rStart);
  if (row1Result[0] != -1) {
    return row1Result;
  }

  const row2Result = BSInGivenRowOfMatrix(matrix, target, rStart + 1);
  if (row2Result[0] != -1) {
    return row2Result;
  }

  return [-1, -1];
}

const strictlySortedMatrix = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 34, 45],
  [56, 67, 78, 89],
  [90, 91, 92, 93],
  [95, 97, 100, 101],
  [102, 104, 105, 107],
  [112, 234, 345, 567],
];

const target = parseInt(question("Enter Target: "));
const position = searchInStrictlySortedMatrix(strictlySortedMatrix, target);
console.log({ position });
