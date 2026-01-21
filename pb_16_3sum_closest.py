class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        sums = {}
        for i in range(len(nums)-2):
            
            l = i+1
            r = len(nums)-1

            while l<r:

                three_sum = (nums[i] + nums[l] + nums[r])
                # print("checking ", nums[i] , nums[l] , nums[r])
                if three_sum < target:
                    l+=1
                elif three_sum > target:
                    r-=1
                else:
                    l+=1
                    r-=1
                
                three_sum_str = str(three_sum)

                sums[three_sum_str] = 1
                

        all_sums = [int(x) for x in (sums.keys())]

        diff_from_tgt = (target - all_sums[0]) if target > all_sums[0] else (all_sums[0] - target)
        sum_min = all_sums[0]    

        # print("all sums ", all_sums)    
        
        for cur_sum in all_sums:

            cur_diff_from_tgt = (target - cur_sum) if target > cur_sum else (cur_sum - target)

            # print(("cur sum", cur_sum, "current differnce from target", cur_diff_from_tgt,"previous_diff from target", diff_from_tgt))

            if diff_from_tgt > cur_diff_from_tgt:
                diff_from_tgt =  cur_diff_from_tgt
                sum_min = cur_sum
        
        return sum_min


