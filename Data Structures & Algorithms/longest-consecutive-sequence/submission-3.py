class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        arr = sorted(list(set(nums)))
        res, total = 1, 1
        for i in range(1, len(arr)):
            if arr[i-1] + 1 == arr[i]:
                total += 1
            else:
                res = max(res, total)
                total = 1
        return max(res, total)