class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left] > nums[right]:
                # rotated array
                mid = (left + right) // 2
                print(left, right, mid)
                # if nums[mid] < nums[left]:
                # you hit the new low [.....low,.....]
                temp = nums[mid]
                if target < temp:
                    # [....,temp,.....target,......]
                    if target <= nums[right]:
                        if target == nums[right]:
                            return right
                        else:
                            left = mid + 1
                    # [....,target,.....temp,......]
                    elif target >= nums[left]:
                        if target == nums[left]:
                            return left
                        else:
                            right = mid - 1
                    else:
                        print("firzt")
                        return -1
                elif target > temp:
                    # [....,temp,.....target,......]
                    # right = mid - 1
                    if target <= nums[right]:
                        if target == nums[right]:
                            return right
                        else:
                            if temp < nums[right]:
                                left = mid + 1
                            else:
                                right = mid - 1

                    elif target >= nums[left]:
                        if target == nums[left]:
                            return left
                        else:
                            if temp < nums[left]:
                                right = mid - 1
                            else:
                                left = mid + 1
                    else:

                        print("second")
                        return -1
                else:
                    return mid
            else:

                # sorted normal binary search
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                elif target == nums[mid]:
                    return mid
                else:
                    print("THRID")

                    return -1
        print(left, right)
        print("FOURTH")

        return -1
