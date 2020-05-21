'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    if word == '':
        return 0
    if 'th' in word[:2]:
        word = word[1:]
        return 1 + count_th(word)
    else:
        word = word[1:]
        return 0 + count_th(word)



print(count_th('thestth;lkajsd;lkjafth;lkajsdf;ljkasdfth'))

