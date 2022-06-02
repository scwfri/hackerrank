#!/usr/bin/env python3

import itertools
import collections


def tower_breaker(towers: int, height: int) -> int:
    have_winner = 0
    players = collections.deque([1, 2])
    towers = [height] * towers

    while not have_winner:
        player_move = players[0]
        print(current_move)
        players.rotate()

        for tower in towers:


        have_winner += 1

    return player_move


def run():
    print(tower_breaker(2, 2))


if __name__ == '__main__':
    raise SystemExit(run())
