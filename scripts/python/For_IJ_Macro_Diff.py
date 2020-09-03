#!/usr/bin/env python

# For_IJ_Macro_Diff.py
# To create the macro that will be
# run in ImageJ, transforming Bruker
# 2dseq file in nifti format, for the
# case of a diffusion experiment.
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

def find_el_infile ( s, t ):
    array_vec = []
    f = open ( s , 'r' )
    for line in f:
        if ( re.search ( "PVM_DwNDiffDir=", line ) ):   
           nums = ( line.strip( ) ).split( '=' )
           if ( isint ( nums[1] ) ):
              ndiffdir = int ( nums[1] )
        if ( re.search ( "PVM_DwAoImages=", line ) ):   
           nums = ( line.strip( ) ).split( '=' )
           if ( isint ( nums[1] ) ):
              nA0 = int ( nums[1] )
              nexp = ndiffdir + nA0
              #nexp = 1
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
                  if ( isfloat ( t ) ):
                     numee = float ( t ) * numee
               array_vec.append ( str ( numee ) )
        numee = 0
        nums = []
        if ( re.search ( "PVM_SliceThick=", line ) ):   
           nums = ( line.strip( ) ).split( '=' )
           if ( isfloat ( nums[1] ) ):
              numee = float ( nums[1] )
              if ( isfloat ( t ) ):
                 numee = float ( t ) * numee
           array_vec.append ( str ( numee ) )
        if ( re.search ( "PVM_SPackArrNSlices=", line ) ):   
           line = f.readline ( )
           nums = ( line.strip( ) ).split( )
           for num in nums:
              if ( isint ( num ) ):
                 numi = int ( num ) * nexp
                 array_vec.append ( str ( numi ) )
    array_vec.append (  num )
    array_vec.append ( str ( nexp ) )
    f.close( )
    try:
       return array_vec
    except ValueError:
        return None


if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = 'Usage: For_IJ_Macro_Diff.py -basedir <base_dir> -filename <name_from>'
           s_2 = ' -data_dir <data_dir> -exp_number <exn> -factor <factor>'
           print ( s_1 + s_2 )
           exit ( 1 );

if ( len ( sys.argv ) != 11 ) :
   s_1 = 'Usage: For_IJ_Macro_Diff.py -basedir <base_dir> -filename <name_from>'
   s_2 = ' -data_dir <data_dir> -exp_number <exn> -factor <factor>'
   print ( s_1 + s_2 )
   exit ( 1 )

cur_dir = os.getcwd ( )

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
           base_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-filename" ):
           name_from = sys.argv.pop ( 0 )
           name_from = base_dir + "/" + name_from
        elif ( cmdarg == "-data_dir" ):
           data_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-exp_number" ):
           exp_number = sys.argv.pop ( 0 )
           if ( isint ( exp_number ) ):
              exn = int ( exp_number )
        elif ( cmdarg == "-factor" ):
           factor = sys.argv.pop ( 0 )
m = 0
a = []
f = open ( name_from, 'r' )


for line in f:
    s_0 = data_dir + '/'
    s_1 = 'run("Raw...", "open=' + s_0
    s_1_p = 'run("Make Substack...", "  slices=1-35");'
    s_1_pp = 'selectWindow("Substack (1-35)");'
    s_1_3p = 'run("NIfTI-1", "save=' + s_0
    s_1_4p = 'selectWindow("2dseq");'
    s_2 = 'run("Properties...", "channels=1 slices='
    s_3 = 'run("Stack to Hyperstack...", "order=xyczt(default)'
    s_4 = 'run("NIfTI-1", "save=' + s_0
    s_5 = 'run("Close");'
    m = m + 1
    if m > 1:
    #print( line.strip() )
       columns = ( line.strip() ).split()
       s_0 = s_0 + columns[0] + '/' + columns[exn] + "/method"
       a = find_el_infile ( s_0, factor )
       #print ( a )
       s_1 = s_1 + columns[0] + '/' + columns[exn] + \
             "/pdata/1/2dseq image=[16-bit Signed] width=" + a[0] + \
             " height=" + a[1] + " number=" + a[5] + " little-endian"\
             + '");'
             
       print ( s_1 )
       s_2 = s_2 + a[5] + " frames=1 unit=pixel pixel_width=" + a[2] + \
             " pixel_height=" + a[3] + " voxel_depth=" + a[4] + '");'
       print ( s_2 )
       print ( s_1_p )
       print ( s_1_pp )
       s_1_3p = s_1_3p + columns[0] + '/' + columns[exn] + '/pdata/1/2dseq_1stA0.nii");' 
       print ( s_1_3p )
       print ( s_5 )
       print ( s_1_4p )
       s_3 = s_3 + ' channels=1 slices=' + a[6] + ' frames=' \
             + a[7] + ' display=Color");'
       print ( s_3 )
       s_4 = s_4 + columns[0] + '/' + columns[exn] + '/pdata/1/2dseq.nii");'
       print ( s_4 )
       print ( s_1_4p )
       print ( s_5 )

f.close ( )
