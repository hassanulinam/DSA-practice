import process from "process";

// Find the smallest character which is larger than the given target character.
const smallestChar = (word: string, target: string) => {
  let start = 0,
    end = word.length - 1,
    mid: number;
  console.log({ start, end });
  while (start <= end) {
    mid = Math.floor((start + end) / 2);

    if (target < word[mid]) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
    console.log({ start, mid, end, char: word[mid] });
  }
  return word[start % word.length];
};

const giveWord = "bdegjloqstuwyz";
const target = process.argv[2];
const smallestLargeChar = smallestChar(giveWord, target);
console.log({ smallestLargeChar });
