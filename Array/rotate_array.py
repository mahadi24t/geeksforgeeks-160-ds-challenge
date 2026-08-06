"""
================================================================================
Problem Name  : Rotate Array
Problem Link  : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/
                arrays-gfg-160/problem/rotate-array-by-n-elements-1587115621
Difficulty    : Medium
--------------------------------------------------------------------------------
Approach      : Reversal Algorithm
                1. Reduce d using d % n to handle d >= n cases.
                2. Reverse the first d elements.
                3. Reverse the remaining n-d elements.
                4. Reverse the entire array.
                Result is a left rotation by d steps.
--------------------------------------------------------------------------------
Time  Complexity: O(n) — three in-place reversals, each traversing O(n).
Space Complexity: O(1) — no extra space used; all operations are in-place.
================================================================================
"""


class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n

        self._reverse(arr, 0, d - 1)
        self._reverse(arr, d, n - 1)
        self._reverse(arr, 0, n - 1)

    @staticmethod
    def _reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
