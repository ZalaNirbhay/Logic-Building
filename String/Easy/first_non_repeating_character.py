def count_word(s):
    words={}
    for ch in s:
        if ch in words:
            words[ch]+=1
        else:
            words[ch]=1
    return words 

def first_non_repeating(s):
    words=count_word(s)
    for ch in s:
        if words[ch]==1:
            return ch
    return None
    
s="nirbhay"
print(first_non_repeating(s))