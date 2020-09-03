#!/usr/bin/env python

# For_FSL_Macro.py
# To create the macro that will be
# run the DTI processing in fsl
#
# The BeBo Company, 2018

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
           s_1 = "Usage: For_FSL_Macro_With_Ecc_RotVec.py -basedir <base_dir> -filename <name_from>"
           s_2 = " -data_dir <data_dir>  -exp_number <exn>" 
           print ( s_1 + s_2 );
           exit ( 1 );

if ( len ( sys.argv ) != 9 ) :
   s_1 = "Usage: For_FSL_Macro_With_Ecc_RotVec.py -basedir <base_dir> -filename <name_from>"
   s_2 = " -data_dir <data_dir>  -exp_number <exn>" 
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
m = -1
a = []
curdir = os.getcwd ( )
f = open ( name_from, 'r' )


for line in f:
    s_0 = data_dir
    s_1 = data_dir + '/'
    #s_1 = '/usr/local/fsl/bin/eddy_correct ' + data_dir + '/'
    s_2 = '/usr/local/fsl/bin/dtifit --data=' + data_dir + '/'
    #s_2 = '/raid1/bboulat/FKBPDICOMS/20180314_094350_FKBP51_1_1/11/'
    m = m + 1
    if m > 0:
    #print( line.strip() )
       columns = ( line.strip() ).split()
       #s_0 = s_0 + columns[0] + '/' + columns[4] + "/2dseq.nii"
       s_1 = s_1 + columns[0] + '/' + columns[exn] + \
             '/pdata/1/processed/fsl_proc/'
       print ( s_1 )
       if not ( os.path.isdir (  s_1 ) ):
          os.mkdir ( s_1 )
          s_1cmd = 'cp ' + re.sub ( r'fsl_proc/', "4D.nii ", s_1 ) + s_1
          p = subprocess.Popen(s_1cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       s_1p = s_1 + 'data.ecclog'
       if not ( os.path.isfile (  s_1p ) ):
          s_1p = s_1 + '4D.nii '
          s_1pp = s_1 + 'data'
          s1_cmd = 'sh /home/spectro/diffusion/scripts/eddy_correct_with_bvecs_corr ' + s_1p + s_1pp + ' 0 ' + \
                    re.sub ( r'pdata/1/processed/fsl_proc/', "diff_bvec.txt ", s_1 ) 
          print ( s1_cmd )
          p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
          os.chdir ( s_1 )
          s1_cmd = 'bash /home/spectro/diffusion/scripts/read_ecclog.sh data.ecclog'
          p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
          stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       filrot = s_1 + 'ec_rot.txt'
       os.chdir ( s_1 )
       g = open ( filrot, 'r' )
       gn = 0
       for line_g in g:
           gn = gn + 1
           columns = ( line_g.strip( ) ).split( ) 
           for i in range ( len ( columns ) ):
               if ( float ( columns[i] ) > 0.01 ):
                  print ( "Achtung, Achtung: %s %d %f" % ( s_1, gn, float ( columns[i] ) ) )  
       g.close ( )
       os.chdir ( curdir )
       s1_cmd = '/usr/local/fsl/bin/dtifit ' + '--data=' + s_1 + 'data.nii.gz --out='
       s1_cmd = s1_cmd + s_1 + 'dti --mask=' + s_1 + '../BrainMask.nii '
       s1_cmd = s1_cmd + '--bvecs=' + re.sub ( r'pdata/1/processed/fsl_proc/', "diff_bvec.txt ", s_1 )
       s1_cmd = s1_cmd + '--bvals=' + re.sub ( r'pdata/1/processed/fsl_proc/', "diff_bval.txt ", s_1 )
       p = subprocess.Popen(s1_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
       stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       print (stdout )

f.close ( )
