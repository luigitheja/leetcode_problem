class Solution:
    def romanToInt(self, s: str) -> int:
        i=0
        convert_map = {
            'I':1,
            'V':5,
            'X':10,
            'L':50, 
            'C':100,
            'D':500,
            'M':1000
        }

        int_num = 0

        while(i< len(s)):
            
            cur_char = s[i]

            count = convert_map.get(cur_char) 

            if not count:
                return 0
            
            if cur_char == 'I' and (i+1 < len(s)) and s[i+1] == 'V':
                count = 4
                i+=1
            if cur_char == 'V' and (i+1 < len(s)) and s[i+1] == 'I':
                count = 6
                i+=1
            if cur_char == 'I' and (i+1 < len(s)) and s[i+1] == 'X' :
                if i+2 < len(s) and s[i+2] in ['V', 'X']:
                    count = 10
                else:
                    count = 9
                    i+=1
            if cur_char == 'X' and (i+1 < len(s)) and s[i+1] == 'I':
                if i+2 < len(s) and s[i+2] in ['V', 'X']:
                    count = 10
                else:
                    count = 11
                    i+=1
            if cur_char == 'X' and (i+1 < len(s)) and s[i+1] == 'L':
                count = 40
                i+=1
            if cur_char == 'X' and (i+1 < len(s)) and s[i+1] == 'C':
                count = 90
                i+=1
            if cur_char == 'C' and (i+1 < len(s)) and s[i+1] == 'D':
                count = 400
                i+=1
            if cur_char == 'C' and (i+1 < len(s)) and s[i+1] == 'M':
                count = 900
                i+=1
            
            int_num += count
            print("adding count", count)

            i+=1
        
        # print("the converted integer is ", int_num)

        return int_num