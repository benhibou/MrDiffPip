# Rotate vector module
#
# The Bebo Company, 2018


import sys
import os
import numpy as np
import subprocess

def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

def extrRotFromAff_txt ( file_name ):
    if os.path.isfile (  file_name ):
       f = open ( file_name, 'r' )
       i = 0
       for line in f:
           columns.append ( ( line.strip ( ) ).split ( ) )
       print ( float ( columns[1][2] ) * float ( columns[1][0] ) )
       s_x = np.sqrt ( np.square ( float ( columns[1][0] ) )\
                       + np.square (  float ( columns[2][0]  ) ) \
                       + np.square ( float ( columns[3][0] ) ) )

       s_y = np.sqrt ( np.square ( float ( columns[1][1] ) )\
                       + np.square (  float ( columns[2][1]  ) ) \
                       + np.square ( float ( columns[3][1] ) ) )
 
       s_z = np.sqrt ( np.square ( float ( columns[1][2] ) )\
                       + np.square (  float ( columns[2][2]  ) ) \
                       + np.square ( float ( columns[3][2] ) ) )

       x = np.array ( [ float ( columns[1][0] ), float ( columns[2][0] ), float ( columns[3][0] ) ] ) / s_x
       y = np.array ( [ float ( columns[1][1] ), float ( columns[2][1] ), float ( columns[3][1] ) ] ) / s_y
       z = np.array ( [ float ( columns[1][2] ), float ( columns[2][2] ), float ( columns[3][2] ) ] ) / s_z
       R = np.array ( [ x, y, z ] )

       # The actual otation matrix will be "R.T".

       print ( np.dot ( R.T, R ) )
       return ( R.T )

def extrRotFromAff ( file_name, nifti_form ):
    if os.path.isfile (  file_name ):
       s_1 = 'fslhd ' + file_name
       print ( s_1 )
       p = subprocess.Popen(s_1, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
       stdout = ((p.communicate()[0]).decode ( 'ascii' )).split( '\n' )
       print ( stdout )
       i = 0
       while i < len ( stdout ):
           print ( i, stdout[i] )
           i += 1
       if ( nifti_form == 'q'):
          a = ( stdout[47].strip ( ) ).split ( )
          b = ( stdout[48].strip ( ) ).split ( )
          c = ( stdout[49].strip ( ) ).split ( )
       elif ( nifti_form == 's' ):
          a = ( stdout[56].strip ( ) ).split ( )
          b = ( stdout[57].strip ( ) ).split ( )
          c = ( stdout[58].strip ( ) ).split ( )
       print ( a )
       print ( b )
       print ( c )
       s_x = np.sqrt ( np.square ( float ( a[1] ) )\
		       + np.square (  float ( b[1]  ) ) \
		       + np.square ( float ( c[1] ) ) )   

       s_y = np.sqrt ( np.square ( float ( a[2] ) )\
		       + np.square (  float ( b[2]  ) ) \
		       + np.square ( float ( c[2] ) ) )   

       s_z = np.sqrt ( np.square ( float ( a[3] ) )\
		       + np.square (  float ( b[3]  ) ) \
		       + np.square ( float ( c[3] ) ) )   

       x = np.array ( [ float ( a[1] ), float ( b[1] ), float ( c[1] ) ] ) / s_x
       y = np.array ( [ float ( a[2] ), float ( b[2] ), float ( c[2] ) ] ) / s_y
       z = np.array ( [ float ( a[3] ), float ( b[3] ), float ( c[3] ) ] ) / s_z
       R = np.array ( [ x, y, z ] )

       # The actual rotation matrix will be "R.T".

       print ( np.dot ( R.T, R ) )
       return ( R.T )

def effectRot (file_name, file_out, R ):

    f = open ( file_name, 'r' )
    g = open ( file_out, 'w' )


    for line in f:
        array_vec = []
        nums = ( line.strip() ).split()
        for num in nums:
            if isfloat ( num ):
               array_vec.append ( float ( num ) )
        a = array_vec[0]
        b = np.array ( array_vec[1:4] )
        #b = np.transpose ( b )
        x = np.array ( [[1], [1], [1]] )
        x = np.matrix ( b )
        #print ( x )
        y = np.transpose ( np.dot ( R,  np.transpose ( x ) ) )
        #print ( y )
        #print (array_vec )
        #print (b )
        #print (np.transpose ( np.dot (R, np.transpose(x) ) ) )
        g.write ( " %.6f %.6f %.6f %.6f\n" % ( a, y.item ( 0 ), y.item ( 1 ), y.item ( 2 ) ) )
    f.close ( )
    g.close ( )
