#!/usr/bin/env python3

import itertools
import collections


def max_min2(arr: list[int], arr_len: int) -> int:
    arr.sort()
    i = 0
    min_unfairness = arr[i + arr_len - 1] - arr[i]
    while i <= (len(arr) - arr_len):
        min_unfairness = min(min_unfairness, arr[i + arr_len - 1] - arr[i])
        i += 1

    return min_unfairness


def max_min(arr: list[int], arr_len: int) -> int:
    arr_perms = itertools.permutations(arr, arr_len)

    arr_perm = next(arr_perms)
    min_unfairness = max(arr_perm) - min(arr_perm)
    for arr_perm in arr_perms:
        min_unfairness = min(min_unfairness, max(arr_perm) - min(arr_perm))

    return min_unfairness


def run():
    print(max_min2([1, 2, 3, 4, 10, 20, 30, 40, 100, 200], 4))


if __name__ == '__main__':
    raise SystemExit(run())
