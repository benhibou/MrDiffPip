#!/usr/bin/env python

# W_FSL_flirt.py
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

print (len ( sys.argv ))
if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = "Usage: W_FSL_flirt.py -basedir <base_dir> -filename <name_from>"
           s_2 = " -data_dir <data_dir>  -exp_number1 <exn1> -exp_number2 <exn2>" 
           print ( s_1 + s_2 );
           exit ( 1 );

if ( len ( sys.argv ) != 11 ) :
   s_1 = "Usage: W_FSL_flirt.py -basedir <base_dir> -filename <name_from>"
   s_2 = " -data_dir <data_dir>  -exp_numberD <exnD> -exp_numberT <exnT>" 
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
        elif ( cmdarg == "-exp_numberD" ):
           exp_numberD = sys.argv.pop ( 0 )
           if ( isint ( exp_numberD) ):
              exnD = int ( exp_numberD )
              print ( exnD)
        elif ( cmdarg == "-exp_numberT" ):
           exp_numberT = sys.argv.pop ( 0 )
           if ( isint ( exp_numberT) ):
              exnT = int ( exp_numberT )
m = -1
a = []
curdir = os.getcwd ( )
f = open ( name_from, 'r' )


for line in f:
    s_0 = data_dir
    s_1 = data_dir + '/'
    s_2 = '/usr/local/fsl/bin/flirt'
    m = m + 1
    if m > 0:
    #print( line.strip() )
       columns = ( line.strip() ).split()
       print ( columns )
       #s_0 = s_0 + columns[0] + '/' + columns[4] + "/2dseq.nii"
       s_1D = s_1 + columns[0] + '/' + columns[exnD] + \
             '/pdata/1/processed/zuzut_masked_1.nii'
       s_1T = s_1 + columns[0] + '/' + columns[exnT] + \
             '/pdata/1/processed/yuzut_masked.nii'
       s_1T_dir = s_1 + columns[0] + '/' + columns[exnT] + \
             '/pdata/1/processed/'
       print ( s_1D, "\t", s_1T )
       if ( os.path.isfile (  s_1D ) ):
          if ( os.path.isfile (  s_1T ) ):
             os.chdir ( s_1T_dir )
             s_T_out = re.sub ( r'masked.nii', "reg.nii", s_1T )
             print ( s_T_out )
             monreg = re.sub ( r'yuzut_masked.nii', "monregT2_D", s_1T )
             s1_cmd = 'flirt -in ' + s_1T +  ' -ref ' + s_1D + ' -out ' + s_T_out +  ' -omat ' + monreg
             print ( s1_cmd )
             p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
             stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )

f.close ( )
os.chdir ( curdir )
