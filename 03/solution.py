"""Solution by <USERNAME>."""

from typing import List


class Solution:
    """Winner of an election."""

    def winner(self, V: List[int]) -> int: # pylint: disable=C0103
        """Solution to problem."""
        minVotes=0
        for e in V:
            total = V.count(e)
            if total > minVotes:
                winner = e
                minVotes=total
        return winner
