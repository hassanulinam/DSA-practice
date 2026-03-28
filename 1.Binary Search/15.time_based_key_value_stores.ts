// https://leetcode.com/problems/time-based-key-value-store

interface TimeStampMap {
  [key: string]: {
    [timestamp: number]: string;
    availableTimeStamps: number[];
  };
}

class TimeMap {
  myMap: TimeStampMap;

  constructor() {
    this.myMap = {};
  }

  set(key: string, value: string, timestamp: number): void {
    const target = this.myMap[key];
    if (target) {
      target[timestamp] = value;
      target.availableTimeStamps.push(timestamp);
    } else {
      this.myMap[key] = {
        [timestamp]: value,
        availableTimeStamps: [timestamp],
      };
    }
  }

  getPreviousTimestamp(arr: number[], target: number): number {
    let left = 0,
      right = arr.length - 1;

    if (target < arr[0]) {
      return -1;
    }
    while (left <= right) {
      const mid = Math.floor((left + right) / 2);

      if (arr[mid] > target) {
        right = mid - 1;
      } else if (arr[mid] < target) {
        left = mid + 1;
      } else {
        return arr[mid];
      }
    }
    return arr[right];
  }

  get(key: string, timestamp: number): string {
    const target = this.myMap[key];
    if (target) {
      let ans = target[timestamp];

      if (ans) {
        return ans;
      }

      const { availableTimeStamps } = target;
      const previous = this.getPreviousTimestamp(
        availableTimeStamps,
        timestamp,
      );
      return target[previous] ?? "";
    }
    return "";
  }
}

const timeMap = new TimeMap();
timeMap.set("foo", "bar", 3);
console.log(timeMap.get("foo", 1));
console.log(timeMap.get("foo", 3));
timeMap.set("foo", "bar2", 4);
console.log(timeMap.get("foo", 4));
console.log(timeMap.get("foo", 5));
