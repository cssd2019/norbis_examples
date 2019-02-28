#!/usr/bin/env python3
""" 
 
 
 
 Kim Brugger (06 Feb 2019), contact: kim@brugger.dk
"""


s = "Thanks for noticing me - Eeyore".lower()
r = 10
while True:

    l = [" "] * len( s )
    for j in range(1, len( s ) - 1 ):
        if (s[j-1]==s[j+1]):
            l[j] = "*"
    print("".join( l ))
    s = "".join( l )

    r-=1
    if ( not r  ):
        break






    
