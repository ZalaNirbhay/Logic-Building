def count_word(s):
    words={}
    for ch in s:
        if ch in words:
            words[ch]+=1
        else:
            words[ch]=1
    return words 

def are_anagrams(s1, s2):

    if len(s1) != len(s2):
        return False

    return count_word(s1) == count_word(s2)

s1="listen"
s2="silent"

print(are_anagrams(s1,s2))