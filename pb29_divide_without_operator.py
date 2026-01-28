class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        #solution courtesy : professor0akes youtube

        INT_MIN = -1* (2**31) 
        INT_MAX = 2**31 - 1 

        quotient = 0

        return_sign = 1 if ((divisor > 0) == (dividend > 0)) else -1

        res = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            quotient = dividend
        else:
            while(dividend >= divisor):
                
                temp_divisor, multiple = divisor, 1
                #move to next 10th digit and check if divisible eg: 100 / 2 -> check if 100/20 -> check if 100/ 200 then stop and set multiple to 10
                while(dividend >= (temp_divisor<<1)):
                    temp_divisor <<=1
                    multiple <<=1
                
                dividend -= temp_divisor
                quotient += multiple

        quotient = (~quotient+1 if return_sign==-1 else quotient)
        

        print("quotient is ", quotient, INT_MAX, INT_MIN)

        if quotient > INT_MAX:
            return INT_MAX
        elif return_sign == -1 and quotient <  INT_MIN:
            quotient = INT_MIN 
        
                    
        return quotient