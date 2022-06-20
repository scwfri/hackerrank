#!/usr/bin/env python3

import pandas as pd


def get_segments(bar: list[int], slen: int) -> list[int]:
    for i in range(0, len(bar)):
        yield bar[i:i + slen]


def run(bar: list[int], day: int, month: int) -> int:
    segments = get_segments(bar, month)
    count = 0
    for s in segments:
        if sum(s) == day:
            count += 1

    return count


if __name__ == '__main__':
    exit(print(run([2, 2, 1, 3, 2], 4, 2)))
