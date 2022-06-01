#!/usr/bin/env python3

a = [1, 0]
b = [2, 0]
x = 1


def run(a: list, b: list, x: int) -> bool:
    a = sorted(a)
    b = sorted(b)

    if len(a) != len(b):
        return False

    for i, xs in enumerate(a, 1):
        if (b[-i] + xs) < x:
            return False

    return True


if __name__ == "__main__":
    print(run([1, 2, 2, 1], [3, 3, 3, 4], 5))
