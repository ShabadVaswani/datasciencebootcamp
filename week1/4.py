def countVowels(word):
    ls = list(word)
    aeiou = ['a', 'e', 'i', 'o', 'u']
    x = 0
    for i in ls:
        if i in aeiou:
            x+=1
    return(x)
print(countVowels('aeiou'))