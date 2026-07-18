// https://leetcode.com/problems/reverse-integer

function reverse(x: number): number {
  const INT_MIN = Math.pow(-2, 31);
  const INT_MAX = Math.pow(2, 31) - 1;

  let ans = 0;
  while (x !== 0) {
    const digit = x % 10;

    if (ans < INT_MIN / 10 || ans > INT_MAX / 10) {
      return 0;
    }
    ans = ans * 10 + digit;
    x = (x - digit) / 10;
  }
  return ans;
}

console.log(reverse(-234));
