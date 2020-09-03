#!/usr/bin/env python

# Cohort_T2_Registration.py
# Macro that will be run the registration of a 
# structural image to the Allen Brain template
# at some chosen resolution, using the ANTS 
# registration package, in # particular the 
# routine antsRegistrationSyNQuick
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

print (len ( sys.argv ))
if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = "Usage: Cohort_T2_Registration.py -basedir <base_dir> -filename <name_from>"
           s_2 = " -data_dir <data_dir>  -exp_number <exn> -filstr <fil_str>" 
           print ( s_1 + s_2 );
           exit ( 1 );

if ( len ( sys.argv ) != 11 ) :
   s_1 = "Usage: Cohort_T2_Registration.py -basedir <base_dir> -filename <name_from>"
   s_2 = " -data_dir <data_dir>  -exp_number <exn> -filstr <fil_str>" 
   print ( s_1 + s_2 );
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
        elif ( cmdarg == "-filstr" ):
           fil_str = sys.argv.pop ( 0 )
m = -1
a = []
curdir = os.getcwd ( )
f = open ( name_from, 'r' )


for line in f:
    s_0 = data_dir
    s_1 = data_dir + '/'
    m = m + 1
    if m > 0:
    #print( line.strip() )
       columns = ( line.strip() ).split()
       s_1 = s_1 + columns[0] + '/' + columns[exn] + \
             '/pdata/1/processed/fsl_proc/bedpost/'
       print ( s_1 )
       if not ( os.path.isdir (  s_1 ) ):
          os.mkdir ( s_1 )
          s1_cmd = 'cp ' + re.sub ( r'bedpost/', "data.nii.gz ", s_1 ) + s_1
          p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
          s1_cmd = 'cp ' + re.sub ( r'fsl_proc/bedpost/', "BrainMask.nii ", s_1 ) + s_1 + 'nodif_brain_mask.nii'
          p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
          s1_cmd = 'cp ' + re.sub ( r'pdata/1/processed/fsl_proc/bedpost/', 'diff_bvec.txt ', s_1 ) + s_1 + 'bvecs'
          p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
          s1_cmd = 'cp ' + re.sub ( r'pdata/1/processed/fsl_proc/bedpost/', 'diff_bval.txt ', s_1 ) + s_1 + 'bvals'
          p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       s_1p = s_1 + '../' + fil_str
       print (s_1p)
       if not ( os.path.isdir (  s_1p ) ):
          s1_cmd = 'bedpostx ' + s_1 + ' --nf=3 --fudge=1  --bi=1000'
          print ( s1_cmd )
          p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       #print ( stdout )

f.close ( )

# file to include into bedpostx input directory: 4D data series (data.nii.gz, nodif_brain_mask, bvecs and bvals. 
# bedpostx /raid1/bboulat/FKBP_DICOMS/20180416_135109_579_1_1/7/pdata/1/processed/fsl_proc/bedpost --nf=3 --fudge=1  --bi=1000
# /usr/local/fsl/bin/bedpostx /raid1/bboulat/FKBP_DICOMS/20180416_135109_579_1_1/7/pdata/1/processed/fsl_proc/bedpost --nf=3 --fudge=1  --bi=1000
