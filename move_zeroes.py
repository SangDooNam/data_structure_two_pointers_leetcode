# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         length = len(nums)
#         count, idcs = 0, []
#         while count < length:
#             if nums[count] == 0:
#                 idcs.append(count)
#                 nums.append(nums[count])
#             count +=1 
            
#         for idx in reversed(idcs):
#             del nums[idx]

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
                


sol = Solution()



nums = [0,1,0,3,12]
#nums = [0,0,1]
#nums = [0]
sol.moveZeroes(nums)

print(nums)