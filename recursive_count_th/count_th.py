'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    countTh = 0
    if len(word)< 2:
        return countTh
    if word[0] == 't' and word[1] == 'h':
        countTh = 1 + count_th(word[2:])
    else:
        countTh = count_th(word[1:])
    return countTh

print(count_th("nothing"))
print(count_th("zero"))

# Understand:
# input is a string word
# check how many times the letters 'th' repeat in it
# must use recursion and no loops

# Plan:
# take input word
# create variable to hold total amount
# if the word is not even two letters then return the count
# check if the first and second letters of the word are t and h
# if so, add to the count and recurse the rest of the word except those 2 letters
# if not then return the count

# Execute
# code above

# Review
# Code runs checking one letter at a time unless it's a match and it skips over two
