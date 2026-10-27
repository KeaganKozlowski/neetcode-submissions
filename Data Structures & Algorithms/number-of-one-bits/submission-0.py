class Solution:
    def hammingWeight(self, n: int) -> int:
        nb, total = str(bin(n)), 0
        for e in nb:
            if e == '1':
                total += 1
        return total

        