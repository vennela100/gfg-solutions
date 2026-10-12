class Solution:
    def reverse(self, x: int) -> int:
        a=str(abs(x))
        return int(a[::-1])
        