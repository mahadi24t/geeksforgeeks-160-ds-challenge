"""
╔══════════════════════════════════════════════════════════════╗
║         GeeksforGeeks - 160 Days of Problem Solving          ║
╠══════════════════════════════════════════════════════════════╣
║  Problem    : Reverse an Array                               ║
║  Link       : https://www.geeksforgeeks.org/batch/           ║
║               gfg-160-problems/track/arrays-gfg-160/         ║
║               problem/reverse-an-array                       ║
║  Difficulty : Easy                                           ║
║  Topic      : Arrays                                         ║
╠══════════════════════════════════════════════════════════════╣
║  Approach   : Python built-in list.reverse()                 ║
║               Uses CPython's internal C-level routine to     ║
║               reverse the list in place - no extra space,    ║
║               no manual swapping needed.                     ║
╠══════════════════════════════════════════════════════════════╣
║  Time  Complexity : O(n) - visits each element exactly once  ║
║  Space Complexity : O(1) - in-place, no auxiliary space used ║
╚══════════════════════════════════════════════════════════════╝
"""


class Solution:
    def reverseArray(self, arr):
        arr.reverse()
