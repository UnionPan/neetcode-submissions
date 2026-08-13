class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        pre = 1
        su = 1
        res = []
        for i in range(len(nums)):

            prefix.append(pre)
            
            pre = pre * nums[i]
            suffix.append(su)
            
            su = su * nums[len(nums)-1-i]

        #print(prefix, suffix)
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[len(nums)-1-i])
        
        return res