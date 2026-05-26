class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while n != 1 and count < 15:
            k = [int(e) for e in str(n)]
            n = sum(map(lambda x: x * x, k))
            count += 1
        if n == 1:
            return True
        return False

        