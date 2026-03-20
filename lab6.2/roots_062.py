#!/usr/bin/env python3
import sys
import math


def get_roots(a, b, c):
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return None

    sqrt_d = math.sqrt(discriminant)
    r1 = (-b - sqrt_d) / (2 * a)
    r2 = (-b + sqrt_d) / (2 * a)

    return sorted([r1, r2])


def main():
    for line in sys.stdin:
        a, b, c = map(float, line.split())
        roots = get_roots(a, b, c)

        if roots is None:
            print("None")
        else:
            print(f"{roots[0]:.1f}, {roots[1]:.1f}")


if __name__ == "__main__":
    main()