class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = {}
        count = 0

        for i in range(len(nums)):
            if nums[i - count] in l:
                nums.pop(i - count)
                count += 1
            else:
                l[nums[i - count]] = 1
        print(nums)
        return (len(nums))