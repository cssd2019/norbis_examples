#!/usr/bin/env python3
""" 
 
 
 
 Kim Brugger (06 Feb 2019), contact: kim@brugger.dk
"""

import sys



def add_one(data):

    if ( not isinstance(data, list)):
        raise TypeError

    new_list = []

    for d in data:
        new_list.append( d + 1 )

    return new_list

def test_one_single():
    assert add_one([1]) == [2]

def test_one_multi():
    assert add_one([1,2]) == [2,3]

def test_one_str():
   with pytest.raises( TypeError):
     add_one(1,2)

def test_one_empty():
    assert add_one([]) == []
