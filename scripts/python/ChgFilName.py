#!/usr/bin/env python

# ChgFilNam.py
# to check on correlation of the user
# ratings with the IAPS ratings

"""
"""
import sys
import os
import time
import numpy as np
from scipy.stats import ttest_ind
from scipy.special import stdtr
import matplotlib.pyplot as plt
from pylab import *
import pylab as P
#from datascience import stats

if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
                print ( "Usage: ChgFilNam.py -basedir <base_dir> -name1 <name_from> ");
                exit ( 1 );

if ( len ( sys.argv ) != 5 ) :
        print ( "Usage: ChgFilNam.py -basedir <base_dir> -name1 <name_from> " );
        exit ( 1 )

cur_dir = os.getcwd ( )
cmdarg = sys.argv.pop ( 0 );

def my_ttest ( a, b ):
    abar = a.mean()
    avar = a.var(ddof=1)
    na = a.size
    adof = na - 1
    print '%.3f %.3f' % (abar, avar)

    bbar = b.mean()
    bvar = b.var(ddof=1)
    print '%.3f %.3f' % (bbar, bvar)
    nb = b.size
    bdof = nb - 1

    # Compute Welch's t-test using the descriptive statistics.
    tf = (abar - bbar) / np.sqrt(avar/na + bvar/nb)
    dof = (avar/na + bvar/nb)**2 / (avar**2/(na**2*adof) + bvar**2/(nb**2*bdof))
    pf = 2*stdtr(dof, -np.abs(tf))
    bbar = 0
    bvar = 0
    return ( tf, pf );

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-basedir' ):
                base_dir = sys.argv.pop ( 0 )
        elif ( cmdarg == "-name1" ):
                name_from1 = sys.argv.pop ( 0 )

list_dir_from = os.popen ( "ls -1 %s" % base_dir ).read()
list_dir_from = list_dir_from.split ( '\n' )
list_dir_from.pop()
j = 1
name_frome1 = []
name_frome2 = []
name_frome3 = []
name_frome4 = []
view_neutral1 = []
view_negative1 = []
detach_negative1 = []
permit_negative1 = []
view_neutral2 = []
view_negative2 = []
detach_negative2 = []
permit_negative2 = []
view_neutral3 = []
view_negative3 = []
view_neutral4 = []
view_negative4 = []
arr_vneu1 = []
arr_vneg1 = []
arr_vneu2 = []
arr_vneg2 = []
arr_detn = []
arr_pern = []
arr_diff = []
arr_vneu1_ia = []
arr_vneg1_ia = []
arr_vneu2_ia = []
arr_vneg2_ia = []
arr_detn_ia = []
arr_pern_ia = []
arr_pmd = []
mamean = []
axx = []
a_tot = []
a_tot_ia = []
pmd = base_dir + "/pmd.txt"

for i in range ( len ( list_dir_from ) ):
    #print i, list_dir_from[i]
    element = list_dir_from[i];
    arg1 = base_dir + "/" + list_dir_from[i] + "/ses000D/" + name_from1;
    arg2 = base_dir + "/" + list_dir_from[i] + "/ses000D/" + name_from2;
    arg3 = base_dir + "/" + list_dir_from[i] + "/ses000P/" + name_from1;
    arg4 = base_dir + "/" + list_dir_from[i] + "/ses000P/" + name_from2;
    #print arg2, "\t", arg1;
    if os.path.isfile(arg1): 
       name_frome1.append ( arg1 );
       name_frome2.append ( arg2 );
       name_frome3.append ( arg3 );
       name_frome4.append ( arg4 );
       j += 1;
       #print j, "\t", name_frome1 
for i in range ( 0, j-1):
    f = open ( name_frome1[i], 'r' )
    for line in f:
        line2 = line.strip ( )
        line1 = line2.split ( )
        if line1[1] == 'view_neutral':
           view_neutral1.append ( line1[5] )
        elif line1[1] == 'view_negative':
           view_negative1.append ( line1[5] )
        elif line1[1] == 'detach_negative':
           detach_negative1.append ( line1[5] )
        else:
           k = 0;
    f.close ( )
    arry_neutral1 = np.array(map(float, view_neutral1))
    arry_negative1 = np.array(map(float, view_negative1))
    arry_detneg1 = np.array(map(float, detach_negative1))
    arr_vneu1.append(arry_neutral1)
    arr_vneg1.append(arry_negative1)
    arr_detn.append(arry_detneg1)
    view_neutral1 = []
    view_negative1 = []
    detach_negative1 = []
    #print amin(arry_negative1), "\t", amax(arry_negative1), "\t", percentile(arry_negative1,25), "\t", percentile(arry_negative1,50), "\t", median(arry_negative1), "\t",percentile(arry_negative1,75), "\t", std(arry_negative1), "\n";
    #print(stats.summary(arry_negative1))
    f = open ( name_frome2[i], 'r' )
    for line in f:
        line2 = line.strip ( )
        line1 = line2.split ( )
        if line1[1] == 'view_neutral':
           view_neutral2.append ( line1[5] )
        elif line1[1] == 'view_negative':
           view_negative2.append ( line1[5] )
        elif line1[1] == 'detach_negative':
           detach_negative2.append ( line1[5] )
        else:
           k = 0;
    f.close ( )
    arry_neutral2 = np.array(map(float, view_neutral2))
    arry_negative2 = np.array(map(float, view_negative2))
    arry_detneg2 = np.array(map(float, detach_negative2))
    arr_vneu1_ia.append(arry_neutral2)
    arr_vneg1_ia.append(arry_negative2)
    arr_detn_ia.append(arry_detneg2)
    view_neutral2 = []
    view_negative2 = []
    detach_negative2 = []
    f = open ( name_frome3[i], 'r' )
    for line in f:
        line2 = line.strip ( )
        line1 = line2.split ( )
        if line1[1] == 'view_neutral':
           view_neutral3.append ( line1[5] )
        elif line1[1] == 'view_negative':
           view_negative3.append ( line1[5] )
        elif line1[1] == 'permit_negative':
           permit_negative1.append ( line1[5] )
        else:
           k = 0;
    f.close ( )
    arry_neutral3 = np.array(map(float, view_neutral3))
    arry_negative3 = np.array(map(float, view_negative3))
    arr_vneu2.append(arry_neutral3)
    arr_vneg2.append(arry_negative3)
    arry_perneg1 = np.array(map(float, permit_negative1))
    arr_pern.append(arry_perneg1)
    view_neutral3 = []
    view_negative3 = []
    permit_negative1 = []
    f = open ( name_frome4[i], 'r' )
    for line in f:
        line2 = line.strip ( )
        line1 = line2.split ( )
        if line1[1] == 'view_neutral':
           view_neutral4.append ( line1[5] )
        elif line1[1] == 'view_negative':
           view_negative4.append ( line1[5] )
        elif line1[1] == 'permit_negative':
           permit_negative2.append ( line1[5] )
        else:
           k = 0;
    f.close ( )
    arry_neutral4 = np.array(map(float, view_neutral4))
    arry_negative4 = np.array(map(float, view_negative4))
    arr_vneu2_ia.append(arry_neutral4)
    arr_vneg2_ia.append(arry_negative4)
    arry_perneg1 = np.array(map(float, permit_negative2))
    arr_pern_ia.append(arry_perneg1)
    view_neutral4 = []
    view_negative4 = []
    permit_negative2 = []

arr_vn1 = np.array(arr_vneu1)
a_vneu1 = arr_vn1.flatten()
a_tot.append(a_vneu1)
arr_vn2 = np.array(arr_vneu2)
a_vneu2 = arr_vn2.flatten()
a_tot.append(a_vneu2)

arr_vn1 = np.array(arr_vneg1)
a_vneg1 = arr_vn1.flatten()
a_tot.append(a_vneg1)
arr_vn2 = np.array(arr_vneg2)
a_vneg2 = arr_vn2.flatten()
a_tot.append(a_vneg2)

arr_vn1 = np.array(arr_detn)
a_detn = arr_vn1.flatten()
a_tot.append(a_detn)
arr_vn2 = np.array(arr_pern)
a_pern = arr_vn2.flatten()
a_tot.append(a_pern)

arr_vn1_ia = np.array(arr_vneu1_ia)
a_vneu1_ia = arr_vn1_ia.flatten()
a_tot_ia.append(a_vneu1_ia)
arr_vn2_ia = np.array(arr_vneu2_ia)
a_vneu2_ia = arr_vn2_ia.flatten()
a_tot_ia.append(a_vneu2_ia)

arr_vn1_ia = np.array(arr_vneg1_ia)
a_vneg1_ia = arr_vn1_ia.flatten()
a_tot_ia.append(a_vneg1_ia)
arr_vn2_ia = np.array(arr_vneg2_ia)
a_vneg2_ia = arr_vn2_ia.flatten()
a_tot_ia.append(a_vneg2_ia)

arr_vn1_ia = np.array(arr_detn_ia)
a_detn_ia = arr_vn1_ia.flatten()
a_tot_ia.append(a_detn_ia)
arr_vn2_ia = np.array(arr_pern_ia)
a_pern_ia = arr_vn2_ia.flatten()
a_tot_ia.append(a_pern_ia)

for i in range ( 0, np.shape ( arr_detn )[0]):
    mamean.append ( np.mean ( arr_pern[i] ) - np.mean ( arr_detn[i] ) )
    arr_pmd.append([])
    for j in range ( 0, np.shape ( arr_detn )[1]):
          arr_pmd[i].append(arr_pern[i][j] - arr_detn[i][j])

f = open ( pmd, 'w' )
for i in range ( 0, np.shape ( arr_detn )[0]):
    f.write ( "%f\n" %  mamean[i] )
f.close ( )

conditions = ["vneu_d", "vneu_p", "vneg_d", "vneg_p", "detach", "permit"]

print np.shape(arr_detn)
#time.sleep(5)
               
meanpointprops = dict(markersize=2)
fig = plt.figure()
ax = fig.add_subplot(111)
plt.title("Per Conditions Average Accross Subjects\n", fontsize=16)
plt.suptitle("\nSubject Ratings", fontsize = 14.5 )
ax.boxplot(a_tot, 0, '', meanprops=meanpointprops, showmeans = True )
ax.set_xticklabels(conditions, rotation=45, fontsize=8)
#plt.setp(xticklabels, rotation=45, fontsize=8)
plt.ylim( -250, 250 )
plt.ylabel("RATINGS",fontsize=15)
plt.show()

ax = plt.subplot(2,1,1)
plt.title("view_neutral, subject ratings\n", fontsize=16)
plt.suptitle("\n\nscale = [-200, 200]", fontsize=10)
plt.boxplot(arr_vneu1, 0, '', meanprops=meanpointprops, showmeans = True )
plt.text(1.0, 60, 'Detach Session')
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.ylim( -210, 100 )
ax.yaxis.set_label_coords(-0.06, -0.060)
plt.ylabel("RATINGS",fontsize=15)
plt.subplot(2,1,2)
plt.boxplot(arr_vneu2, 0, '', meanprops=meanpointprops, showmeans = True )
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.text(1.0, 60, 'Permit Session')
plt.ylim( -210, 100 )
plt.xlabel("USER LABEL", fontsize=15)
plt.show()

ax = plt.subplot(2,1,1)
plt.title("view_negative, subject ratings\n", fontsize=16)
plt.suptitle("\n\nscale = [-200, 200]", fontsize=10)
plt.ylim( -210, 210 )
plt.boxplot(arr_vneg1, 0, '', meanprops=meanpointprops, showmeans = True )
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.ylim( -210, 210 )
plt.text(24, 170, 'Detach Session')
ax.yaxis.set_label_coords(-0.06, -0.06)
plt.ylabel("RATINGS",fontsize=15)
plt.subplot(2,1,2)
plt.ylim( -210, 210 )
plt.boxplot(arr_vneg2, 0, '', meanprops=meanpointprops, showmeans = True )
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.ylim( -210, 210 )
plt.text(24, 170, 'Permit Session')
plt.xlabel("USER LABEL", fontsize=15)
plt.show()
  
ax = plt.subplot(2,1,1)
#ax.set_title("Detach_negative, Subject ratings\nScale = [-200, 200]", fontsize=10)
plt.text(1.5,150, "Detach_negative, Subject ratings\nScale = [-200, 200]", fontsize=8)
plt.boxplot(arr_detn, 0, '', meanprops=meanpointprops, showmeans = True )
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.ylim( -210, 210 )
ax.yaxis.set_label_coords(-0.06, -0.060)
plt.ylabel("RATINGS",fontsize=15)
ax = plt.subplot(2,1,2)
plt.boxplot(arr_pern, 0, '', meanprops=meanpointprops, showmeans = True )
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.ylim( -210, 210 )
#plt.xlabel("Permit_negative, Subject ratings\nScale = [-200, 200]", fontsize=10)
plt.text(1.5,-190, "Permit_negative, Subject ratings\nScale = [-200, 200]", fontsize=8)
plt.xlabel("USER LABEL", fontsize=15)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.title("Per Conditions Average Accross Subjects\n", fontsize=16)
plt.suptitle("\nIAPS Ratings", fontsize = 14.5 )
ax.boxplot(a_tot_ia, 0, '', meanprops=meanpointprops, showmeans = True )
ax.set_xticklabels(conditions, rotation=45, fontsize=8)
#plt.setp(xticklabels, rotation=45, fontsize=8)
plt.ylim( -200, 150 )
plt.ylabel("RATINGS",fontsize=15)
plt.show()

ax = plt.subplot(2,1,1)
plt.title("view_neutral, IAPS ratings\n", fontsize=16)
plt.suptitle("\n\nscale = [-200, 200]", fontsize=10)
plt.boxplot(arr_vneu1_ia, 0, '', meanprops=meanpointprops, showmeans = True )
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.ylim( -210, 100 )
plt.text(24, 60, 'Detach Session')
ax.yaxis.set_label_coords(-0.06, -0.060)
plt.ylabel("RATINGS",fontsize=15)
plt.subplot(2,1,2)
plt.boxplot(arr_vneu2_ia, 0, '', meanprops=meanpointprops, showmeans = True )
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.ylim( -210, 100 )
plt.text(24, 60, 'Permit Session')
plt.xlabel("USER LABEL", fontsize=15)
plt.show()

ax = plt.subplot(2,1,1)
plt.title("view_negative, IAPS ratings\n", fontsize=16)
plt.suptitle("\n\nscale = [-200, 200]", fontsize=10)
plt.ylim( -210, 210 )
plt.boxplot(arr_vneg1_ia, 0, '', meanprops=meanpointprops, showmeans = True )
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.ylim( -210, 210 )
plt.text(24, 140, 'Detach Session')
plt.ylabel("RATINGS", position=(-0.06, -0.06), fontsize=15)
#ax.yaxis.set_label_coords(-0.06, -0.060)
#plt.ylabel("RATINGS",fontsize=15)
plt.subplot(2,1,2)
plt.boxplot(arr_vneg2_ia, 0, '', meanprops=meanpointprops, showmeans = True )
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.ylim( -210, 210 )
plt.text(24, 140, 'Permit Session')
plt.xlabel("USER LABEL", fontsize=15)
plt.show()

ax = plt.subplot(2,1,1)
#ax.set_title("Detach_negative, IAPS ratings\nScale = [-200, 200]", fontsize=10)
plt.text(20,140, "Detach_negative, IAPS ratings\nScale = [-200, 200]", fontsize=10)
plt.boxplot(arr_detn_ia, 0, '', meanprops=meanpointprops, showmeans = True )
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.ylim( -210, 210 )
ax.yaxis.set_label_coords(-0.06, -0.060)
plt.ylabel("RATINGS",fontsize=15)
ax = plt.subplot(2,1,2)
plt.xlabel("USER LABEL", fontsize=15)
plt.boxplot(arr_pern_ia, 0, '', meanprops=meanpointprops, showmeans = True )
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.ylim( -210, 210 )
plt.text(20,-140, "Permit_negative, IAPS ratings\nScale = [-200, 200]", fontsize=10)
plt.show()

for i in range(1,31):
    axx.append ( i )
plt.title("PermitNeg - DetachNeg\n", fontsize=16)
plt.suptitle("\n\nDiff_of_Mean = Mean_of_Diff", fontsize=10)
plt.boxplot(arr_pmd, 0, '', meanprops=meanpointprops, showmeans = True )
plt.plot(axx, mamean)
plt.xlabel("USER LABEL", fontsize=15)
plt.ylabel("SUBJECT RATINGS DIFFERENCE",fontsize=13)
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.show()
#time.sleep(2)
