class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            x=str(x)
            new = x[::-1]
            
            if x==new:
                return True
            else:
                return False
