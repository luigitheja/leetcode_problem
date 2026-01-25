class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # solution derived from youtube -> professor oaks 

        output_list = []

        def backtrack(s, n, open, close):

            if len(s) == 2*n :
                output_list.append(s)
                return

            if open < n:
                backtrack(s+'(', n, open+1, close)
            
            #pruning happens here
            if close < open:
                backtrack(s+')', n, open, close+1)

        backtrack('', n, 0, 0)

        return output_list