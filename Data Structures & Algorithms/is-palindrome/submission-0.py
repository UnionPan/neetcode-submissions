class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(filter(str.isalnum, s)).lower()
        
        left, right = 0, len(filtered)-1
        while left < right:
            if left != right and filtered[left] != filtered[right]:
                return False
            elif left == right:
                return True
            else:
                left += 1
                right -= 1
        
        return True 