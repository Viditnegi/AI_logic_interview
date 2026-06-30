
def compare(chars1, chars2):
    for i in range(26):
        if chars1[i] != chars2[i]:
            return False
    
    return True

def group_anagrams(strs):
    counts = {}
    group_by_len = {}
    for word in strs:          # Make word : count array dict
        chars = [0]*26
        for char in word:
            chars[char]+=1

        counts[word] = chars
        if len(word) not in group_by_len:
            group_by_len[len(word)] = set()
        
        group_by_len[len(word)].insert(word)     # make count : words array dict

    
    final_list = []
    for word in strs:
        group = [word]
        group_by_len[len(word)].remove(word)

        candidates = group_by_len[len(word)]               # a set to erase the already grouped words
        for candidate in candidates:
            if compare(candidate, counts[word]):      
                group.append(candidate)
                group_by_len[len(word)].remove(word)
                              
    
    return final_list





    

    


