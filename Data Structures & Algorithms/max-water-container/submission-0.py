class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        i, j = 0, len(heights) - 1
        while i < j:
            temp = (j - i) * min(heights[i], heights[j])
            if temp > volume:
                volume = temp
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return volume

        