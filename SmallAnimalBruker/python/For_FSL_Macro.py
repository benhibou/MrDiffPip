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

if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = "Usage: For_FSL_Macro.py -basedir <base_dir> -filename <name_from>"
           s_2 = " -data_dir <data_dir>  -exp_number <exn>" 
           print ( s_1 + s_2 );
           exit ( 1 );

if ( len ( sys.argv ) != 9 ) :
   s_1 = "Usage: For_FSL_Macro.py -basedir <base_dir> -filename <name_from>"
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
f = open ( name_from, 'r' )


for line in f:
    s_0 = data_dir
    s_1 = '/usr/local/fsl/bin/dtifit --data=' + data_dir + '/'
    s_2 = "/raid1/bboulat/FKBP/20180314_094350_FKBP51_1_1/11/"
    m = m + 1
    if m > 0:
    #print( line.strip() )
       columns = ( line.strip() ).split()
       #s_0 = s_0 + columns[0] + '/' + columns[4] + "/2dseq.nii"
       s_1 = s_1 + columns[0] + '/' + columns[exn] + \
             "/pdata/1/r2dseq.nii --out="
       s_1 = s_1 + data_dir + '/' + columns[0] + '/' + columns[exn] + \
             "/pdata/1/dti --mask="
       s_1 = s_1 + data_dir + '/' + columns[0] + '/' + columns[exn] + \
             "/pdata/1/BrainMask_" + str ( m ) + ".nii --bvecs="
       #s_1 = s_1 + data_dir + '/' + columns[0] + '/' + columns[exn] + \
       #      "/pdata/1/2dseq_bm_" + str ( m ) + ".nii --bvecs="
             
       s_1 = s_1 + s_2 + "diff_bvec.txt --bvals=" + s_2 + "diff_bval.txt --wls"
       print ( s_1 )
       #os.system ( s_1 )
       p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
       stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       #my_out = ( stdout[0].strip() ).split ( ':' )[1]
       print ( stdout )

f.close ( )

#/usr/local/fsl/bin/dtifit --data=/raid1/bboulat/FKBP_2/20180328_133537_549_1_1/7/pdata/1/2dseq.nii.gz --out=/raid1/bboulat/FKBP_2/20180328_133537_549_1_1/7/pdata/1/dti --mask=/raid1/bboulat/FKBP_2/20180328_133537_549_1_1/7/pdata/1/2dseq_bm_21.nii --bvecs=/raid1/bboulat/FKBP/20180314_094350_FKBP51_1_1/11/diff_bvec.txt --bvals=/raid1/bboulat/FKBP/20180314_094350_FKBP51_1_1/11/diff_bval.txt --wls
