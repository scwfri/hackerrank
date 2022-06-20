#!/usr/bin/env python

import collections
import string


def caesar_cipher(cipher: str, rotation: int) -> str:
    alphabet = collections.deque(string.ascii_lowercase)
    rotated = collections.deque(string.ascii_lowercase)
    rotated.rotate(-rotation)

    encrypted = ''
    for c in cipher:
        if c.lower() not in alphabet:
            encrypted += c
        else:
            is_upper = c.isupper()
            char = rotated[alphabet.index(c.lower())]
            encrypted += (char.upper() if is_upper else char)

    return encrypted


def run():
    plain_text = 'middle-Outz'
    print(f'{plain_text=}')
    print(f'{caesar_cipher(plain_text, 2)=}')


if __name__ == '__main__':
    raise SystemExit(run())
