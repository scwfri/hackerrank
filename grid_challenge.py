#!/usr/bin/env python

def run(grid: list[str]) -> str:
    sorted_grid = [sorted(list(row)) for row in grid]

    for idx in range(len(sorted_grid[0])):
        prev_char = sorted_grid[0][idx]
        for row in sorted_grid:
            if row[idx] < prev_char:
                return 'NO'
            else:
                prev_char = row[idx]

    return "YES"


if __name__ == '__main__':
    assert run(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']) == 'YES'
    assert run(['zxy', 'abc']) == 'NO'
    assert run(['zja', 'akz']) == 'YES'
