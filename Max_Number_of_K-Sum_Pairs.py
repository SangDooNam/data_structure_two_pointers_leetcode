class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        
        count = 0
        for num in nums:
            complement = k - num
            if num_counts.get(num, 0) > 0 and num_counts.get(complement, 0) > (1 if num == complement else 0):
                count += 1
                num_counts[num] -= 1
                num_counts[complement] -= 1
        return count



# nums = [1,2,3,4]
# k = 5

# nums = [3,1,3,4,3]
# k = 6

# nums =[3,1,5,1,1,1,1,1,2,2,3,2,2]
# k = 1

nums =[4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2

nums =[2,2,2,3,1,1,4,1]
k = 4

# sol = Solution()
# print(sol.maxOperations(nums, k))

