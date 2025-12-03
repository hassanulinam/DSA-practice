# // Rotate give array from right to left

from MyUtils import rotate_arr_ltr, rotate_arr_rtl


def main():
    arr = [int(x) for x in input("Enter arr: ").split()]
    k = int(input("Enter no.of rotations: "))
    direction = int(input("(1.RTL  2.LTR) Enter Direction: "))
    if direction == 1:
        rotate_arr_rtl(arr, k)
    else:
        rotate_arr_ltr(arr, k)
    print(arr)


if __name__ == "__main__":
    main()
