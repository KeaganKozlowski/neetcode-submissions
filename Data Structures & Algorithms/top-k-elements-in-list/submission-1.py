class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        ret = []
        for e in nums:
            if e not in dic:
                dic[e] = 1
            else:
                dic[e] += 1
        for i in range(k):
            t = max(dic, key=dic.get)
            ret.append(t)
            dic[t] = 0
        return(sorted(ret))



            
        
        