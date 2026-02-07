class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        #solution courtesy : professor0akes yt

        if not words:
            return []

        for word in words:
            if word not in s:
                return []
        

        strlen = len(words[0])
        min_len = strlen * len(words)
        slen = len(s)
        if slen < min_len:
            return []
        
        # def get_item_nth_removed(n, lis):
        #     return [lis[i] for i in range(len(lis)) if i != n]
        
        i=0
        iter_last = (len(s)-min_len)

        combo_count = {}

        while(i <= iter_last):

            sub_str = s[i:i+strlen]
            sub_str_whole = s[i:i+min_len]
            #sieve to check if the word is not in list or not
            
            # for word in words:
            #     if word not in sub_str_whole:
            #         i+=1
                    
            if sub_str in words:
                j=0
                words_copy = words.copy()
                # print("sub_str", sub_str, "sub_str_whole", sub_str_whole, combo_count )
                #another sieve to get time optimization for one of the longas test case
                if sub_str_whole == ''.join(words_copy):
                    words_copy = []
                else:
                    while(j < min_len):
                        sub_word = s[i+j : i+j+strlen]
                        # print("checking subword", sub_word)
                        if sub_word in words_copy:
                            # print("before removing", sub_word, words_copy)
                            words_copy.remove(sub_word)
                            # print("after removing", sub_word, words_copy)
                        j+=strlen
                if not words_copy:
                    if sub_str_whole not in combo_count.keys():
                        combo_count[sub_str_whole] = [i]
                    else:
                        combo_count[sub_str_whole].append(i)
                    i+=1
                else:
                    i+=1
                
            else:
                i+=1
        res_combos = []
        for value in combo_count.values():
            res_combos +=value
        return res_combos