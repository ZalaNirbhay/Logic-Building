# Write a function that counts frequency of characters.

def count_word(s):
    words={}
    for ch in s:
        if ch in words:
            words[ch]+=1
        else:
            words[ch]=1
    return words 
   
s="banana"
print(count_word(s))