class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplets = {}
        for i in range(len(nums)-2):
            
            l = i+1
            r = len(nums)-1

            while l<r:

                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum < 0:
                    l+=1
                elif three_sum > 0:
                    r-=1
                else:
                    triplets[(nums[i], nums[l], nums[r])] =1
                    l+=1
                    r-=1
        
        unique_triplets = [list(x) for x in list(triplets.keys())]

        return unique_triplets