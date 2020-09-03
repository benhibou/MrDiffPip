#!/usr/bin/env python


# rotBvec.py
# A script to extract the rotaion part
# of an affine transformation.
# Then apply it to rotate the bvectors of
# a diffusion experiment. A flag is passed 
# to tell whether one shall use 

import sys
import os
import subprocess
import time
import string
import re
import numpy as np
import rotateVec


def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = 'Usage: rotBvec.py -basedir <base_dir> -filename <file_name> '
           s_2 = '-transpose <trp> -form <nifti_form> '
           s_3 = '-filevec <file_vec> -filout <file_out>'
           print ( s_1 + s_2 + s_3 );
           exit ( 1 );

if ( len ( sys.argv ) != 13 ) :
   s_1 = 'Usage: rotBvec.py -basedir <base_dir> -filename <file_name> '
   s_2 = '-transpose <trp> -form <nifti_form> '
   s_3 = '-filevec <file_vec> -filout <file_out>'
   print ( s_1 + s_2 + s_3 );
   exit ( 1 )

cur_dir = os.getcwd ( )

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
           base_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-filename" ):
           file_name = sys.argv.pop ( 0 )
           file_name = base_dir + "/" + file_name
        elif ( cmdarg == "-transpose" ):
           trp = sys.argv.pop ( 0 )
        elif ( cmdarg == "-form" ):
           nifti_form = sys.argv.pop ( 0 )
        elif ( cmdarg == "-filevec" ):
           file_vec = sys.argv.pop ( 0 )
        elif ( cmdarg == "-filout" ):
           file_out = sys.argv.pop ( 0 )

R = rotateVec.extrRotFromAff ( file_name, nifti_form )
print ( R )
if ( trp == 'y' ):
   B = R.T
else:
   B = R
n = rotateVec.effectRot ( file_vec, file_out, B )
print ( n )
