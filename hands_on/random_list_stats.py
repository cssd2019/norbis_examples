#!/usr/bin/env python3
""" 
 
 Generates a list of random  values and print some stats related to the data generated
 
 C. Monkey ( c.monkey@bananalab.no)
"""

import sys
import random

# Global variable for the list length
list_length = 10


def random_number_list(data=[]):
    """ Add random number between 0 and 9 (both inclusive) to a list """

    for i in range( 0, list_length ):
        # append a random int to the data list
        data.append( random.randint(0, 10))

    return data


def sort_list(data, reverse=False):
    # Find max and min values
    max_val  = max( data )
    min_val  = min( data )
    # return sorted list
    return( sorted( data, reverse=reverse))
    


def set_list_length( length=int):
    """ Change the length of the list to generate """
    list_length = length
    print( "INFO: Changed list length to: {}".format( list_length ))



def list_len( data=[]):
    """ find the list length """
    i = 0
    for d in data:
        i += 1

    return i
    
    
def list_sum( data=[]):
    """ find the sum of all the values in the list """
    summed = 0
    for d in  data:
        # add value, throw to int to avoid issues
        summed += int(d)

    return summed
    

def median( data=[]):
    """ returns the median value of the list """
    middle = int(list_len(data)/2)

    
    return data[ middle ]

def mean( data=[]):
    """ returns the mean value of the list """
    return list_sum( data )/ list_len( data )


def mode(data=[]):
    """ returns the modal value in a list  """

    # gets the values represented once
    value_set = set( data )

    # Initial values
    c = -1
    v = []
    for d in value_set:
        # Current count is higher that prev observed
        if ( c < data.count( d )):
            c = data.count( d )
            v = [d]

        elif ( c == data.count( d )):
            v.append(  d )

    return v,c
    
    


def main() :
    
    # Change the list length to 20.
    set_list_length( 20 )

    # create a random list, and sort it
    sorted_list =  sort_list( random_number_list(  )) 

    # Print the results
    print( "List length: {}".format( len( sorted_list)))
    print( "Lowest: {}, highest: {}".format( sorted_list[0], sorted_list[ -1 ]))
    print( "Mean: {}".format( mean( sorted_list )))
    print( "Median: {}".format( median( sorted_list )))
    print( "Mode: {0[0]} (count: {0[1]})".format( mode( sorted_list )))
    exit()


max = random_number_list
if __name__ == '__main__':
    main()
    


