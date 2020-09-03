#!/usr/bin/env python


# extractRotFromAff.py
# A script to extract the rotaion part
# of an affine transformation.
# The rotation will be given as "R.T",
# right the transpose of "R". Thus the 
# inverse transform will be in effect "R".
#
# The BeBo Company, 2018


import sys
import os
import subprocess
import time
import string
import re
import numpy as np


if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = 'Usage: extractRotFromAff.py -basedir <base_dir> -filename <file_name>'
           print ( s_1 );
           exit ( 1 );

if ( len ( sys.argv ) != 5 ) :
   s_1 = 'Usage: extractRotFromAff.py -basedir <base_dir> -filename <file_name>'
   print ( s_1 );
   exit ( 1 )

cur_dir = os.getcwd ( )

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
           base_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-filename" ):
           file_name = sys.argv.pop ( 0 )
           file_name = base_dir + "/" + file_name


#print( line.strip() )
if os.path.isfile (  file_name ):
   s_1 = 'fslhd ' + file_name
   print ( s_1 )
   p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
   stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
   print ( stdout )
   i = 0
   while i < len ( stdout ):
         print ( i, stdout[i] )
         i += 1
   a = ( stdout[47].strip ( ) ).split ( )
   b = ( stdout[48].strip ( ) ).split ( )
   c = ( stdout[49].strip ( ) ).split ( )
   s_x = np.sqrt ( np.square ( float ( a[1] ) )\
                   + np.square (  float ( b[1]  ) ) \
                   + np.square ( float ( c[1] ) ) )   

   s_y = np.sqrt ( np.square ( float ( a[2] ) )\
                   + np.square (  float ( b[2]  ) ) \
                   + np.square ( float ( c[2] ) ) )   

   s_z = np.sqrt ( np.square ( float ( a[3] ) )\
                   + np.square (  float ( b[3]  ) ) \
                   + np.square ( float ( c[3] ) ) )   

   x = np.array ( [ float ( a[1] ), float ( b[1] ), float ( c[1] ) ] ) / s_x
   y = np.array ( [ float ( a[2] ), float ( b[2] ), float ( c[2] ) ] ) / s_y
   z = np.array ( [ float ( a[3] ), float ( b[3] ), float ( c[3] ) ] ) / s_z
   R = np.array ( [ x, y, z ] )

   # The actual rotation matrix will be "R.T".

   print ( np.dot ( R.T, R ) )
