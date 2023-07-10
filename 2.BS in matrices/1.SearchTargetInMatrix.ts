import { question } from "readline-sync";

function findIndexInMatrix(
  matrix: number[][],
  target: number
): [number, number] {
  let row = 0,
    col = matrix.length - 1;

  while (row < matrix.length && col >= 0) {
    if (matrix[row][col] === target) {
      return [row, col];
    } else if (matrix[row][col] < target) {
      row++;
    } else {
      col--;
    }
  }
  return [-1, -1];
}

const matrix = [
  [1, 10, 20, 30],
  [2, 11, 23, 31],
  [5, 14, 25, 34],
  [7, 15, 27, 35],
  [9, 19, 29, 39],
];

const target = parseInt(question("Enter Target: "));
const position = findIndexInMatrix(matrix, target);
console.log({ position });
