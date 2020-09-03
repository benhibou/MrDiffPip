#!/usr/bin/env python

# W_fslbet.py
# a wrapper to FSL brain extraction
# peocedure (BET).
# Allows to run "BET" accross
# the many subjects of a group study.
# the "basedir" is the directory where
# the file containing the specification
# of the data for the animals are stored.
# Comes under "filename". 
# "basedir_f" is the directory of the study
# under which the nifti file for all the 
# subjects are stored. 
# The script will create a "processed" directory
# in each and every subject subdirectory, where
# brain mask will be stored.

import sys
import os
import subprocess
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

if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = 'Usage: W_fslchpixdim.py -basedir <base_dir> -filename <file_name>'
           s_2 = ' -basedir_f <base_dir_from> -filstr <file_string>'
           print ( s_1 + s_2 );
           exit ( 1 );

if ( len ( sys.argv ) != 9 ) :
   s_1 = 'Usage: W_fslchpixdim.py -basedir <base_dir> -filename <file_name>'
   s_2 = ' -basedir_f <base_dir_from> -filstr <file_string>' 
   print ( s_1 + s_2 );
   exit ( 1 )

cur_dir = os.getcwd ( )

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
           base_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-filename" ):
           file_name = sys.argv.pop ( 0 )
           file_name = base_dir + "/" + file_name
        elif ( cmdarg == '-basedir_f' ):
           base_dir_f = sys.argv.pop ( 0 ) + '/'
        elif ( cmdarg == '-filstr' ):
           file_string = sys.argv.pop ( 0 )
m = 0
f = open ( file_name, 'r' )


for line in f:
    if m > 0:
       s_1 = base_dir_f
       #print( line.strip() )
       columns = ( line.strip() ).split()
       s_2 = s_1 + columns[0] + '/' + file_string + \
             '/' + columns[1] + re.sub ( r'_BIDS', "", columns[0] ) + columns[2]
       s_1 = s_1 + columns[0] + '/' + file_string + '/processed'
       print ( s_1, "\n", s_2 )
       if not ( ( os.path.isdir (  s_1 ) ) ):
          os.mkdir ( s_1 )
       if ( os.path.isdir (  s_1 ) ):
          mon_deux = s_2
          mon_zuzut = s_1 + '/zuzut.nii.gz'
          if ( os.path.isfile ( mon_deux ) ):
             s_1 = 'cp ' + s_2 + ' ' + mon_zuzut
             p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
             stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
          s_1 = '/usr/local/fsl/bin/bet ' + mon_zuzut + ' ' + mon_zuzut + '_brain -F -f 0.5 -g 0 -m'
          print ( s_1 )
          p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
    m = m + 1

#/usr/local/fsl/bin/bet /Volumes/MEIN_LEBEN/HDTI/FOE0003_BIDS/dwi/sub-FOE0003_run-1_dwi /Volumes/MEIN_LEBEN/HDTI/FOE0003_BIDS/dwi/sub-FOE0003_run-1_dwi_brain -F -f 0.5 -g 0 -m
