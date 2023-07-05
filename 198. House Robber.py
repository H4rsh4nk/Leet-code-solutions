class Solution:
    def rob(self, nums: List[int]) -> int:
        ind = len(nums) - 3
        nums.append(0)
        while ind >= 0:
            nums[ind] = nums[ind] + max(nums[ind+2], nums[ind+3])
            ind = ind - 1
        return max(nums[0], nums[1])
