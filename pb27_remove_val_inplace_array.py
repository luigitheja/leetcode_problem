class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        

        output_wo_val = []

        for i in range(len(nums)):

            if nums[i] != val:
                output_wo_val.append(nums[i])

        
        for i in range(len(nums)):
            if i < len(output_wo_val):
                nums[i] = output_wo_val[i]
            else:
                nums[i] = '_'
        
        return len(output_wo_val)
        
