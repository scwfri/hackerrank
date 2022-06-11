#!/usr/bin/env python

import itertools


def max_profit2(prices: list[int]) -> int:
    max_profit = 0
    buy_price = prices[0]
    for sell_price in prices:
        max_profit = max(max_profit, sell_price - buy_price)
        buy_price = min(buy_price, sell_price)

    print(max_profit)
    return max_profit


def max_profit(prices: list[int]) -> int:
    it = itertools.combinations(prices, 2)
    max_profit = max(0, max(sell - buy for buy, sell in it))
    print(max_profit)
    return(max_profit)


if __name__ == "__main__":
    max_profit([7, 1, 5, 3, 6, 4])
    max_profit2([7, 1, 5, 3, 6, 4])
