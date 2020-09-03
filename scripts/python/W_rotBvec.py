#!/usr/bin/env python

# W_rotBvec.py
# a wrapper to the script rotBvec
# Allows to run Read_diff_Val.py accross
# the many animals of a group study.
# the "basedir" is the directory where
# the file containing the parameters
# for the animals are stored, IDs,
# type of experiment, ... the file
# comes under "filename". 
# "basedir_f" is the directory of the study
# under which the data for all the animals
# are stored. "filestring" is the name of the 
# file that contains the diffusion parameters
# to be collected.
#
# The BeBo Company, 2018

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
           s_1 = 'Usage: W_rotBvec.py -basedir <base_dir> -filename <file_name>'
           s_2 = ' -filin <filin> -transpose <trp> -form <flbl>'
           s_3 = ' -filvec <filvec> -filout <filout>'
           print ( s_1 + s_2 + s_3 );
           exit ( 1 );

if ( len ( sys.argv ) != 21 ) :
   s_1 = 'Usage: W_rotBvec.py -basedir <base_dir> -filename <file_name>'
   s_2 = ' -basedir_f1 <basedir_f1> -basedir_f2 <basedir_f2> -exp# <exn> -filin <filin>' 
   s_3 = ' -transpose <trp> -form <flbl> -filvec <filvec> -filout <filout>'
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
        if ( cmdarg == '-basedir_f1' ):
           basedir_f1 = sys.argv.pop ( 0 )
        if ( cmdarg == '-basedir_f2' ):
           basedir_f2 = sys.argv.pop ( 0 )
        if ( cmdarg == '-exp#' ):
           exp_number = sys.argv.pop ( 0 )
           if ( isint ( exp_number ) ):
              exn = int ( exp_number )
        if ( cmdarg == '-filin' ):
           filin = sys.argv.pop ( 0 )
        elif ( cmdarg == '-transpose' ):
           trp = sys.argv.pop ( 0 )
           print ( trp )
        elif ( cmdarg == '-form' ):
           flbl = sys.argv.pop ( 0 )
        elif ( cmdarg == '-filvec' ):
           filvec = sys.argv.pop ( 0 )
        elif ( cmdarg == '-filout' ):
           filout = sys.argv.pop ( 0 )
m = 0
f = open ( file_name, 'r' )
curdir = os.curdir


for line in f:
    if m > 0:
       s_1 = basedir_f1
       #print( line.strip() )
       columns = ( line.strip() ).split()
       s_2 = s_1 + columns[0] + "/" + columns[exn] + '/'
       s_1 = basedir_f2
       s_3 = s_1 + columns[0] + "/" + columns[exn] + '/'
       #s_1 = "-basedir " + s_1 + columns[0] + "/" + columns[exn] + my_string + " "
       print ( s_2 )
       #print ( s_3 )
       if ( os.path.isdir (  s_2 ) ):
          s_1 = '/home/spectro/diffusion/scripts/rotBvec.py -basedir ' + s_2 + \
                ' -filename ' + filin + ' -transpose ' + trp + ' -form ' + flbl + \
                ' -filevec ' + s_3 + filvec + ' -filout ' + s_3 + filout
          #s_1 = s_1 + " " + base_dir_t + str ( m ) + "_" + file_string
          print ( s_1 )
       p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
       stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       #print ( stdout)
       s_1 = '/home/spectro/myProg/myPython/DiffValForDipy_Val1st.py -basedir ' + s_3 + \
             ' -filename ' + filout
       #s_1 = '/home/spectro/myProg/myPython/DiffValForDipy_Val1st.py -basedir ' + os.curdir + \
       print ( s_1 )
       p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
       stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       #print (stdout)
       #s_1 = 'cp ' + os.curdir + '/diff_bval.txt ' + s_2 + 'diff_bval.txt'
       #p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
       #stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       #s_1 = 'cp ' + os.curdir + '/diff_bvec.txt ' + s_2 + 'diff_bvec.txt'
       #p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
       #stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       #monfil = s_2 + re.sub ( r'trois.nii', "monvec3.txt", filin )
       #s_1 = 'cp ' + os.curdir + '/monvec3 ' + monfil
       #p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
       #stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
    m = m + 1
