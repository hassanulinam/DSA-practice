def power(A: int, B: int) -> int:
    if B < 0:
        raise ValueError("Only positive powers accepted")
    if B == 0:
        return 1
    if B == 1:
        return A

    half = power(A, B // 2)
    if B % 2 == 0:
        return half * half
    return A * half * half


A = int(input("Enter A: "))
B = int(input("Enter B: "))
print(f"{A} power {B} = {power(A, B)}")
