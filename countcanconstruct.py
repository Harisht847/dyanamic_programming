def countcancounstract(target, wordbank):
    if target == '':
        return True 
    count = 0
    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            result = countcancounstract(suffix,wordbank)
            if result:
                count +=1
    return count 

print(countcancounstract("abcdef",["ab","abc","cd","def","abcd"]))
print(countcancounstract("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(countcancounstract("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
print(countcancounstract("purple",["purp","p","ur","le","purpl"]))
'''
print(countcancounstract("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee"]))
'''