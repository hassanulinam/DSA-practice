def print_n_numbers(n):
    if n == 0:
        print()
        return

    print_n_numbers(n - 1)
    print(n, end=" ")


n = int(input("Enter n: "))
print_n_numbers(n)
