def set_i_th_bit(n: int, i: int) -> int:
    return n | (1 << i)


def check_i_th_bit(n: int, i: int) -> bool:
    return (n & (1 << i)) != 0


def unset_i_th_bit(n: int, i: int) -> int:
    if check_i_th_bit(n, i):
        return n ^ (1 << i)
    return n


def count_set_bits(n: int) -> int:
    ans = 0
    for i in range(32):  # assuming 32 bit integers
        ans += check_i_th_bit(n, i)
    return ans


n = int(input("Enter N: "))
i = int(input("Enter i: "))

print("n =", bin(n))
print(f"On setting bit-{i}:", bin(set_i_th_bit(n, i)))
print(f"{i}th bit in {n} is:", check_i_th_bit(n, i))
print(f"On unsetting {i}th bit in {bin(n)[2:]}:", bin(unset_i_th_bit(n, i)))
print(f"set bits in {bin(n)} is: {count_set_bits(n)}")
