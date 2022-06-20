#!/usr/bin/env python

"""
We define super digit of an integer

using the following rules:

Given an integer, we need to find the super digit of the integer.

    If x has only digit, then its super digit is x.

Otherwise, the super digit of x
is equal to the super digit of the sum of the digits of x.
"""

import pytest


def super_digit(n: str, k: int) -> int:
    s = sum(int(i) for i in n) * k
    n = str(s)
    while len(n) > 1:
        s = sum(int(i) for i in n)
        n = str(s)
    return int(n)


FUNCS = pytest.mark.parametrize('f', (super_digit,),)


@FUNCS
def test_f(f):
    assert f('9875', 4) == 8
    assert f('148', 3) == 3
    assert f('123', 3) == 9
