#!/usr/bin/env python

# to read the diffusion parameters   
# vectors and values in a file where
# they are arranged in four columns
# first three for the vectors, last
# one for the value, and output them
# into two files, one for the values
# arranged in one column and another
# file arranged in three columns, one
# for each component of the diffusion
# gradient vector.

"""
"""
import sys
import os
import time
import string
import re
import numpy as np
from scipy.stats import ttest_ind
from scipy.special import stdtr
import matplotlib.pyplot as plt
from pylab import *
import pylab as P
import string

def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

#from datascience import stats
# if element is found it returns index of element else returns -1

def find_element_in_list(element, list_element):
    try:
        index_element = list_element.index(element)
        return index_element
    except ValueError:
        return None

if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
                print ( "Usage: DiffValInCol.py -basedir <base_dir> -filename <name_from>");
                exit ( 1 );

if ( len ( sys.argv ) != 5 ) :
        print ( "Usage: DiffValInCol.py -basedir <base_dir> -filename <name_from>" );
        exit ( 1 )

cur_dir = os.getcwd ( )

a = 0
array_vec_1 = []
array_vec_2 = []
array_vec_3 = []
array_val = []
s_1 = ''
s_2 = ''
s_3 = ''
s_4 = ''

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
                base_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-filename" ):
                name_from = sys.argv.pop ( 0 )
                name_from = base_dir + "/" + name_from
m = 0
f = open ( name_from, 'r' )

Fil_DiffVec = base_dir + "/" + "diff_bvecInC.txt"
Fil_DiffVal = base_dir + "/" + "diff_bvalInC.txt"

#if os.path.exists ( Fil_Diff ):
i = 0
MMF = open (Fil_DiffVec, 'w' )
MMG = open (Fil_DiffVal, 'w' )

for line in f:
    #print( line.strip() )
    columns = ( line.strip() ).split()
    s_1 = columns[0] + " " + columns[1] + " " + columns[2] + "\n"
    MMF.write ( str ( s_1 ) )
    s_4 = columns[3] + "\n"
    MMG.write ( str ( s_4 ) )
    #print ( columns[3] )
    print ( str(s_4) )

MMF.close()
#MMG.close()
