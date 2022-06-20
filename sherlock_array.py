#!/usr/bin/env python

"""
Watson gives Sherlock an array of integers.
His challenge is to find an element of the array such that the sum of all
elements to the left is equal to the sum of all elements to the right.
"""

import pytest


def sherlock_array(arr: list[int]) -> str:
    for idx in range(len(arr) - 1):
        if sum(arr[:idx]) == sum(arr[idx + 1:]):
            return 'YES'

    return 'NO'


def sherlock_array1(arr: list[int]) -> str:
    right_sum = sum(arr)
    left_sum = 0

    for i in arr:
        right_sum -= i
        if left_sum == right_sum:
            return 'YES'
        left_sum += i

    return 'NO'


FUNCS = pytest.mark.parametrize('f', (sherlock_array, sherlock_array1),)


@FUNCS
def test_f(f):
    assert f([5, 6, 8, 11]) == 'YES'
