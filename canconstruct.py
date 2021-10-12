def canconstruct(word, wordlist,memo={}):
    if word in memo:
        return memo[word]
    if word == '':
        return True
    for w in wordlist:
        if word.startswith(w):
            suffix = word[len(w):]
            memo[word] = canconstruct(suffix, wordlist)
            if memo[word]:
                return memo[word]  
    memo[word] = False     
    return False
'''
bruteforce :  o(n power m * m) time ---> o(n*m power 2) time
o(m power 2) space ----->   o(m power 2) space
'''

print(canconstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(canconstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(canconstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
print(canconstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee"]))
