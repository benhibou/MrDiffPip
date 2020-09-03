#!/usr/bin/env python

# Cp_File_2.py
# to copy files from different location
# as described in a text file into 
# one other directory for further
# processing.
# The text file is supposed to contain
# only one string per line
#
# The BeBo Company, 2019

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
           s_1 = 'Usage: Cp_File_2.py -basedir <base_dir> -filename <file_name>'
           s_2 = ' -basedir_f <base_dir_from> -basedir_t <base_dir_to>'
           print ( s_1 + s_2 );
           exit ( 1 );

if ( len ( sys.argv ) != 9 ) :
   s_1 = 'Usage: Cp_File_2.py -basedir <base_dir> -filename <file_name>'
   s_2 = ' -basedir_f <base_dir_from> -basedir_t <base_dir_to>'
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
        elif ( cmdarg == '-basedir_t' ):
           base_dir_t = sys.argv.pop ( 0 ) + '/'
           print ( base_dir_t )
m = 0
f = open ( file_name, 'r' )


for line in f:
       s_1 = base_dir_f
       #print( line.strip() )
       columns = ( line.strip() )
       columns_f = base_dir_f + '/' + columns
       if ( os.path.isfile (  columns_f ) ):
          m = m + 1
          s_1 = 'cp -f ' + columns_f + ' ' + base_dir_t
          print ( s_1 )
          p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )

f.close ( )
print ( str ( m ) + ' file(s) copied' )
