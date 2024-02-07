class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        length = len(s)
        if length == 0:
            return True
        s_idx = 0
        
        for t_idx in range(len(t)):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
                if s_idx == length:
                    return True 
        
        return False
    

sol = Solution()

# s = "abc"
# t = "ahbgdc"

# s = "axc"
# t = "ahbgdc"

s ="b"
t ="abc"

print(sol.isSubsequence(s, t))