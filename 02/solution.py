"""Solution by <USERNAME>."""

from typing import List


class Solution:
    """Sigma transformation."""

    def sigma_transformation(self, A: List[int]) -> List[int]: # pylint: disable=C0103
        """Solution to problem."""
        if len(A) <= 1:
            return A
        else:
            for i in range(1,len(A)):
                A=self.calculo(A,i)
                print(A)
            return A

    def calculo(self, A: List[int], i: int) -> List[int]:
        A[i] = A[i]+ A[i-1]
        return A
                
