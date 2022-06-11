#!/usr/bin/env python
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

"""


def two_sum(nums: list[int], target: int) -> list[int]:
    ts_lst = []
    i = 0
    j = i + 1
    nums_len = len(nums)
    while i < nums_len - 1:
        while j < nums_len:
            if nums[i] + nums[j] == target:
                ts_lst = [j, i]
                print(ts_lst)
                return ts_lst
            else:
                j += 1
        i += 1
        j = i + 1


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) in ([0, 1], [1, 0])
    assert two_sum([0, 4, 3, 0], 0) in ([0, 3], [3, 0])
