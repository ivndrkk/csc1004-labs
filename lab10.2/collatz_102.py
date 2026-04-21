def collatz(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    print(sequence)
    return sequence

if __name__ == "__main__":
    print(collatz(6))
    print(collatz(19))
    print(collatz(1))