def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)


def get_proper_divisors(n):
    divisors = get_divisors(n)
    divisors.remove(n)
    return divisors


def is_perfect(n):
    return sum(get_proper_divisors(n)) == n