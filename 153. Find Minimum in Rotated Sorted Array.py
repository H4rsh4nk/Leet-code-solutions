class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] > nums[right]:
                mid = (left + right) // 2
                if nums[mid] > nums[left]:
                    left = mid + 1
                elif nums[mid] < nums[right]:
                    right = mid
                else:
                    left = left +1 
            else:
                return nums[left]
            