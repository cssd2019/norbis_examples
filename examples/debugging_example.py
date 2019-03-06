#!/usr/bin/env python3
""" 
 
 
 
 Kim Brugger (06 Mar 2019), contact: kim@brugger.dk
"""

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

def fibo_next(i:int, j:int) -> int:

    assert isinstance(i, int), "i is not an Int"
    assert isinstance(j, int), "i is not an Int"

    if ( i < j ):
        i, j = j, i
    
    
    return max(i, j) + min(i,j)


def fibo(loops:int):


    assert isinstance(loops, int), "i is not an Int"

    n = 0
    m = 1

    for i in range( 0, loops):
        print( "{}".format( n ))
        o = m
        m = fibo_next( n, m)
        n = m

    print( n )

def main():
    fibo( 10 )
   
if __name__ == '__main__':
    main()
