class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #solution courtesy : professor_0akes yt
        def find_left_most(nums, target):
            left, right = 0, len(nums)-1
            while(left<=right):
                mid = left + (right-left)//2

                if nums[mid] == target:
                    right = mid-1
                elif nums[mid] <target:
                    left = mid+1
                else:
                    right = mid-1
            return left
        
        def find_right_most(nums, target):
            left, right = 0, len(nums)-1
            while(left<=right):
                mid = left + (right-left)//2
                if nums[mid] == target:
                    left = mid+1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return right
        
        left_most_target = find_left_most(nums, target)
        right_most_target = find_right_most(nums, target)

        if left_most_target <= right_most_target:
            return left_most_target, right_most_target
        else:
            return -1, -1
        
        
