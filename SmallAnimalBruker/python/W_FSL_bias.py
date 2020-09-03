#!/usr/bin/env python

# W_FSL_bias.py
# To run FSL bias between
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
           s_1 = "Usage: W_FSL_bias.py -basedir <base_dir> -filename <name_from>"
           s_2 = " -data_dir <data_dir>  -exp# <exn1> -avg# <avg>" 
           print ( s_1 + s_2 );
           exit ( 1 );

if ( len ( sys.argv ) != 11 ) :
   s_1 = "Usage: W_FSL_bias.py -basedir <base_dir> -filename <name_from>"
   s_2 = " -data_dir <data_dir>  -exp# <exnD> -avg# <avg>" 
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
        elif ( cmdarg == "-exp#" ):
           exp_numberD = sys.argv.pop ( 0 )
           if ( isint ( exp_numberD) ):
              exnD = int ( exp_numberD )
        elif ( cmdarg == "-avg#" ):
           avg = sys.argv.pop ( 0 )
           #if ( isint ( avg ) ):
              #avg_number = int ( avg )
m = -1
a = []
curdir = os.getcwd ( )
f = open ( name_from, 'r' )


for line in f:
    s_0 = data_dir
    s_1 = data_dir + '/'
    s_2 = '/usr/local/fsl/bin/fslroi'
    s_3 = '/usr/local/fsl/bin/fslmaths'
    s_4 = '/usr/local/fsl/bin/fast'
    m = m + 1
    if m > 0:
    #print( line.strip() )
       columns = ( line.strip() ).split()
       print ( columns )
       s_dir = s_1 + columns[0] + '/' + columns[exnD] + \
             '/pdata/1/processed/'
       print ( s_dir )
       if ( os.path.isdir (  s_dir ) ):
          s1_cmd = s_2 + ' ' + s_dir + '/4D.nii ' + s_dir + 'B_zero.nii 1 ' + avg
          print ( s1_cmd )
          p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
          s1_cmd = s_3 + ' ' + s_dir + 'B_zero.nii.gz -Tmean ' + s_dir + 'Avg_B_zero'
          print ( s1_cmd )
          p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
          s1_cmd = s_4 + ' -t 2 -o ' + s_dir +'fast -n 3 -b -B ' + s_dir + 'Avg_B_zero'
          print ( s1_cmd )
          p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
          s1_cmd = s_3 + ' ' + s_dir + '4D.nii -div ' + s_dir + 'fast_bias.nii.gz ' + \
                   s_dir + '4D_div -odt float'
          print ( s1_cmd )
          p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )

f.close ( )
os.chdir ( curdir )
