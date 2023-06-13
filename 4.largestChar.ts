import process from "process";

// Find the largest character which is smaller than the given target character
function largestSmallChar(word: string, target: string): string {
  let start = 0,
    end = word.length - 1,
    mid: number;
  console.log({ start, end });
  while (start <= end) {
    mid = Math.floor((start + end) / 2);

    if (word[mid] < target) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
    console.log({ start, mid, end });
  }
  return word[end % word.length];
}

const givenWord = "adgjkmoqsuwy";
const target = process.argv[2];

const largestSmallCharacter = largestSmallChar(givenWord, target);
console.log({ largestSmallCharacter });
