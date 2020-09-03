#!/usr/bin/env python

# W_AntSynAndApply.py
# To run FSL flirt between
# registering T2s (T1s) to
# the B0 image of a diffusion exp.
#
# The BeBo Company, 2019

import sys
import subprocess
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

#print (len ( sys.argv ))
if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = "Usage: W_AntSynAndApply.py -basedir <base_dir> -filename <name_from>"
           s_2 = " -data_dir <data_dir>  -exp_number1 <exn1> -dir_parcel <dir_parcel>" 
           s_3 = " -fil_parcel <fil_parcel>"
           print ( s_1 + s_2 + s_3);
           exit ( 1 );

if ( len ( sys.argv ) != 13 ) :
   s_1 = "Usage: W_AntSynAndApply.py -basedir <base_dir> -filename <name_from>"
   s_2 = " -data_dir <data_dir>  -exp_numberD <exnD> -dir_parcel <dir_parcel>" 
   s_3 = " -fil_parcel <fil_parcel>"
   print ( s_1 + s_2 + s_3);
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
        elif ( cmdarg == "-exp_numberD" ):
           exp_numberD = sys.argv.pop ( 0 )
           if ( isint ( exp_numberD) ):
              exnD = int ( exp_numberD )
        elif ( cmdarg == "-dir_parcel" ):
           dir_parcel = sys.argv.pop ( 0 )
        elif ( cmdarg == "-fil_parcel" ):
           fil_parcel = sys.argv.pop ( 0 )
m = -1
a = []
curdir = os.getcwd ( )
f = open ( name_from, 'r' )


for line in f:
    s_0 = data_dir
    s_1 = data_dir + '/'
    s_2 = '/home/spectro/diffusion/ANTsX-ANTs-4367a81/Scripts/antsRegistrationSyNQuick.sh -d 3 -f '
    m = m + 1
    if m > 0:
    #print( line.strip() )
       columns = ( line.strip() ).split()
       s_1D = s_1 + columns[0] + '/' + columns[exnD] + \
              '/pdata/1/processed/fsl_proc/bedpost.bedpostX/'
       s_1F = s_1 + columns[0] + '/' + columns[exnD] + \
             '/pdata/1/processed/zuzut_masked_1.nii'
       s_1T = dir_parcel + "/" + fil_parcel
       print ( s_1F, "\t", s_1T )
       if ( os.path.isfile (  s_1T ) ):
          if ( os.path.isdir (  s_1D ) ):
             if ( os.path.isfile (  s_1F ) ):
                os.chdir ( s_1D )
                s_T_out = re.sub ( dir_parcel, s_1D, s_1T )
                s_T_out = re.sub ( r'.nii', "", s_T_out ) 
                s1_cmd = s_2 + s_1F + ' -m ' + s_1T + ' -o ' + s_T_out + '_tryreg'
                print ( s1_cmd )
                p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
                stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
                s_2 = 'antsApplyTransforms -d 3 -i '
                s_1T = re.sub ( r'_Masked', "_labels", s_1T )
                s_T2_out = re.sub ( dir_parcel, s_1D, s_1T )
                s1_cmd = s_2 + s_1T + ' -o ' + s_T2_out +  ' -t ' + s_T_out + '_tryreg0GenericAffine.mat -r ' + s_1F
                print ( s1_cmd )
                p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
                stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )

f.close ( )
os.chdir ( curdir )
