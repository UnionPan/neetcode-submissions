class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        offset = {}
        for i, n in enumerate(nums):
            
            if target - n in offset and offset[target-n] != i:  
                return [offset[target-n], i]
            
            offset[n] = i
        
        