class Solution:
    def intToRoman(self, num: int) -> str:
        
        converted = ""


        def get_num_index(n, roms, nums):

            if n >= 14 and n <= 39:
                return 'X', 10

            for i in range(len(nums)-1):
                if (nums[i]<=n and nums[i+1]>n):    
                    return roms[i], nums[i]
            return 'M', 1000


        roms = ['I','IV','V','VI','IX','X','XI','XL','L','XC','C','CD','D','CM','M']
        nums = [1, 4, 5, 6, 9, 10, 11, 40, 50, 90, 100, 400, 500, 900, 1000]

        rem = -1

        while rem != 0:

            max_rom, max_num = get_num_index(num, roms, nums)

            quo, rem = divmod(num, max_num)

            converted = converted+ max_rom*quo

            num = rem
            print("converted so far", converted, "remainder", rem)
        
        return converted

        
