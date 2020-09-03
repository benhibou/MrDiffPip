#!/usr/bin/env python

# Read_Diff_Val.py
# to read the diffudion parameters   
# vectors and values from the Bruker
# method file

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
                print ( "Usage: Read_Diff_Val.py -basedir <base_dir> -filename <name_from> \
        -nb0 <nb0>");
                exit ( 1 );

if ( len ( sys.argv ) != 7 ) :
        print ( "Usage: Read_Diff_Val.py -basedir <base_dir> -filename <name_from> \
-nb0 <nb0>" );
        exit ( 1 )

cur_dir = os.getcwd ( )

a = 0
array_vec = []
array_val = []

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
                base_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-filename" ):
                name_from = sys.argv.pop ( 0 )
                name_from = base_dir + "/" + name_from
        elif ( cmdarg == "-nb0" ):
                nb0 = int ( sys.argv.pop ( 0 ) )
m = 0
f = open ( name_from, 'r' )
for line in f:
    #print( line )
    if ( re.search ( "PVM_DwDir=\(", line ) ):
       a = 2
       vals = [ int ( s )  for s in re.findall ( r'\b\d+\b', line )]
       print ( vals[0]*vals[1], "\n")
       if a == 2:
          i = 0
          while i < ( vals[0] * vals[1] ): 
             line = f.readline ( )
             nums = ( line.strip() ).split()
             j = len ( nums )
             i = i + j
             #print ( i )
             for num in nums:
                 if isfloat ( num ):
                    array_vec.append ( float ( num ) )
    if ( re.search ( "_DwEffBval=\(", line ) ):
       a = 3
       val = [int ( s )  for s in re.findall ( r'\b\d+\b', line )]
       print ( val[0], "\n" )
       if a == 3:
          i = 0
          while i < val[0]: 
             line = f.readline ( )
             nums = ( line.strip() ).split()
             j = len ( nums )
             i = i + j
             #print ( i )
             for num in nums:
                 if isfloat ( num ):
                    array_val.append ( float ( num ) )
       print ( "hello", array_val, "\t", len(array_val) )
     


Fil_Diff = base_dir + "/" + "diff_param.txt"
Fil_Diff_bck = base_dir + "/" + "diff_param.txt_bck" 
cmd_1 = "cp " + Fil_Diff + " " + Fil_Diff_bck
cmd_2 = "cp " + Fil_Diff_bck + " " + Fil_Diff
#
#if not os.path.exists ( Fil_Diff_bck ):
#   os.system ( cmd_1 ) 
#else:
#   os.system ( cmd_2 )

i = 0
j = 0
#if os.path.exists ( Fil_Diff ):
MMF = open (Fil_Diff, 'w' )
for x in range (0, 7):
    s = "0\t0\t0\t0\n"
    MMF.write ( s )
while i < len ( array_vec ):
      s = str ( array_val[j+nb0] ) + "\t" + \
          str ( array_vec[i] ) + "\t" + str ( array_vec[i+1] ) + "\t" + \
          str ( array_vec[i+2] ) + "\n"
      i = i + 3
      j = j + 1
      MMF.write ( s )
#ModMethFil = "/home/nmrsu/someprog/rare_adj/scripts/mytry2"
#MMF = open (ModMethFil, 'w' )
#MMF.writelines ( contents )
#MMF.close ( )
