class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        import itertools
        dig_comb_val = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        dig_comb_keys = ['2','3','4','5','6','7','8','9']

        dig_comb = dict(zip(dig_comb_keys, dig_comb_val))

        prev_comb = [ x for x in dig_comb[digits[0]] ]

        for comb_ind in range(1, len(digits)):

            dig = digits[comb_ind]
            prev_comb = [[ (j+i) for i in dig_comb[dig]] for j in prev_comb]
            prev_comb = list(itertools.chain.from_iterable(prev_comb))
        
        

        return prev_comb
        
        