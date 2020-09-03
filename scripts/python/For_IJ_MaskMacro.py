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
                print ( "Usage: FOr_IJ_MaskMacro.py -basedir <base_dir> -filename <name_from>");
                exit ( 1 );

if ( len ( sys.argv ) != 5 ) :
        print ( "Usage: FOr_IJ_MaskMacro.py -basedir <base_dir> -filename <name_from>" );
        exit ( 1 )

cur_dir = os.getcwd ( )

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
                base_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-filename" ):
                name_from = sys.argv.pop ( 0 )
                name_from = base_dir + "/" + name_from
        elif ( cmdarg == "-scaling" ):
                scaling = sys.argv.pop ( 0 )
m = 0
a = []
f = open ( name_from, 'r' )


for line in f:
    s_0 = '/raid1/bboulat/FKBP_3/'
    s_2 = 'selectWindow("c12dseq_1stA0.nii");'
    s_3 = 'imageCalculator("Add create 32-bit stack", "c12dseq_1stA0.nii","c22dseq_1stA0.nii"); \
           \nselectWindow("Result of c12dseq_1stA0.nii");\nsetOption("BlackBackground", false); \
           \nrun("Make Binary", "method=Percentile background=Default calculate black"); \
           \nrun("32-bit");\nrun("Divide...", "value=255 stack"); \
           \nrun("NIfTI-1", "save='
    s_4 = 'run("Close");'
    s_5 = 'selectWindow("c12dseq_1stA0.nii");\nrun("Close");\nselectWindow("c22dseq_1stA0.nii"); \
           \nrun("Close");'
    m = m + 1
    if m > 1:
    #print( line.strip() )
       columns = ( line.strip() ).split()
       s_1 = 'open("' + s_0 + columns[0] + '/' + columns[4] + '/pdata/1/c12dseq_1stA0.nii");'
       print ( s_1 )

       s_1p = 'open("' + s_0 + columns[0] + '/' + columns[4] + '/pdata/1/c22dseq_1stA0.nii");'
       print ( s_1p )

       print ( s_2 )
       s_3 = s_3 + s_0 + columns[0] + '/' + columns[4] + '/pdata/1/BrainMask_' + str(m-1) + '.nii");'
       print ( s_3 )
       print ( s_4 )
       print ( s_5 )

f.close ( )
