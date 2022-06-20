#!/usr/bin/env python3

from typing import List

import itertools
import collections


def count_turns(book: List[int], target_page: int):
    book_it = iter(book)
    page_turns = 0
    for page in book_it:
        try:
            pages = (page, next(book_it))
        except StopIteration:
            pages = (page, 0)

        print(f'{pages=}')
        if target_page in pages:
            return page_turns
        else:
            page_turns += 1


def page_count(pages: int, target_page: int) -> int:
    book = list(range(0, pages + 1))
    print(book)
    turns_forward = count_turns(book, target_page)
    turns_backward = count_turns(list(reversed(book)), target_page)
    return min(turns_forward, turns_backward)


def page_count2(pages: int, target_page: int) -> int:
    book_pages = pages // 2
    pages_to_target = target_page // 2

    return min(pages_to_target, (book_pages - pages_to_target))

def run():
    print(page_count2(8, 5))


if __name__ == '__main__':
    raise SystemExit(run())
