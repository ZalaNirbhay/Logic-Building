name="butterfly"
sub_name="fly"
def find_substring(s, sub):
    i,j=0,len(sub)
    while j<=len(s):
        if (s[i:j] == sub):
            return True
        i+=1
        j+=1
    return False
    

print(find_substring(name,sub_name))
    