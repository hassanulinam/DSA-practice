from MyUtils import reverse_array


def main():
    arr = [int(x) for x in input("Enter Arr#: ").split()]
    reverse_array(arr)
    print(arr)


if __name__ == "__main__":
    main()


#  TS - version
# import { question } from "readline-sync";

# const arr = question("Enter Arr: ")
#   .split(" ")
#   .map((s: string) => parseInt(s));

# function swapArrayElements(arr: number[], i: number, j: number): void {
#   arr[i] += arr[j];
#   arr[j] = arr[i] - arr[j];
#   arr[i] -= arr[j];
# }

# export function reverseArray(arr: number[]): void {
#   const N = arr.length;
#   const midLen = Math.floor(N / 2) - 1;

#   for (let i = 0; i <= midLen; i++) {
#     swapArrayElements(arr, i, N - i - 1);
#   }
# }

# export function reverseArrayV2(arr: number[]): void {
#   let left = 0;
#   let right = arr.length - 1;

#   while (left < right) {
#     swapArrayElements(arr, left, right);
#     left++;
#     right--;
#   }
# }

# reverseArrayV2(arr);
# console.log(arr);
