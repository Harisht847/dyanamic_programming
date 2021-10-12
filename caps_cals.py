import string
from collections import OrderedDict

def sum_of_value(words):
    alphabet_string = list(string.ascii_uppercase)
    numbers = [i for i in range(1,26)]
    values = {key:value for key,value in zip(alphabet_string,numbers)}
    counter = []
    for word in words:
        count = 0
        for w in word:
            count = count+ values[w]
        counter.append(count)
    sum_of_words = {key:value for key,value in zip(words,counter)}
    print(sum_of_words)
    return OrderedDict(sorted(sum_of_words.items(),reverse=True))

words = ["GMAIL","YAHOO", "OUTLOOK","HUBSPOT","AOL","YANDEX","GMX"]
dict = sum_of_value(words)


def dictionairy(x):
    return {k: v for k, v in sorted(x.items(), reverse=True,key=lambda item: item[1])}.keys()


print(dictionairy(dict))
