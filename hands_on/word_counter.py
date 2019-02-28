#!/usr/bin/env python3
""" 
 
 
 
 Kim Brugger (06 Feb 2019), contact: kim@brugger.dk
"""

import sys
import os
import string



def remove_punctuation( text ):
    """ removes punctuation from a string """
    return text.translate(str.maketrans({key: None for key in string.punctuation}))


def count_word_occurence_in_string(text ):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """

    text = text.lower()

    text = remove_punctuation( text )
    
    words = set( text.split() )
    words = sorted( words )

    res   = []
    
    for word in words:
        res.append( [ word, text.count( word )])

    return res


def count_word_occurence_in_file(file_name):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """

    counts = {}
    with open(file_name, 'r') as f:
        for line in f:
            word_counts = count_word_occurence_in_string( line)
            for word, count in word_counts:
                if word not in counts:
                    counts[ word ] = 0
                    
                counts[ word ] += count
                
    print( counts )
    return counts



if __name__ == '__main__':
    if len( sys.argv) != 2:
        print( "Function takes a single filename as input")
        sys.exit()

    filename = sys.argv[ 1 ]
    if not os.path.isfile( filename ):
        print("'{}' does not exist or is not a file".format( filename ))
        sys.exit()
        
        
    for word, count in count_word_occurence_in_file( filename ).items():
        print("{} --> {}".format( word, count))
