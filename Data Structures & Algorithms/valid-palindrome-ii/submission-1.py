class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        p0, p1, nomatch = 0, len(s) - 1, []
        while p0 < p1:
            if s[p0] != s[p1]:
                nomatch.append(s[:p0]+s[p0+1:])
                nomatch.append(s[:p1]+s[p1+1:])
                break
            else:
                p0 += 1
                p1 -= 1
        for match in nomatch:
            if match == match[::-1]:
                return True
        return False

        