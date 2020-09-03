#!/usr/bin/env python

import sys
import os
import time
import string
import re
import numpy as np


if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
                print ( "Usage: Create_Tar_String.py -basedir <base_dir> -filename <name_from>");
                exit ( 1 );

if ( len ( sys.argv ) != 5 ) :
        print ( "Usage: Create_Tar_String.py -basedir <base_dir> -filename <name_from>" );
        exit ( 1 )

cur_dir = os.getcwd ( )

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
                base_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-filename" ):
                name_from = sys.argv.pop ( 0 )
                name_from = base_dir + "/" + name_from
m = 0
f = open ( name_from, 'r' )

s_1 = 'tar cvf FKBP.tar '

for line in f:
    m = m + 1
    if m > 1:
    #print( line.strip() )
       columns = ( line.strip() ).split()
       s_1 = s_1 + columns[0] + "/" + columns[4] + " " + columns[0] + "/" + columns[5] \
             + " "
       print ( s_1 )
