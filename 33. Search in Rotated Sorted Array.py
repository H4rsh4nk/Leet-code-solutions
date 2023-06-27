def main():
    class Solution:
        def search(self, nums: list[int], target: int) -> int:
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                mid_num = nums[mid]
                left_num = nums[left]
                right_num = nums[right]
                print(left_num, right_num, mid_num, target)

                if target == mid_num or target == right_num or target == left_num:
                    if  target == mid_num:
                        return mid
                    elif target == left_num:
                        return left
                    else:
                        return right
                
                #shifted
                if left_num < right_num:
                    if target <= mid_num:
                        right = mid 
                    else:
                        left = mid + 1
                #unshifted
                else:
                    if target > left_num:
                        if mid_num > left_num:
                            if target < mid_num: 
                                right = mid
                            else:
                                left = mid + 1
                        else:
                            right = mid - 1
                    elif target < right_num:
                        if mid_num < right_num:
                            if target <= mid_num:
                                right = mid 
                            else: 
                                left = mid + 1
                        else:
                            left = mid + 1
                    else:
                        return -1
            
            return -1

    # Example usage
    nums = [8,9,2,3,4]
    target = 9
    solution = Solution()
    result = solution.search(nums, target)
    print(result)

if __name__ =='__main__':
    main()