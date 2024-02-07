class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        result = 0
        l, r = 0 , len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            result = max(result, area)
        
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result


sol = Solution()




height = [1,8,6,2,5,4,8,3,7]

print(sol.maxArea(height))
# first to find max value
# second to find big value located from the max value