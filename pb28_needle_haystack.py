class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        hay_len = len(haystack)
        ned_len = len(needle)

        if ned_len > hay_len:
            return -1
        
        if ned_len == hay_len:
            
            if haystack != needle:
                return -1
            else:
                return 0
        
        j = 0 
        for i in range(0, hay_len-ned_len+1):

            if haystack[j: j+ned_len] == needle:
                return j
            
            j+=1
        
        return -1
