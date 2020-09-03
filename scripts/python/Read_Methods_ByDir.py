#!/usr/bin/env python

# Read_Methods_ByDir.py
# to read    
# method file

"""
"""
import sys
import os
import time
import string
import re
import numpy as np
from scipy.stats import ttest_ind
from scipy.special import stdtr
import matplotlib.pyplot as plt
from pylab import *
import pylab as P
import string
import time

def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

#from datascience import stats
# if element is found it returns index of element else returns -1

def find_element_in_list(element, list_element):
    try:
        index_element = list_element.index(element)
        return index_element
    except ValueError:
        return None

if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
                print ( "Usage: Read_Methods_ByDir.py -basedir <base_dir> -filename <name_from> " \
                        "-listname <list_name>");
                exit ( 1 );

if ( len ( sys.argv ) != 7 ) :
        print ( "Usage: Read_Methods_ByDir.py -basedir <base_dir> -filename <name_from> "\
                "-listname <list_name>" );
        exit ( 1 )

cur_dir = os.getcwd ( )

a = 0
array_vec = []
array_val = []
dict_name = {}

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
                base_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-filename" ):
                name_from = sys.argv.pop ( 0 )
        elif ( cmdarg == "-listname" ):
                list_name = sys.argv.pop ( 0 )
m = 0
list_dir_from = os.popen ( "ls -1 %s" % base_dir ).read()
list_dir_from = list_dir_from.split ( '\n' )
list_dir_from.pop()

Fil_List = base_dir + "/" + list_name + ".txt"
Fil_List_bck = base_dir + "/" + list_name + ".txt_bck" 
#if os.path.isfile ( Fil_List ):
cmd_1 = "cp " + Fil_List + " " + Fil_List_bck
cmd_2 = "cp " + Fil_List_bck + " " + Fil_List
 
if not os.path.exists ( Fil_List_bck ):
    os.system ( cmd_1 ) 
#else:
#    os.system ( cmd_2 )

MMF = open (Fil_List, 'w' )

s_1 = ''
s_2 = ''
s_3 = ''
nums = ''

for i in range ( len ( list_dir_from ) ):
    #print i, list_dir_from[i]
    element = list_dir_from[i];
    arg1 = base_dir + "/" + list_dir_from[i]

    if os.path.isdir ( arg1 ):
       subj = arg1 + "/subject"
       if os.path.isfile ( subj ):
          print ( subj )
          MMG = open ( subj, 'r' )
          for line in MMG:
          #print( line )
             if ( re.search ( "SUBJECT_study_name=\(", line ) ):
                line = MMG.readline ( )
                nums = ( line.strip() )
                print ( nums )
          MMG.close ( )
       list_dir_from2 = os.popen ( "ls -1 %s" % arg1 ).read()
       list_dir_from2 = list_dir_from2.split ( '\n' )
       list_dir_from2.pop()
       for j in range ( len ( list_dir_from2 ) ):
           arg2 = arg1 + "/" + list_dir_from2[j]
           m_1 = 0
           if os.path.isdir ( arg2 ):
              arg3 = arg2 + "/" + name_from
              if os.path.isfile ( arg3 ):
                 #print ( arg3 )
                 f = open ( arg3, 'r' )
                 s = ''
                 for line in f:
                     #print( line )
                     line = line.strip ( )
                     if ( re.search ( "\#\#\$Method=", line ) ):
                        #print ( arg1, "\t", list_dir_from2[i], "\t",\
                        #        re.sub ( r'>', '', re.sub ( r'.*:', '', line ) ) )
                        if ( line.find ( "FLASH" ) != -1 ):
                           arg4 = arg2 + "/pdata/1/dicom/MRIm205.dcm"
                           if os.path.isfile ( arg4 ):
                                m_1 = 1
                                s_1 = list_dir_from2[j]
                                print ( arg1, "Hi\t", list_dir_from2[j], "\t",\
                                        re.sub ( r'>', '', re.sub ( r'.*:', '', line ) ) )
                        if ( line.find ( "FieldMap" ) != -1 ):
                           arg4 = arg2 + "/pdata/1/dicom/MRIm64.dcm"
                           if os.path.isfile ( arg4 ):
                                m_1 = 2
                                s_2 = list_dir_from2[j]
                                print ( arg1, "Hello\t", list_dir_from2[j], "\t",\
                                        re.sub ( r'>', '', re.sub ( r'.*:', '', line ) ) )
                        if ( line.find ( "nmrsuDtiEpi" ) != -1 ):
                           arg4 = arg2 + "/pdata/1/dicom/MRIm3395.dcm"
                           if os.path.isfile ( arg4 ):
                                m_1 = 3
                                s_3 = list_dir_from2[j]
                                print ( arg1, "Hello\t", list_dir_from2[j], "\t",\
                                        re.sub ( r'>', '', re.sub ( r'.*:', '', line ) ) )
           if ( m_1 == 3 ):
              s = list_dir_from[i] + "\t" + nums + "\t" + s_1 + "\t" + s_2 + "\t" + s_3 + "\n"
              MMF.write ( s )

MMF.close ( )
