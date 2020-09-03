#!/usr/bin/env python

# W_Read_Diff_Val.py
# a wrapper to the script Read_Diff_Val
# Allows to run Read_diff_Val.py accross
# the many animals of a group study.
# the "basedir" is the directory where
# the file containing the parameters
# for the animals are stored, IDs,
# type of experiment, ... the file
# comes under "filename". 
# "basedir_f" is the directory of the study
# under which the data for all the animals
# are stored, "exp#" is the experiment number
# for the study. "filestring" is the name of the 
# file that contains the diffusion parameters
# to be collected (in Bruker Paravision, the
# method file). "nb0" is the number of B_0 experiment
# recorded (no diffusion gradient).

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
           s_1 = 'Usage: W_Read_Diff_Val.py -basedir <base_dir> -filename <file_name>'
           s_2 = ' -basedir_f <base_dir_from> -exp# <expn>'
           s_3 = ' -filestring <file_string> -nb0 <nb0>'
           print ( s_1 + s_2 + s_3 );
           exit ( 1 );

if ( len ( sys.argv ) != 13 ) :
   s_1 = 'Usage: W_Read_Diff_Val.py -basedir <base_dir> -filename <file_name>'
   s_2 = ' -basedir_f <base_dir_from> -exp# <expn>' 
   s_3 = ' -filestring <file_string> -nb0 <nb0>'
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
        elif ( cmdarg == '-basedir_f' ):
           base_dir_f = sys.argv.pop ( 0 ) + '/'
        elif ( cmdarg == '-exp#' ):
           exp_number = sys.argv.pop ( 0 )
           if ( isint ( exp_number ) ):
              exn = int ( exp_number )
        elif ( cmdarg == '-filestring' ):
           file_string = sys.argv.pop ( 0 )
        elif ( cmdarg == '-nb0' ):
           nb0 = sys.argv.pop ( 0 )
m = 0
f = open ( file_name, 'r' )


for line in f:
    if m > 0:
       s_1 = base_dir_f +'/'
       #print( line.strip() )
       columns = ( line.strip() ).split()
       s_2 = s_1 + columns[0] + "/" + columns[exn] + "/" + file_string
       s_1 = "-basedir " + s_1 + columns[0] + "/" + columns[exn] + "/ "
       print ( s_2 )
       if ( os.path.isfile (  s_2 ) ):
          s_1 = 'Read_Diff_Val.py ' + s_1 + \
                "-filename " + file_string + " -nb0 " + nb0
          #s_1 = s_1 + " " + base_dir_t + str ( m ) + "_" + file_string
          print ( s_1 )
       p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
       stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
    m = m + 1
