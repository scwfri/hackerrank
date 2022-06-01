#!/usr/bin/env python3

import itertools
import collections


def get_sock_pairs(count: int, socks: list[int]) -> int:
    sock_count = collections.Counter(socks)
    sock_pairs = 0
    for color in sock_count:
        sock_pairs += sock_count[color] // 2

    return(sock_pairs)


def run():
    print(get_sock_pairs(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))


if __name__ == '__main__':
    raise SystemExit(run())
