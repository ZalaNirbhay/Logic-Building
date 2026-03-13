def rev_string(s):
    rev_str=""
    for i in range(len(s)-1,-1,-1):
        rev_str+=s[i]
    return rev_str
        
s="nirbhay"
print(rev_string(s))