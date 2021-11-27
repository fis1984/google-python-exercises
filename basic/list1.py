#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    count = 0
    
    for word in words:
        if len(word) >= 2 and word[0] == word[len(word) - 1]:
            count += 1
    
    return count
            


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    x_list = [x for x in words if x[0] == "x" or x[0] == "X"]
    not_x_list = [x for x in words if x[0] != "x" and x[0] != "X"]
    not_x_list.sort()
    x_list.sort()
    x_list.extend(not_x_list)
    return x_list  
  
# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    quick_sort(tuples, 0, len(tuples) - 1)
    return tuples   

def quick_sort(tuples, left, right):
    
    if right <= left: return 
        
    piv = tuples[left][-1]
    i = left + 1
    j = right
    
    while i <= j:
        """Scan until reaching value equal or greater than piv
           or right marker 
        """        
        while i <= j and tuples[i][-1] < piv :  i = i + 1          
        """Scan until reaching value equal or smaller than piv
            or left marker
        """
        while i <= j and piv < tuples[j][-1] :  j = j - 1        
      
        if i <= j: 
            """to change tuples[i] and tuples [j]"""
            tuples[i], tuples[j] = tuples[j], tuples[i]
            i, j = i + 1, j - 1
            
    #put piv in his right placeholder
    tuples[left], tuples[j] = tuples[j], tuples[left]
    
    quick_sort(tuples, left, j - 1)
    quick_sort(tuples, j + 1, right) 
    
# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print ('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print ('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

        
    print()
    print ('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
        [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
        [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
        [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
