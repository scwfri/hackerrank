#!/usr/bin/env python
"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]



Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length
"""


def window_max_easy(nums: list[int], k: int) -> list[int]:
    sliding_max = []
    left = 0
    right = k

    while right <= len(nums):
        sliding_max.append(max(nums[left:right]))
        left += 1
        right += 1

    print(sliding_max)
    return sliding_max


def window_max_optimized(nums: list[int], k: int) -> list[int]:
    if not nums:
        return []

    sliding_max = []
    left = 1
    right = k + 1
    print(f'append {max(nums[0:k])}')
    sliding_max.append(max(nums[0:k]))
    while right <= len(nums):
        compare_max = sliding_max[-1]
        if compare_max == nums[left - 1]:
            if nums[left] >= compare_max - 1:
                compare_max = max(nums[left], nums[right - 1])
            else:
                compare_max = max(nums[left:right])
        else:
            compare_max = max(compare_max, nums[right - 1])

        sliding_max.append(compare_max)
        left += 1
        right += 1

    print(sliding_max)
    return sliding_max


if __name__ == '__main__':
    window_max_optimized([1, 3, -1, -3, 5, 3, 6, 7], 3)
    window_max_optimized([1], 1)
    window_max_optimized([1, -1], 1)
    window_max_optimized([1, 3, 1, 2, 0, 5], 3)
    window_max_optimized([-7, -8, 7, 5, 7, 1, 6, 0], 4)
