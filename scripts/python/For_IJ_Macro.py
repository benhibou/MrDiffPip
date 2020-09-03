#!/usr/bin/env python

# For_IJ_Macro.py
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
                print ( "Usage: For_IJ_Macro.py -basedir <base_dir> -filename <name_from> -scaling <scaling>");
                exit ( 1 );

if ( len ( sys.argv ) != 7 ) :
        print ( "Usage: For_IJ_Macro.py -basedir <base_dir> -filename <name_from> -scaling <scaling>" );
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
    s_1 = 'run("Raw...", "open=/raid1/bboulat/FKBP_3/'
    s_2 = 'run("Properties...", "channels=1 slices='
    s_3 = 'run("NIfTI-1", "save=/raid1/bboulat/FKBP_3/'
    s_4 = 'run("Close");'
    m = m + 1
    if m > 1:
    #print( line.strip() )
       columns = ( line.strip() ).split()
       s_0 = s_0 + columns[0] + '/' + columns[5] + "/method"
       if ( isfloat ( scaling ) ): 
          scale = float ( scaling )
          a = find_el_infile ( s_0, scale )
       #print ( a )
       s_1 = s_1 + columns[0] + '/' + columns[5] + \
             "/pdata/1/2dseq image=[16-bit Signed] width=" + a[0] + \
             " height=" + a[1] + " number=" + a[5] + " little-endian"\
             + '");'
             
       print ( s_1 )
       s_2 = s_2 + a[5] + " frames=1 unit=pixel pixel_width=" + a[2] + \
             " pixel_height=" + a[3] + " voxel_depth=" + a[4] + '");'
       print ( s_2 )
       s_3 = s_3 + columns[0] + '/' + columns[5] + '/pdata/1/2dseq.nii");'
       print ( s_3 )
       print ( s_4 )

f.close ( )
