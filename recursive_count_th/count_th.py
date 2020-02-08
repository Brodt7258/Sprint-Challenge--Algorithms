'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  
  # base case. the string is too small to contain 'th', therefore there is nothing left to check
  if len(word) < 2:
    return 0

  # found an occurence, add 1 to the result, move up 2 characters and check again
  elif word[0:2] == 'th':
    return 1 + count_th(word[2:])

  # did not find an occurence, move up 1 character and check again
  else:
    return count_th(word[1:])
