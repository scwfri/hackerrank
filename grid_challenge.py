#!/usr/bin/env python

def grid_challenge(grid: list[str]) -> str:
    sorted_grid = [sorted(list(row)) for row in grid]

    for idx in range(len(sorted_grid[0])):
        prev_char = sorted_grid[0][idx]
        for row in sorted_grid:
            if row[idx] < prev_char:
                return 'NO'
            else:
                prev_char = row[idx]

    return "YES"


def test_grid_challenge():
    assert grid_challenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']) == 'YES'
    assert grid_challenge(['zxy', 'abc']) == 'NO'
    assert grid_challenge(['zja', 'akz']) == 'YES'
