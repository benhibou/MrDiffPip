#!/usr/bin/env python

# The BeBo Comp, 2018
# applrot.py
# A script to build the rotation matrix
# associated to a unit quaternion.
# The input should consist of the three
# last components of the quaternion
# b, c, d
# Subsequentely the rotation is applied
# to rotate the b_table associated to
# a diffusion experiment.
#
# The BeBo Company, 2018


import sys
import os
import subprocess
import time
import string
import re
import numpy as np
import math


def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = 'Usage: applrot.py -b <b> -c <c> -d <d> -flinam <filename> '
           s_2 = '-filout <filout>'
           exit ( 1 );

if ( len ( sys.argv ) != 11 ) :
   s_1 = 'Usage: applrot.py -b <b> -c <c> -d <d> -flinam <filename> '
   s_2 = '-filout <filout>'
   print ( s_1 + s_2 )
   exit ( 1 )

cur_dir = os.getcwd ( )

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-b' ):
           b = float ( sys.argv.pop ( 0 ) )
        if ( cmdarg == '-c' ):
           c = float ( sys.argv.pop ( 0 ) )
        if ( cmdarg == '-d' ):
           d = float ( sys.argv.pop ( 0 ) )
        if ( cmdarg == '-filnam' ):
           file_name = sys.argv.pop ( 0 )
        if ( cmdarg == '-filout' ):
           file_out = sys.argv.pop ( 0 )

a = math.sqrt ( 1 - b * b - c * c - d * d )
print ( a )

r_11 = a * a + b * b - c * c - d * d
r_12 = 2 * ( b * c - a * d )
r_13 = 2 * ( b * d + a * c )
r_21 = 2 * ( b * c + a * d )
r_22 = a * a - b * b + c * c - d * d
r_23 = 2 * ( c * d - a * b )
r_31 = 2 * ( b * d - a * c )
r_32 = 2 * ( c * d + a * b )
r_33 = a * a - b * b - c * c + d * d


print ( "%.6f\t%.6f\t%.6f" % ( r_11, r_12, r_13 ) )
print ( "%.6f\t%.6f\t%.6f" % ( r_21, r_22, r_23 ) )
print ( "%.6f\t%.6f\t%.6f" % ( r_31, r_32, r_33 ) )

R = np.matrix ( [[r_11, r_12, r_13], [r_21, r_22, r_23], [r_31, r_32, r_33]] )
I = np.dot ( R, np.transpose ( R ) )
print ( I ) 

m = 0
f = open ( file_name, 'r' )
g = open ( file_out, 'w' )


for line in f:
    array_vec = [] 
    nums = ( line.strip() ).split()
    for num in nums:
        if isfloat ( num ):
           array_vec.append ( float ( num ) )
    a = array_vec[0]
    print ( a )
    b = np.array ( array_vec[1:4] )
    #b = np.transpose ( b )
    x = np.array ( [[1], [1], [1]] )
    x = np.matrix ( b )
    y = np.transpose ( np.dot ( np.transpose ( R ),  np.transpose ( x ) ) )
    #print (array_vec )
    #print (b )
    print ( x )
    #print (np.transpose ( np.dot (R, np.transpose(x) ) ) )
    print ( y )
    print ( y.item(0,2) )
    g.write ( " %.6f %.6f %.6f %.6f\n" % ( a, y.item ( 0 ), y.item ( 1 ), y.item ( 2 ) ) )  
f.close ( )
g.close ( )
