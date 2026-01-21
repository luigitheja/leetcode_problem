class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # nums = list(set(nums))

        nums.sort()

        results = []

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):

                l = j+1
                r = len(nums)-1
                
                while(l < r):

                    cur_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if cur_sum < target:
                        l+=1
                    elif cur_sum > target:
                        r-=1
                    else:
                        if [nums[i] , nums[j] , nums[l] , nums[r]] not in results:
                            results.append([nums[i] , nums[j] , nums[l] , nums[r]])
                        l+=1
                        r-=1
        
        
        return results


