#!/usr/bin/env python

# FOr_IJ_MaskMacro.py
# To create the macro that will be
# run in ImageJ
#
# The BeBo Company, 2018

import sys
import os
import time
import string
import re
import numpy as np

def isint(value):
  try:
    int(value)
    return True
  except:
    return False

def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

def find_el_infile ( s, sc ):
    array_vec = []
    f = open ( s , 'r' )
    for line in f:
        if ( re.search ( "PVM_Matrix=", line ) ):
           line = f.readline ( )
           nums = ( line.strip( ) ).split( )
           for num in nums:
               array_vec.append ( num )
        if ( re.search ( "PVM_SpatResol=", line ) ):   
           line = f.readline ( )
           nums = ( line.strip( ) ).split( )
           for num in nums:
               if ( isfloat ( num ) ):
                  numee = float ( num )
                  numee = sc * numee
               array_vec.append ( str ( numee ) )
        numee = 0
        nums = []
        if ( re.search ( "PVM_SliceThick=", line ) ):   
           nums = ( line.strip( ) ).split( '=' )
           if ( isfloat ( nums[1] ) ):
              numee = float ( nums[1] )
              numee = sc * numee
           array_vec.append ( str ( numee ) )
        if ( re.search ( "PVM_SPackArrNSlices=", line ) ):   
           line = f.readline ( )
           nums = ( line.strip( ) ).split( )
           for num in nums:
               array_vec.append ( num )
    f.close( )
    try:
       return array_vec
    except ValueError:
        return None


if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
                print ( "Usage: FOr_IJ_MaskMacro.py -basedir <base_dir> ");
                exit ( 1 );

if ( len ( sys.argv ) != 3 ) :
        print ( "Usage: FOr_IJ_MaskMacro.py -basedir <base_dir>" );
        exit ( 1 )

cur_dir = os.getcwd ( )

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
                base_dir = sys.argv.pop ( 0 )

#Structure = [315, 698, 1089, 583, 942, 131, 295, 319, 780, 477,\
#             803, 549, 1097, 339, 323, 348, 771, 354, 528, 519,\
#             1009, 73 ]

# For WM
Structure = [967, 949, 840, 848, 832, 911, 901, 798, 933, 917,\
             792, 960, 484682512, 983, 776, 956, 964, 1108, 971,\
             484682516, 986, 784, 896, 1000, 991, 768, 884, 908,\
             940, 1099, 301, 824]
filnam = []

for i in range ( len ( Structure ) ): 
    name = "structure_" + str ( Structure[i] ) + ".nrrd"
    filnam.append ( name )
    s_0 = base_dir + "/" + filnam[i]
    s_1 = 'open("' + s_0 + '");'
    print ( s_1 )
    s_2 = 'run("Multiply...", "value=' + str(i+1) + ' stack");'
    print ( s_2 )
    name = re.sub ( r'.nrrd', "_" + str(i+1)+ ".nii", s_0 )
    s_3 = 'run("NIfTI-1", "save=' + name + '");'
    print ( s_3 ) 
