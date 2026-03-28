# In the given array, all the elements are repeating twice, expect 2. Find out those 2 numbers.

# solution idea: on xor-all --> 2 non-repeating numbers xor will be done.
# in the resultant xor, whichever the bit is 1, find the position., that means, at that ith-bit, our 2 unique numbers bit values were different.
# so, we divide the array elements into 2 buckets based on that ith-bit., and find out the unique element in that bucket.


def check_i_th_bit(n: int, i: int) -> bool:
    return n & (1 << i) != 0


arr = list(map(int, input("Enter arr: ").split()))
xor_all = 0
for val in arr:
    xor_all ^= val

diff_bit = 0  # i-th bit where in final xor bit value is 1
while not check_i_th_bit(xor_all, diff_bit):
    diff_bit += 1

print(f"xor_all: {bin(xor_all)}, i: {diff_bit}")
u1, u2 = 0, 0
for val in arr:
    if check_i_th_bit(val, diff_bit):
        u1 ^= val
    else:
        u2 ^= val

print(u1, u2)
