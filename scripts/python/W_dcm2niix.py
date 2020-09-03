#!/usr/bin/env python

# W_dcm2niix.py
# a wrapper to the script dcm2niix
# Allows to run "dcm2niix accross
# the many animals of a group study.
# the "basedir" is the directory where
# the file containing the specification
# of the data for the animals are stored.
# Comes under "filename". 
# "basedir_f" is the directory of the study
# under which the DICOM data for all the animals
# are stored. 

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
           s_1 = 'Usage: W_dcm2niix.py -basedir <base_dir> -filename <file_name>'
           s_2 = ' -basedir_f <base_dir_from> -filstr <file_string> -exp# <exn>'
           print ( s_1 + s_2 );
           exit ( 1 );

if ( len ( sys.argv ) != 11 ) :
   s_1 = 'Usage: W_dcm2niix.py -basedir <base_dir> -filename <file_name>'
   s_2 = ' -basedir_f <base_dir_from> -filstr <file_string> -exp# <exn>' 
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
        elif ( cmdarg == '-exp#' ):
           exp_number = sys.argv.pop ( 0 )
           if ( isint ( exp_number ) ):
              exn = int ( exp_number )
m = 0
f = open ( file_name, 'r' )


for line in f:
    if m > 0:
       s_1 = base_dir_f
       #print( line.strip() )
       columns = ( line.strip() ).split()
       s_2 = s_1 + columns[0] + '/' + columns[exn] + '/' + file_string + '/nii'
       s_3 = s_1 + columns[0] + '/' + columns[exn] + '/' + file_string + '/processed'
       s_1 = s_1 + columns[0] + '/' + columns[exn] + '/' + file_string + '/dicom'
       print ( s_2 )
       if not os.path.exists (  s_2 ):
         s_d = 'mkdir ' + s_2
         p = subprocess.Popen(s_d, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
         stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       if not os.path.exists (  s_3 ):
         s_d = 'mkdir ' + s_3
         p = subprocess.Popen(s_d, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
         stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       if ( os.path.isdir (  s_2 ) ):
          s_1 = 'dcm2nii -z y -m y -o ' + s_2 + ' ' + s_1
          print ( s_1 )
          p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
          i = 0
          while i < len ( stdout ):
               print ( i, stdout[i] )
               i += 1
          if ( os.path.isdir (  s_3 ) ):
             s_2 = s_2 + "/" + stdout[6].split('->' )[1]
             s_3 = 'cp ' + s_2 + '.gz ' + s_3 + '/deux.nii.gz' 
             print ( s_3 )
             p = subprocess.Popen(s_3, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
             stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
          #print ( stdout )
          #if ( os.path.isdir (  s_3 ) ):
          #   s_d = cp 
    m = m + 1


#dcm2niix  -z y -m y -o ./11/pdata/1/nii ./11/pdata/1/dicom
