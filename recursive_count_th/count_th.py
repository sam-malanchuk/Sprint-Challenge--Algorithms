'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if it's less than 2 then it can't be 'th', return 0
    if len(word) < 2:
        return 0
    elif word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])

# Understand:
# takes in single string word
# checks how many times the string has the string 'th'
# cannot use any loops, must use recursion
