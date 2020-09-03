#!/usr/bin/env python


# printGrad.py
#
# The BeBo Company, 2019


import sys
import os
import subprocess
import time
import string
import re
import numpy as np
import nibabel as nib
from dipy.io import read_bvals_bvecs
from dipy.core.gradients import gradient_table
from dipy.viz import window, actor


if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = 'Usage: printGrad.py -basedir <base_dir> -fbvals <file_name> -fbvecs <flie_name>'
           print ( s_1 );
           exit ( 1 );

if ( len ( sys.argv ) != 7 ) :
   s_1 = 'Usage: printGrad.py -basedir <base_dir> -fbval <file_name> -fbvecs <flie_name>'
   print ( s_1 );
   exit ( 1 )

cur_dir = os.getcwd ( )

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
           base_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-fbvals" ):
           fbvals = sys.argv.pop ( 0 )
           fbvals = base_dir + "/" + fbvals
        elif ( cmdarg == "-fbvecs" ):
           fbvecs = sys.argv.pop ( 0 )
           fbvecs = base_dir + "/" + fbvecs


#print( line.strip() )

if os.path.isfile ( fbvecs ):
   bvals, bvecs = read_bvals_bvecs ( fbvals, fbvecs )
   gtab = gradient_table ( bvals, bvecs )
   print ( bvecs.T[2,7] )
   #for att in dir ( bvecs ):
   #    print ( att, getattr ( bvecs, att ) )
   #print ( gtab.gradients )
   colors_b = window.colors.blue * np.ones( (96, 3) )
   colors = colors_b
   colors = np.insert( colors, (0, colors.shape[0]), np.array([0,0,0]), axis = 0 )
   ren = window.Renderer ( )
   ren.SetBackground ( 0, 0, 0 )
   ren.add ( actor.point ( gtab.gradients, colors, point_radius = 40 ) )
   window.record ( ren, out_path = 'gradients.png', size = ( 300, 300 ) )
   window.show ( ren )
