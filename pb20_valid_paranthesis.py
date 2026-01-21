class Solution:
    def isValid(self, s: str) -> bool:
        
        open_close = {
            ')':'(', ']':'[','}':'{'
        }

        stack = []

        for ch in s:

            if ch in open_close.keys():
                if len(stack) == 0:
                    return False

                item = stack.pop()
                if item != open_close[ch]:
                    return False
            elif ch in open_close.values():
                stack.append(ch)
        
        if len(stack) > 0:
            return False
        
        return True
                    