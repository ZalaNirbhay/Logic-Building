def rev_sentence(s):
    
    words = s.split(" ")
    rev_words = []
    
    for word in words:
        rev_words.append(word[::-1])
        
    return " ".join(rev_words)

s="hello i am nirbhay zala"
print(rev_sentence(s))