#!/usr/bin/env python

# BM_NiftyManip.py
# A script to adjust the nifti
# header of the BrainMask files
# which were not written appropriately
# by ImageJ 

import sys
import os
import subprocess
import time
import string
import re
import numpy as np
import nibabel as nib

if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
           s_1 = 'Usage: BM_NiftyManip.py -basedir <base_dir> -filename <file_name>'
           s_2 = ' -basedir_f <base_dir_from> -basedir_t <base_dir_to>'
           s_3 = ' -filestring1 <file_string> -filestring2 <file_string>'
           print ( s_1 + s_2 + s_3 );
           exit ( 1 );

if ( len ( sys.argv ) != 13 ) :
   s_1 = 'Usage: BM_NiftyManip.py -basedir <base_dir> -filename <file_name>'
   s_2 = ' -basedir_f <base_dir_from> -basedir_t <base_dir_to>'
   s_3 = ' -filestring1 <file_string> -filestring2 <file_string>'
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
           print ( file_name )
        elif ( cmdarg == '-basedir_f' ):
           base_dir_f = sys.argv.pop ( 0 ) + '/'
        elif ( cmdarg == '-basedir_t' ):
           base_dir_t = sys.argv.pop ( 0 ) + '/'
        elif ( cmdarg == '-filestring1' ):
           file_string1 = sys.argv.pop ( 0 )
        elif ( cmdarg == '-filestring2' ):
           file_string2 = sys.argv.pop ( 0 )
m = 0
f = open ( file_name, 'r' )


for line in f:
    if m > 0:
       s_0 = base_dir_t
       s_1 = base_dir_f
       #print( line.strip() )
       columns = ( line.strip() ).split()
       s_1p = s_0 + columns[0] + "/" + columns[4] + \
             "/pdata/1/" + file_string2 + "_" + str ( m ) \
             + "_mod.nii"

       s_0 = s_0 + columns[0] + "/" + columns[4] + \
             "/pdata/dicom/" + file_string1 + ".nii"
       print ( s_0 )

       s_1 = s_1 + columns[0] + "/" + columns[4] + \
             "/pdata/1/" + file_string2 \
             + ".nii"
       
       print ( s_1 )
       print ( s_1p )
       if ( os.path.isfile (  s_0 ) ):
          if ( os.path.isfile (  s_1 ) ):
             img = nib.load ( s_0 )
             hdr = img.header
             m_bm = nib.load ( s_1 )
             bm_header = m_bm.header
             #print ( bm_header, "\n\n" )
             bm_header['pixdim'] = hdr['pixdim']
             bm_header['qform_code'] = hdr['qform_code']
             bm_header['sform_code'] = hdr['sform_code']
             bm_header['quatern_b'] = hdr['quatern_b']
             bm_header['quatern_c'] = hdr['quatern_c']
             bm_header['quatern_d'] = hdr['quatern_d']
             bm_header['qoffset_x'] = hdr['qoffset_x']
             bm_header['qoffset_y'] = hdr['qoffset_y']
             bm_header['qoffset_z'] = hdr['qoffset_z']
             bm_header['srow_z'] = hdr['srow_z']
             bm_header['srow_y'] = hdr['srow_y']
             bm_header['srow_x'] = hdr['srow_x']
             print ( bm_header, "\n\n" )
             nib.save( m_bm, s_1p )
             #print ( bm_header, "\n\n" )

    m = m + 1

#example.filename = '/raid1/bboulat/FKBP_3/20180314_134047_FKBP51_1_2/9/pdata/1/r2dseq.nii'
#img = nib.load ( example_filename )
#hdr = img.header
#bm = '/raid1/bboulat/FKBP_3/20180314_134047_FKBP51_1_2/9/pdata/1/BM.nii'
#m_bm = nib.load(bm)
#bm_header = m_bm.header
#bm_header['qform_code'] = hdr['qform_code']
#bm_header['sform_code'] = hdr['sform_code']
#bm_header['quatern_b'] = hdr['quatern_b']
#bm_header['quatern_c'] = hdr['quatern_c']
#bm_header['quatern_d'] = hdr['quatern_d']
#bm_header['qoffset_x'] = hdr['qoffset_x']
#bm_header['qoffset_y'] = hdr['qoffset_y']
#bm_header['qoffset_z'] = hdr['qoffset_z']
#bm_header['srow_z'] = hdr['srow_z']
#bm_header['srow_y'] = hdr['srow_y']
#bm_header['srow_x'] = hdr['srow_x']
#nib.save( m_bm, '/raid1/bboulat/FKBP_3/20180314_134047_FKBP51_1_2/9/pdata/1/BM_Mod.nii')
#
