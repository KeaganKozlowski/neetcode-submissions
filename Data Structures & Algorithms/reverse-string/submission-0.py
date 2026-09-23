class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p0, p1 = 0, len(s) - 1
        while p0 < p1:
            s[p0], s[p1] = s[p1], s[p0]
            p0 += 1
            p1 -= 1
        
        