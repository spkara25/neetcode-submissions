class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_int = int('{:032b}'.format(n)[::-1], 2)
        return reversed_int
