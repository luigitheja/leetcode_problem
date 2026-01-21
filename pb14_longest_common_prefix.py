class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs == []:
            return ""

        prefix_ends = True

        i=0
        prefix = previous_prefix = ""
        while i< len(strs[0]): 
            i+=1
            previous_prefix = prefix
            prefix = strs[0][:i]
            if not all([s.startswith(prefix)  for s in strs]):
                return previous_prefix
        
        return prefix