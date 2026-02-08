class Solution:
    def longestValidParentheses(self, s: str) -> int:

        #refered to professor0akes solution on yt but solved myself lol
        stack = ['' for i in range(len(s))]
        sp = 0
        inner_bracket = False
        for sym in s:
            
            if sym == '(' and stack[sp] == '':
                stack[sp] = '('
                sp +=1
            elif sym == ')' and sp>0:
                # and stack[sp-1] == '(':
                #stack[sp-1] = '()'
                if stack[sp-1] == '(':
                    stack[sp-1] = '()'
                elif stack[sp-1] == '()':
                    j = sp-1
                    inner_bracket = False
                    while(j>=0):
                        if stack[j] == '()':
                            j-=1
                        elif stack[j] == '(':
                            stack[j] = '()'
                            break
                        else:
                            sp+=1
                            break
                    if j<0:
                        sp+=1
                
            # print("stack after adding symbol ", sym, "is ", stack)

        print(stack)
        max_len = 0
        cur_max_len = 0
        for item in stack:
            if item == '()':
                cur_max_len +=2
            else:
                max_len = max(max_len, cur_max_len)
                cur_max_len = 0
        
        return max_len

