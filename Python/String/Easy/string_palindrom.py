# Write a function to check whether a string is palindrome.

# simplest and fastest way using slicing method

# def palindrome_string(s):
#     return s==s[::-1]

# two pointer approch 
def palindrome_string(s):
    start=0
    end=len(s)-1
    while(start<end):
        if s[start] != s[end]:
            return False
        
        start +=1
        end -=1
    return True

s="madam"
print(palindrome_string(s))