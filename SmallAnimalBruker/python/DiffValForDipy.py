#!/usr/bin/env python

# DiffValForDipy.py
# to read the diffusion parameters   
# vectors and values in a file where
# they are arranged in four columns
# first three for the vectors, last
# one for the value, and output them
# into two files, one for the values
# arranged in one row and another
# file arranged in three rows, one
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
                print ( "Usage: DiffValForDipy.py -basedir <base_dir> -filename <name_from>");
                exit ( 1 );

if ( len ( sys.argv ) != 5 ) :
        print ( "Usage: DiffValForDipy.py -basedir <base_dir> -filename <name_from>" );
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
for line in f:
    #print( line.strip() )
    columns = ( line.strip() ).split()
    array_vec_1.append ( float ( columns[1] ) )
    array_vec_2.append ( float ( columns[2] ) )
    array_vec_3.append ( float ( columns[3] ) )
    array_val.append ( float ( columns[0] ) )

Fil_DiffVec = base_dir + "/" + "diff_bvec.txt"
Fil_DiffVal = base_dir + "/" + "diff_bval.txt"

#if os.path.exists ( Fil_Diff ):
i = 0
MMF = open (Fil_DiffVec, 'w' )
MMG = open (Fil_DiffVal, 'w' )
while i < len ( array_vec_1 ):
      s1 = str ( array_vec_1[i] ) + " "
      s_1 = s_1 + s1
      print (s_1)
      s2 = str ( array_vec_2[i] ) + " "
      s_2 = s_2 + s2
      s3 = str ( array_vec_3[i] ) + " "
      s_3 = s_3 + s3
      s4 = str ( array_val[i] ) + " "
      s_4 = s_4 + s4
      i = i + 1
MMF.write ( str ( s_1 ) )
MMF.write ( "\n" )
MMF.write ( str ( s_2 ) )
MMF.write ( "\n" )
MMF.write ( str ( s_3 ) )
MMG.write ( str ( s_4 ) )
MMF.close()
MMG.close()
