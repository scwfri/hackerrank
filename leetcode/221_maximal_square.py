#!/usr/bin/env python

def maximal_square(matrix: list[list[str]]) -> int:
    i = 0
    j = 0
    m = len(matrix)
    n = len(matrix[0])
    while i < m:
        while j < n:
            if matrix[i][j] != "0":
                if i == 0 or j == 0:
                    matrix[i][j] = int(matrix[i][j])
                else:
                    up = matrix[i - 1][j]
                    diag = matrix[i - 1][j - 1]
                    left = matrix[i][j - 1]
                    adjacent = min(int(up), int(diag), int(left))
                    matrix[i][j] = adjacent + int(matrix[i][j])
            else:
                matrix[i][j] = int(matrix[i][j])
            j += 1

        i += 1
        j = 0

    print(matrix)
    max_square = max(i for j in matrix for i in j) ** 2
    print(max_square)
    return max_square


if __name__ == "__main__":
    assert maximal_square([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]) == 4
    assert maximal_square([["0", "1"], ["1", "0"]]) == 1
    assert maximal_square([["1", "1"], ["1", "1"]]) == 4
