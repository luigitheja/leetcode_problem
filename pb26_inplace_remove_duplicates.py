class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        output = []
        
        for num in nums:
            if num not in output:
                output.append(num)
        
        for i in range(len(nums)):
            if i < len(output):
                nums[i] = output[i]
            else:
                nums[i] = '_'
            



        return len(output)