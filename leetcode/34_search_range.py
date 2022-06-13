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


def search_range(nums: list[int], target: int) -> list[int]:
    if not nums:
        return [-1, -1]

    res = [-1, -1]
    low = 0
    nums_len = len(nums)
    high = nums_len - 1
    idx = -1
    while low <= high:
        mid = (low + high) // 2
        print(f"{mid=}, {low=}, {high=}")
        if mid >= nums_len:
            break
        if nums[mid] == target:
            idx = mid
            break
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    lower_idx = idx
    upper_idx = idx

    while lower_idx >= 0 and nums[lower_idx] == target:
        res[0] = lower_idx
        lower_idx -= 1

    while upper_idx < nums_len and nums[upper_idx] == target:
        res[1] = upper_idx
        upper_idx += 1

    print(f"input: {nums=}, {target=}")
    print(res)
    return res


if __name__ == "__main__":
    assert search_range([5, 7, 7, 7, 8, 10], 8) == [4, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
    assert search_range([1], 1) == [0, 0]
    assert search_range([2, 2], 3) == [-1, -1]
