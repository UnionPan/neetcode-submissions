class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        starts = {}
        suffix = {}
        res = 1
        num_set = set(nums)
        for i, n in enumerate(nums):
            if n-1 not in num_set:
                starts[n] = n+1
        
        
        for start in starts:
            length = 1
            while True:
                if start+1 in num_set:
                    start = start+1
                    length = length +1
                else:
                    break
            
            
            res = max(res, length)
        

        return res