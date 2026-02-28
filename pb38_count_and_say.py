class Solution:
    def countAndSay(self, n: int) -> str:

        def get_rle(num):

            if num == 1:
                return '1'
            
            else:
                prev_num = '-'
                enc_counts = []
                rle = ""
                for ch in get_rle(num-1):

                    if prev_num != ch:
                        prev_num = ch
                        enc_counts.append((1,ch))
                    else:
                        enc_counts[-1] = ( (enc_counts[-1][0]+1), enc_counts[-1][1])
                
                for cnt, ch in enc_counts:
                    rle += (str(cnt) + str(ch))
                
                return rle
        
        return get_rle(n)






        