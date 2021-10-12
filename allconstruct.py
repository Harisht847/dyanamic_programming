def allconstruct(target, wordbank, data=[]):
    if target == '':
        return [[]]
    combination = []
    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            result = allconstruct(suffix,wordbank)
            targetways = list(map(lambda x:([word]+x), result))
            combination = combination + targetways
    return combination
print(allconstruct("abcdef",["ab","abc","cd","def","abcd","ef","c"]))            