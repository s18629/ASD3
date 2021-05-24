def reverseWord(word):
    if len(word) == 0:
        return word
    else:
        return reverseWord(word[1:]) + word[0]


word = "algorithm"
print(reverseWord(word))