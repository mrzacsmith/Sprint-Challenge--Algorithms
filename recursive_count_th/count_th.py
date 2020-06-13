'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    if len(word) < 2:
        return 0

    elif word[:2] == 'th':
        print(word)
        return 1 + count_th(word[1:])
    else:
        print(word)
        return 0 + count_th(word[1:])


print(count_th('theather'))
print(count_th('never'))
