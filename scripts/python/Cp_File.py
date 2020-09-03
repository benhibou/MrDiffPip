#!/usr/bin/env python

# Cp_File.py
# to copy files from different location
# as described in a text file into 
# one other directory for further
# processing. Would apply for example 
# to copy all the FA iimages associated with
# the different individuals in one cohort.
#
# The BeBo Company, 2019

def isint(value):
  try:
    int(value)
    return True
  except:
    return False

import sys
import os
import subprocess
import time
import string
import re
import numpy as np


if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = 'Usage: Cp_File.py -basedir <base_dir> -filename <file_name> -exp# <exp_number>'
           s_2 = ' -basedir_f <base_dir_from> -basedir_t <base_dir_to>'
           s_3 = ' -filestring <file_string>'
           print ( s_1 + s_2 + s_3 );
           exit ( 1 );

if ( len ( sys.argv ) != 15 ) :
   s_1 = 'Usage: Cp_File.py -basedir <base_dir> -filename <file_name> -exp# <exp_number>'
   s_2 = ' -basedir_f <base_dir_from> -basedir_t <base_dir_to>'
   s_3 = ' -filestring <file_string> -filestring2 <file_string2>'
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
        elif ( cmdarg == '-exp#' ):
           exp_number = sys.argv.pop ( 0 )
           if ( isint ( exp_number ) ):
              enne = int ( exp_number )
        elif ( cmdarg == '-basedir_f' ):
           base_dir_f = sys.argv.pop ( 0 ) + '/'
        elif ( cmdarg == '-basedir_t' ):
           base_dir_t = sys.argv.pop ( 0 ) + '/'
           print ( base_dir_t )
        elif ( cmdarg == '-filestring' ):
           file_string = sys.argv.pop ( 0 )
        elif ( cmdarg == '-filestring2' ):
           file_string2 = sys.argv.pop ( 0 )
m = 0
f = open ( file_name, 'r' )


for line in f:
    if m > 0:
       emme = 1000 + m
       s_1 = base_dir_f
       #print( line.strip() )
       columns = ( line.strip() ).split()
       s_1 = s_1 + columns[0] + "/" + columns[enne] + "/pdata/1/processed/" + file_string
       #print ( s_1 )
       if ( os.path.isfile (  s_1 ) ):
          s_1 = 'cp -f ' + s_1
          s_1 = s_1 + " " + base_dir_t + file_string2 + '/' + str ( emme ) + "_" + file_string
          print ( s_1 )
          p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       elif ( os.path.isfile (  s_1 ) == False ):
          s_1 = "\n\nWarning " + s_1 + " File does not exists\n\n"
          print ( s_1 )
    m = m + 1
