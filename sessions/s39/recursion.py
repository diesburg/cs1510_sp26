'''
File: recursion.py
Author: CS 1510
Description: Recursive functions.  The second summation function performs
the same as the first, but it also has informative print statements.  The last
recursive function finds the Fibonacci sequence, but it is really a bad example
of recursion because the work it performs grows exponentially.
'''

def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)



##def sum(n):
##    print("asked to find sum("+str(n)+")")
##    if n==1:
##        print("base case")
##        return 1
##    else:
##        print("going to find",n,"+ sum("+str(n-1)+")")
##        result= n+sum(n-1)
##        print("got",result,"from",n,"+ sum("+str(n-1)+")")
##        return result


def fib(n):
    if n==2 or n==1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
