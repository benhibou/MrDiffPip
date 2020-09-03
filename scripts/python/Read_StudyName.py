#!/usr/bin/env python

# Read_StudyName.py
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
                print ( "Usage: Read_StudyName.py -basedir <base_dir> -filename <name_from> " \
                        "-listname <list_name>");
                exit ( 1 );

if ( len ( sys.argv ) != 7 ) :
        print ( "Usage: Read_StudyName.py -basedir <base_dir> -filename <name_from> "\
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
for i in range ( len ( list_dir_from ) ):
    #print (i, list_dir_from[i] )
    element = list_dir_from[i];
    arg1 = base_dir + "/" + list_dir_from[i] + "/" + name_from

    if os.path.isfile ( arg1 ):
       f = open ( arg1, 'r' )
       for line in f:
           #print( line )
           if ( re.search ( "SUBJECT_study_name=\(", line ) ):
              line = f.readline ( )
              nums = ( line.strip() )
              dict_name[element] = nums

Fil_List = base_dir + "/" + list_name + ".txt"
Fil_List_bck = base_dir + "/" + list_name + ".txt_bck" 
#if os.path.isfile ( Fil_List ):
cmd_1 = "cp " + Fil_List + " " + Fil_List_bck
cmd_2 = "cp " + Fil_List_bck + " " + Fil_List
 
if not os.path.exists ( Fil_List_bck ):
    os.system ( cmd_1 ) 
#else:
#    os.system ( cmd_2 )

i = 0
j = 0
#if os.path.exists ( Fil_List ):
MMF = open (Fil_List, 'w' )
subdir = dict_name.keys()
#for i in range ( 0, len ( subdir ) ):
#print ( dict_name.keys(), dict_name.values() )
for k, v in dict_name.items() :
    print ( k, v)
for key,val in dict_name.items():
    s = str( key ) + "\t" + str( val ) + "\n"
    #print ( s )
    MMF.write ( s )
#ModMethFil = "/home/nmrsu/someprog/rare_adj/scripts/mytry2"
#MMF = open (ModMethFil, 'w' )
#MMF.writelines ( contents )
MMF.close ( )
