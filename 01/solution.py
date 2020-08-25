"""Solution by <USERNAME>."""

from typing import List


class Solution:
    """Combining the conquered!"""

    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None: # pylint: disable=C0103
        """Solution to problem."""
        for i in range(0,n):
            A[m+i]=B[i]
        A.sort()