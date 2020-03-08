'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    def count(word, counter=0):

        if 'th' in word:
            word = word.replace('th','/',1)
            counter += count(word, counter) + 1
            
        return counter
   
    return count(word)


