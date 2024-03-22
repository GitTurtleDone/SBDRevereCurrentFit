# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import pandas as pd
import matplotlib as matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from collections import defaultdict
from glob import glob
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import LogLocator
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from matplotlib import rcParams
import openpyxl as xl
from openpyxl import Workbook
from matplotlib import rc
import os
import re

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.ttk import *
from PIL import Image
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)
from mpl_toolkits.axes_grid.inset_locator import inset_axes
import matplotlib.gridspec as gridspec
import pickle




#----------turn ON this code when having problem of Times New Roman bold font----------
#del matplotlib.font_manager.weight_dict['roman']
#matplotlib.font_manager._rebuild()
#----------turn ON this code when having problem of Times New Roman bold font----------
#Set default Font globally
global glDefaultFont
glDefaultFont = "Times New Roman"
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = [glDefaultFont]
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.linewidth'] = 10

#----------turn ON this code when want to go back to the old Math text style  ----------

#plt.rcParams['mathtext.fontset'] = 'cm'

#----------turn ON this code when want to go back to old Math text style ----------
plt.rcParams['mathtext.rm'] = 'serif'
"""


plt.rcParams['axes.labelweight'] = 'heavy'

rc("font", weight = "bold")
rc('text',usetex = False)
"""

#Global Data Varaiable
global XYData,lXYData,rXYData,mXYData, glWbkData, singlecolor, arrcolor, clmaps,  lstGlLb
global fldGlParamConfig, dvGlParamConfig # fields and default values of Global Parameters
global fldPlotSetup, dvfldPlotSetup # fields and default values of a Plot Setup
global fldOneAxisConfig,dvOneAxisConfig # fields and default values of One Axis Config Dialog
global glFigSize, glFs, glBs, glOffset, glInsetFs, glInsetPos, glAxPos, glFrameWScrollbarSize, glSettings
global fldGlPar, dvGlPar
global fldGlFigLayout, dvGlFigLayout
global glFldExlData, glDvExlData
global glFigTypes
global glDctSubPlotSetup
global glAxConfig
global glTripleAxAdjust
global glTextFs
global glPlotStt
global glDataSource
global glIns
global glMarkerStyleNames, glMarkerStyles, glDctMarker, glLineStyles, glDrawStyles, glDctLineStyle
global glErrBarCapsize, glMarkerSize
global glDataFolder
global glLogMinorTickLimit
global glTextFileExtentions
#Constants
glFigSize = (200,150)
glFs = 25
glFw = 'bold'
glInsetFs = 20
glTextFs = 20
glBs = 10
glLogMinorTickLimit = 200
glOffset = 2000
glInsetPos = [0.2, 0.5, 0.3, 0.3]
glAxPos = [0,0,1,1]
glFrameWScrollbarSize = [500,400]
glIns = None
  

glWbkData = {}
glDataSource = {"Text Files": None, "Workbooks": glWbkData, "Data Folder": ""}
glDataFolder = ""

fldGlParamConfig =  'Font size', 'Log Base', 'Stack Offset','Inset Position', 'Inset Fontsize'
#dvGlParamConfig =  '20', str(glBs),'1000', r'[0.18, 0.55, 0.2, 0.4]','15'
dvGlParamConfig =  '20', str(glBs),'1000', str(glInsetPos),str(glInsetFs)

fldPlotSetup = 'Stack or Normal', 'X Scale', 'Y Scale', 'Line or Scatter', 'x Axis Title','y Axis Title'
dvfldPlotSetup =  'Normal', 'Lin','Lin','Line',r'2$\theta$ CuK$\alpha_1$ (deg)','y Axis Title'

glDctSubPlotSetup = {"comboboxes":{"fields":['Normal or Stack', 'X Scale', 'Y Scale', 'Line or Scatter'],
                                "default values":[['Normal','Stack'], ['Lin','Log'],['Lin','Log'],['Line','Scatter']]},                  
                  "entries":{"fields":['x Axis Title','y Axis Title'],
                             "default values":[r'2$\theta$ CuK$\alpha_1$ (deg)','y Axis Title']}}

glMarkerStyleNames = ["None","square", "cirle", "triangle_down", "triangle_up","triangle_left","triangle_right",
                     "star", "plus", "plus(field)","x", "x(filled)", #"Vertical line","Horizontal Line", Vertical and Horizontal Line are preserved for Error Bar
                     "pentagon", "hexagon1", "hexagon2","octagon", "diamond", "thin-diamond"]
glMarkerStyles = ["None","s","o","v","^","<",">",
                  "*","+","P","x","X",#"Vertical line","Horizontal Line", Vertical and Horizontal Line are preserved for Error Bar "|","_",
                  "p","h","H","8","D","d"]
glDctMarker ={"comboboxes":{"fields":["Style"], "default values":[glMarkerStyleNames]},
               "entries": {"fields": ["Size", "Face Color", "Edge Color", "Edge Width"],"default values":["15", "None", "Black", "2"]}}
"""
-----Old Line Styles---------------------
glLineStyles = ["-", "--", "-.", ":", ""]
glLineStyleNames= ["solid","dashed","dashdot","dotted","None"]
-----Old Line Styles---------------------
"""
glLineStyles = [(0, ()),"",(0, (1, 5)),(0, (5, 3)), (0, (5, 3, 1, 3)),(0, (5, 3, 1, 3, 1, 3)),(0, (1, 10)),(0, (1, 1)),(0, (5, 10)),(0, (3, 2)),
                (0, (3, 10, 1, 10)),(0, (3, 1, 1, 1)),(0, (3, 10, 1, 10, 1, 10)),(0, (3, 1, 1, 1, 1, 1))]
glLineStyleNames= ["solid","None","dotted","dashed","dashdot","dashdotdotted","loosely dotted","densely dotted","loosely dashed","densely dashed",
                   "loosely dashdotted","densely dashdotted","loosely dashdotdotted","densely dashdotdotted"]

glDrawStyles = ["default","steps","steps-pre","steps-mid","steps-post"]
glDctLineStyle = {"comboboxes":{"fields":["Line Style", "Draw Style"], "default values":[glLineStyleNames,glDrawStyles]},
               "entries": {"fields": ["Color", "Width"],"default values":["Black", "1"]}}


fldOneAxisConfig =  'Min', 'Max', 'Major Locator','Minor Locator', 'Axis Color'
dvOneAxisConfig =  '38', '42','1','0.2','Black'

glAxConfig = {"Axes Info" : [dvOneAxisConfig], 
              "Add Labels": [{"Add" : True, "Label Position":(0.1,0.9), "Text" : 'Data 1'}], 
              "Add Texts" : [{"Add" : True, "Text Position":(0.9,0.1), "Color" : 'black', "Text" : 'Data 1'}]}

glSettings = {'Global Parameters' : '1','Excel Data Info': '1','Plot Setup': '1','Plot Configure' : '1'}

fldGlFigLayout = 'Number of Rows', 'Number of Columns', 'Figure Size'

dvGlFigLayout = [1, 1, glFigSize]

glFldExlData = 'Workbooks', 'WorkSheet','X range', 'Y range', 'Z range'

glDvExlData = '','','A34:E4034', 'B34:F4034','E34:A4034'

glDctExlData = {"fields": glFldExlData, "default values": glDvExlData}

glFigTypes = ['Mono Axis', 'Double Axes', 'Double Axes with an Inset', 'Triple Axes']


fldGlPar = 'Figure Size', 'Font Size', 'Log Base', 'Stack Offset', 'Inset Position', 'Inset Fontsize',  'Frame with Scroll Bar Size'
dvGlPar = r'(240,180)', '20', '10', '2000',r'[0.18, 0.55, 0.2, 0.4]', '15', r'[500,400]' 

glPlotStt = {"Plot Type" : None,
             "Plot Data Source": glDataSource,
             "Plot Layout": None,
             "Plot Info" : None,
             "Plot Setup" : None,
             "Plot Config" : None,
             "Plot Figure": None,
             "Workbooks": None}
glErrBarCapsize = 5
glMarkerSize = 10

glTextFileExtentions = [".txt", ".TXT", ".csv", ".CSV", "dat", ".DAT"]
#prepare colors for the lines in the graph
singlecolor = ["black","red","green","blue","purple","grey","orange","springgreen","cyan","violet"]
arrcolor = ["Greys","Reds","Greens","Blues","Purples","Oranges"]
clmaps = defaultdict(list)
for k in range(6):
    clmaps[k] = plt.get_cmap(arrcolor[k])

def glPlotSttReset():
    global glPlotStt, glWbkData, glDataSource
    #glWbkData = {}
    glDataSource["Data Folder"] = ""
    glPlotStt = {"Plot Type" : None,
             "Plot Data Source": glDataSource,
             "Plot Layout": None,
             "Plot Info" : None,
             "Plot Setup" : None,
             "Plot Config" : None,
             "Plot Figure": None,
             "Workbooks": None}
    
#dvGlPar = r'(240,180)', '20', '10', '2000',r'[0.18, 0.55, 0.2, 0.4]', '15', r'[500,400]' 
#Generate a Default Figure  
def GnFg(size = glFigSize ):
    FgNm = plt.figure(tight_layout = True)
    FgNm.set_facecolor('white')
    FgNm.set_size_inches(mm2inch(size))
    return FgNm

def rmv_elts(main_lst, rmv_lst):
    tem_lst = []
    for j in rmv_lst:
        tem_lst.append(main_lst[j-1])
    for j in tem_lst:
        main_lst.pop(main_lst.index(j))
#convert from mm to inch subprogram        
def mm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch/10 for i in tupl[0])
    else:
        return tuple(i/inch/10 for i in tupl)
#convert a tuple: from inch to mm subprogram     
def inch2mm(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i*inch*10 for i in tupl[0])
    else:
        return tuple(i*inch*10  for i in tupl)

    
# convert a string to a tuple to add into the location of a legend
def StrToLctTup(s):
    lstDataLoc = ['best','upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center']
    if (len(s)<2 or s =='10'):
        if isNumber(s):
            return int(s)
        else:
            tk.messagebox.showwarning('Wrong Legend Location Entry','Please, enter the legend position again.')   
                          
    else:
        if s in lstDataLoc:
            return s
        else:
            try:
                s= re.sub('[(){}<>]', '', s)
                return tuple(float(item) for item in s.split(',') if item.strip())
            except ValueError:
                tk.messagebox.showwarning('Wrong Legend Location Entry','Please, enter the legend position again.') 
                
# convert a string to a tuple to add into the location of an inset figure
def StrToInsetLctTup(s):
    try:
        s= s.replace("[","").replace("]","")
        s= s.replace("(","").replace(")","")
        return list(float(item) for item in s.split(',') if item.strip("[]"))
    except ValueError:
        tk.messagebox.showwarning('Wrong Inset Graph Location Entry','Please, enter the Inset Graph Location again.') 

def RemoveLastChar(s,RemoveChar = "\n"):
    l = len(s)
    lastChar = s[l-1]
    while lastChar == RemoveChar:
        s = s[:(l-1)]
        lastChar = s[len(s)-1]
        l -= 1
        if l < 0:
            break
    return s   

    
#General axes set up
plt.rcParams['axes.linewidth'] = 1.75
def Setup(ax,fs = glFs):
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.label.set_weight("bold")
    ax.yaxis.label.set_weight("bold")
    ax.xaxis.label.set_size(fs)
    ax.yaxis.label.set_size(fs)
    ax.tick_params(which='major', direction = 'in', width=1.5, length=5)
    ax.tick_params(which='minor', direction = 'in', width=1, length=3.5)
    ax.tick_params(axis='both', which='major', labelsize=fs)
    ax.tick_params(axis='x', pad=5.5)
    ax.tick_params(axis='y', pad=5.5)

#Set up the log scale for Y axis
def setYLogScale(ax,axBase = glBs, axLogMinorTicklimit = glLogMinorTickLimit):
    
    axMin,axMax = ax.get_ylim()
    axMin = 10**np.floor(np.log10(axMin))
    axMax = 10**np.ceil(np.log10(axMax)) 
    ax.set_ylim(axMin,axMax)
    LogNumTicks = np.around((np.log10(axMax)-np.log10(axMin))/np.log10(axBase)+1) 
    ax.yaxis.set_major_locator(LogLocator(base = axBase, numticks=200)) 
    MinorTicks = np.arange(2,10)*10**(np.log10(axBase)-1)
    if LogNumTicks <= axLogMinorTicklimit:
        ax.yaxis.set_minor_locator(LogLocator(base = axBase, numticks=200,subs= MinorTicks))
    for label in ax.yaxis.get_minorticklabels():
        label.set_visible(False)
    #ax.tick_params(axis='y', which='minor')
#Set up the log scale for X axis
def setXLogScale(ax,axBase = glBs, axLogMinorTicklimit = glLogMinorTickLimit):
    axMin,axMax = ax.get_xlim()
    axMin = 10**np.floor(np.log10(axMin))
    axMax = 10**np.ceil(np.log10(axMax)) 
    ax.set_xlim(axMin,axMax)
    LogNumTicks = np.around((np.log10(axMax)-np.log10(axMin))/np.log10(axBase)+1) 
    ax.xaxis.set_major_locator(LogLocator(base = axBase, numticks=200)) 
    MinorTicks = np.arange(2,10)*10**(np.log10(axBase)-1)
    if LogNumTicks <= axLogMinorTicklimit:
        ax.xaxis.set_minor_locator(LogLocator(base = axBase, numticks=200,subs= MinorTicks))
    for label in ax.xaxis.get_minorticklabels():
        label.set_visible(False)
#Configure X axis with parameters such as Min, Max, Multiple Locator, Minor Locator, and color
def ConFigXScale(ax,Scale,tb = 'both'):
    try:
        ax.set_xlim(float(Scale[0]),float(Scale[1]))
    except ValueError:
        ax.set_ylim(ax.get_xlim()[0],ax.get_xlim()[1])
    if ax.get_xaxis().get_scale() == 'linear':
        ax.xaxis.set_major_locator(MultipleLocator(float(Scale[2])))
        ax.xaxis.set_minor_locator(MultipleLocator(float(Scale[3])))
    if tb == 'Top' or tb == 'top':
        ax.spines['top'].set_color(Scale[4])
    if tb == 'Bottom' or tb == 'bottom':
        ax.spines['bottom'].set_color(Scale[4])
    if tb == 'Both' or tb == 'both':
        ax.spines['top'].set_color(Scale[4])
        ax.spines['bottom'].set_color(Scale[4])
    
    ax.tick_params(axis='x', which = 'both', colors=Scale[4])
    ax.xaxis.label.set_color(Scale[4])
#Configure Y axis with parameters such as Min, Max, Multiple Locator, Minor Locator, and color
def ConFigYScale(ax,Scale,lr = 'both'):
    try:
        ax.set_ylim(float(Scale[0]),float(Scale[1]))
    except ValueError:
        ax.set_ylim(ax.get_ylim()[0],ax.get_ylim()[1])
    if ax.get_yaxis().get_scale() == 'linear':
        ax.yaxis.set_major_locator(MultipleLocator(float(Scale[2])))
        ax.yaxis.set_minor_locator(MultipleLocator(float(Scale[3])))
    if lr == 'left':
        ax.spines['left'].set_color(Scale[4])
    if lr == 'right':
        ax.spines['right'].set_color(Scale[4])
    if lr == 'Both' or lr == 'both':
        ax.spines['left'].set_color(Scale[4])
        ax.spines['right'].set_color(Scale[4])
    ax.tick_params(axis='y', which = 'both', colors=Scale[4])
    ax.yaxis.label.set_color(Scale[4])
#Configure XY axis with parameters such as Min, Max, Multiple Locator, Minor Locator, and color


        

    
# Check whether the string is blank or not
def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True
#Check whether a string line is a DataLine or not
def isDataLine(c):
    if not (any(c.isalpha() for c in c) or isBlank(c)):
        return True
    else:
        return False
#Check whether a string is a number or not
def isNumber(s):
    """ Returns True if string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False
#transpose a matrix
def mTr(m):    
    #return  np.array([m[j][i] for i in range(len(m[0])) for j in range(len(m))]).reshape(len(m[0]),len(m))    
    Temp = np.asarray(m)
    return Temp.T
#Match the row number if a certain value in a "lst" equals to a pre-defined "MatchValue" to a certain "Error"
def MatchRow(lst,MatchValue, Error = 0):
    k = 0
    if Error == 0:
        for k in range (len(lst)):
            if (lst[k] == MatchValue):
                return k
    else:
        for k in range (len(lst)):
            if np.abs(lst[k] - MatchValue) <= Error:
                return k
def LoadData(fname,SplitStr=" "):
    Temp = defaultdict(list)
    with open(fname) as f:
        lines = f.readlines()
        for line in lines: 
            if isDataLine(line):
                x = line.split(SplitStr)
                y = [float(value) for value in x if isNumber(value)] 
                Temp[0].append(y)
    Temp[0] = mTr(Temp[0])
    f.close() 
    return Temp[0]
def LoadFullData(fname,SplitStr=" "):
    Temp = defaultdict(list)
    with open(fname) as f:
        lines = f.readlines()
        for line in lines: 
            x = line.split(SplitStr)
            Temp[0].append(x)
    Temp[0] = mTr(Temp[0])
    f.close() 
    return Temp[0]

def Sv2DDt(FlNm,hd,lst):
    f = open(FlNm, "w")
    f.write(hd)
    for j in range(len(lst[0])):
        s = ""
        for k in range(len(lst)):
            s = s + "{:g}".format(lst[k][j]) + "\t"
        f.write(s+"\n")
    f.close() 

    
def TripleAxesScatter (xDt,y1Dt,y2Dt,y3Dt,xLb = "Concentration (M)",y1Lb = ["Growth Rate","Growth Rate (nm/min)"],y2Lb = ["(0006) Peak Position","(0006) Peak Position (deg)"],y3Lb = ["RC FWHM","Rocking Curve FWHM (deg)"],
                       xRg = [-0.01,0.11, 0.02,0.01], y1Rg = [0,12,2,0.4],y2Rg = [39.5,39.8, 0.1,0.02],y3Rg=[100,220,20,4],LbLocation = (0.03,0.4) ):
    fig, host = plt.subplots(tight_layout = True)
    fig.subplots_adjust(right=0.8)
    fig.set_facecolor('white')
    fig.set_size_inches(mm2inch(240, 180))
    
    ax1 = host.twinx()
    ax2 = host.twinx()
    #Setup(host)
    #Setup(ax1)
    #Setup(ax2)
    host.tick_params(axis='both', which='major', labelsize=15)
    ax1.tick_params(axis='both', which='major', labelsize=15)
    ax2.tick_params(axis='both', which='major', labelsize=15)
    
    ax2.spines["right"].set_position(("axes", 1.2))
    ax2.spines["right"].set_visible(True)
    
    line1, = host.plot(xDt,y1Dt,'s',markersize = 15,color= 'black',label=y1Lb[0])
    line2, = ax1.plot(xDt,y2Dt,'o',markersize = 15,color= 'red',label=y2Lb[0])
    line3, = ax2.plot(xDt,y3Dt,'^',markersize = 15,color= 'green',label=y3Lb[0])
    
    host.set_xlabel(xLb, fontsize = 20)
    host.set_ylabel(y1Lb[1], fontsize = 20)
    ax1.set_ylabel(y2Lb[1], fontsize = 20)
    ax2.set_ylabel(y3Lb[1], fontsize = 20)
    
    
    
    host.set_xlim(xRg[0],xRg[1])
    host.xaxis.set_major_locator(MultipleLocator(xRg[2]))
    host.xaxis.set_minor_locator(MultipleLocator(xRg[3]))
    host.set_ylim(y1Rg[0],y1Rg[1])
    host.yaxis.set_major_locator(MultipleLocator(y1Rg[2]))
    host.yaxis.set_minor_locator(MultipleLocator(y1Rg[3]))
    
    ax1.set_ylim(y2Rg[0],y2Rg[1])
    ax1.yaxis.set_major_locator(MultipleLocator(y2Rg[2]))
    ax1.yaxis.set_minor_locator(MultipleLocator(y2Rg[3]))
    ax2.set_ylim(y3Rg[0],y3Rg[1])
    ax2.yaxis.set_major_locator(MultipleLocator(y3Rg[2]))
    ax2.yaxis.set_minor_locator(MultipleLocator(y3Rg[3]))
    
    
    
    host.yaxis.label.set_color(line1.get_color())
    ax1.yaxis.label.set_color(line2.get_color())
    ax2.yaxis.label.set_color(line3.get_color())
    
    ax1.spines["right"].set_edgecolor(line2.get_color())
    ax2.spines["right"].set_edgecolor(line3.get_color())
    #ax1.tick_params.set_edgecolor(line2.get_color())
    #ax2.tick_params.set_edgecolor(line3.get_color())
    
    #tkw = dict(size=5, width=3)
    host.tick_params(axis='y', colors=line1.get_color())
    ax1.tick_params(axis='y', colors=line2.get_color(), which='both')
    ax2.tick_params(axis='y', colors=line3.get_color(), which='both')
    #host.tick_params(axis='x', **tkw)
    Setup(host)
    Setup(ax1)
    Setup(ax2)
    
    lines = [line1, line2, line3]
    
    host.legend(lines, [l.get_label() for l in lines],loc = LbLocation,fontsize = 18)
    return fig

def DoubleAxesScatter (ax):
    #Draw the left axis
    line1, = ax.plot(xDt,y1Dt, 's',markersize = 15,color= 'black')
    #Draw the right axis
    axr = ax.twinx()
    line2, = axr.plot(xDt,y2Dt, 'o',markersize = 15,color= 'red')
    
    ax.set_xlabel(xLb, fontsize = 20)
    ax.set_ylabel(y1Lb, fontsize = 20)
    axr.set_ylabel(y2Lb, fontsize = 20)
    
    Setup(ax)
    Setup(axr)
    
    axr.spines["right"].set_edgecolor(line2.get_color())
    axr.tick_params(axis='y', colors=line2.get_color(), which="both")
    axr.yaxis.label.set_color(line2.get_color())

def MonoAxis2(ax,data,dtConfig,xBase = glBs, yBase = glBs, *args,**kwargs):
    global singlecolor, arrcolor, clmaps, glOffset, glBs,glErrBarCapsize, glMarkerSize
    line = defaultdict(list)
    try:        
        if dtConfig[6] != None:
            try:
                if dtConfig[6][0] == True:
                    for i in range(len(dtConfig[6][1])):
                        if dtConfig[6][1][i][0] == "X":
                            xBase = int(dtConfig[6][1][i][1])
                        else:
                            yBase = int(dtConfig[6][1][i][1])
            except (TypeError, KeyError, IndexError, AttributeError):
                pass
                #tk.messagebox.showwarning('Base is not 1, 10, 100, etc','Please, refill Base entry') 
    except IndexError:
        pass
        #tk.messagebox.showwarning('Log Base frame has not been added to Setup','Please, do Config All, Save Data and Try Again')
    lnNum = len(data)
     #Draw the lines
    for j in range(lnNum):
        if j < 10 :
            lncolor = singlecolor[j]
        else: #just in case there are more than 10 lines in the graph
            lncolor = clmaps[np.remainder(j,5)](255-20*np.fmod(j,5))  
        Temp = np.asarray(data[j])
        
        #Temp[0] = data[j][1]
        #Temp[1] = data[j][1]
        if dtConfig[0] == 'Stack':
            if dtConfig[2] == 'Lin':
                Temp[1] = Temp[1]+glOffset*(lnNum-j-1)
                #Temp[1] == [Temp[1][m]+glOffset*(lnNum-j-1) for m in range(len(Temp[1]))]
            else:
                if dtConfig[2] =='Log' or dtConfig[2] == 'log':
                    fct = yBase**(lnNum-j-1)
                    Temp[1] = Temp[1] * fct + fct
                    ##if j == 0:
        
        ##   y_max = 10^np.ceil(np.log10(np.amax(np.asarray(Temp[1]))))
        if dtConfig[3] == 'Line' or dtConfig[3] == 'line':
            if (len(Temp)) < 3:
                line[j] = ax.plot(Temp[0],Temp[1],linestyle='-',linewidth=1.5,color= lncolor)  
            else:
                if (len(Temp[2]) != 0 and len(Temp[3]) != 0):
                    line[j] = ax.errorbar(Temp[0],Temp[1], xerr = Temp[2], yerr = Temp[3], capsize = glErrBarCapsize, linestyle='-', linewidth=2, color= lncolor)   
                else:
                    if len(Temp[2]) != 0:
                        line[j] = ax.errorbar(Temp[0],Temp[1], xerr = Temp[2], linestyle='-', capsize = glErrBarCapsize, linewidth=2, color= lncolor)    
                    else:
                        line[j] = ax.errorbar(Temp[0],Temp[1], yerr = Temp[3], linestyle='-', capsize = glErrBarCapsize, linewidth=2, color= lncolor)   
        else:
            if (len(Temp)) < 3:
                line[j] = ax.plot(Temp[0],Temp[1], 's',markersize = glMarkerSize, color= lncolor)     
            else:
                if (len(Temp[2]) != 0 and len(Temp[3]) != 0):
                    line[j] = ax.errorbar(Temp[0],Temp[1], xerr = Temp[2], yerr = Temp[3], capsize = glErrBarCapsize, marker = 's', markersize = glMarkerSize, color= lncolor)    
                else:
                    if len(Temp[2]) != 0:
                        line[j] = ax.errorbar(Temp[0],Temp[1], xerr = Temp[2], capsize = glErrBarCapsize, marker = 's', markersize = glMarkerSize, color= lncolor)
                    else:
                        line[j] = ax.errorbar(Temp[0],Temp[1], yerr = Temp[3], capsize = glErrBarCapsize, marker = 's', markersize = glMarkerSize, color= lncolor)                  
    if dtConfig[1] == 'Log' or dtConfig[1] == 'log':
        ax.set_xscale('log')
        setXLogScale(ax, axBase = xBase)
    if dtConfig[2] == 'Log' or dtConfig[2] == 'log':
        ax.set_yscale('log')
        setYLogScale(ax, axBase = yBase) 
    ax.set_xlabel(dtConfig[4], fontsize = glFs, fontweight = "bold")
    ax.set_ylabel(dtConfig[5], fontsize = glFs, fontweight = "bold")
    Setup(ax)
def MonoAxis(XYdata,dtConfig, fig = None, gs = None):
    if fig == None:
        #Generate a figure
        fig = GnFg()
    else:
        fig.show()
    if gs == None:
        #Generate a grid space
        gs = gridspec.GridSpec(1, 1)
    #Draw the left axis
    ax = fig.add_subplot(gs[0,0])
    MonoAxis2(ax,XYdata,dtConfig)
    Setup(ax)
    fig.show()
    return fig    
def DoubleAxes(lXYData,rXYData,ldtConfig,rdtConfig, fig = None, gs = None):
    if fig == None:
        #Generate a figure
        fig = GnFg()
    else:
        fig.show()
    if gs == None:
        #Generate a grid space
        gs = gridspec.GridSpec(1, 1)
    #Draw the left axis
    lAx = fig.add_subplot(gs[0,0])
    MonoAxis2(lAx,lXYData,ldtConfig)
    #Draw the right axis
    rAx = lAx.twinx()
    MonoAxis2(rAx,rXYData,rdtConfig)
    rAx.spines["right"].set_visible(True)
    rAx.spines["left"].set_visible(False)
    rAx.spines["top"].set_visible(False)
    rAx.spines["bottom"].set_visible(False)
    
    Setup(lAx)
    Setup(rAx)
    lAx.yaxis.set_ticks_position('left')
    rAx.yaxis.set_ticks_position('right')
    fig.show()
    #plt.show()
    return fig

def FigInset(mXYData,iXYData,mdtConfig,idtConfig, InsetPos = glInsetPos, InsetFs = glInsetFs, fig = None, gs = None):
    if fig == None:
        #Generate a figure
        fig = GnFg()
    else:
        fig.show()
    if gs == None:
         #Generate a grid space
        gs = gridspec.GridSpec(1,1)
    #Draw the main axis
    mAx = fig.add_subplot(gs[0,0])
    MonoAxis2(mAx,mXYData,mdtConfig)
    
    
    bxPos = mAx.get_position().get_points()
    
    NewInsetPos = setSubPlotNewAxPos(bxPos,InsetPos)
    iAx = fig.add_axes(NewInsetPos)         
    MonoAxis2(iAx,iXYData,idtConfig)
    
    
    Setup(mAx)
    Setup(iAx,fs = InsetFs)
    return fig
def getRnC(pos):
    q,r = divmod(pos[2],pos[0])
    if r == 0:
        return [q-1,r]
    else:
        return [q,r-1]
def setSubPlotNewAxPos(sbPos,AxPos):
    return [sbPos[0][0]+(sbPos[1][0]-sbPos[0][0])*AxPos[0],
            sbPos[0][1]+(sbPos[1][1]-sbPos[0][1])*AxPos[1],
            (sbPos[1][0]-sbPos[0][0])*AxPos[2],
            (sbPos[1][1]-sbPos[0][1])*AxPos[3]]
glTripleAxAdjust = [0.85,1.15] 
def TripleAxes(lXYData,mXYData,rXYData,ldtConfig,mdtConfig,rdtConfig,axAdjust = glTripleAxAdjust, fig = None, gs = None):
    if fig == None:
        #Generate a figure
        fig = GnFg()
    else:
        fig.show()
    if gs == None:
        #Generate a grid space
        gs = gridspec.GridSpec(1, 1)
    
    #Draw the left axis
    lAx = fig.add_subplot(gs[0,0])
    MonoAxis2(lAx,lXYData,ldtConfig)
    #Draw the middle axis
   
    
    fig.subplots_adjust(right = axAdjust[0])
    mAx = lAx.twinx()
    MonoAxis2(mAx,mXYData,mdtConfig)
    #mAx.spines["right"].set_visible(True)
    #mAx.spines["left"].set_visible(False)
    for ln in mAx.lines:
        ln.set_color("red")
        ln.set_marker("o")
    #Draw the right axis
    rAx = lAx.twinx()
    rAx.spines["right"].set_position(("axes", axAdjust[1]))
    MonoAxis2(rAx,rXYData,rdtConfig)	
    for ln in rAx.lines:
        ln.set_color("green")
        ln.set_marker("^")
    
    Setup(lAx)
    Setup(mAx)
    Setup(rAx)
    
    mAx.spines["right"].set_visible(True)
    mAx.spines["left"].set_visible(False)
    mAx.spines["top"].set_visible(False)
    mAx.spines["bottom"].set_visible(False)
    
    rAx.spines["right"].set_visible(True)
    rAx.spines["left"].set_visible(False)
    rAx.spines["top"].set_visible(False)
    rAx.spines["bottom"].set_visible(False)
    
    lAx.yaxis.set_ticks_position('left')
    mAx.yaxis.set_ticks_position('right')
    rAx.yaxis.set_ticks_position('right')
    
    #plt.show()
    return fig

def WriteToSheet(mySheet,lst,StartCell = (1,1)):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            mySheet.cell(row = i+StartCell[0], column = j+StartCell[1]).value = lst[i][j]

def GetRange (MyRange):
    
    """ Don't delete this
    Temp = [[0 for j in range(len(MyRange[0])) ] for i in range(len(MyRange))]
    for i in range(len(MyRange)):
        for j in range(len(MyRange[0])):
            Temp[i][j] = MyRange[i][j].value
    """
    Temp = []
    for i in range(len(MyRange)):
        for j in range(len(MyRange[i])):
            Temp.append(MyRange[i][j].value)
    
    return Temp

#-----------------------------------------------GUIs------------------------------------------------------------------ 
##-----------------------------------------------general GUIs -----------------------------------------------------------
###-----------------------------------------------general GUI classes -----------------------------------------------------
        
class clsOneAxisDataLbDlg(tk.Frame): # A class to handle label of the graphs
    def __init__(self,parent,frTxt,lstLb, lbInfo = None, *args, **kwargs):
        tk.Frame.__init__(self,parent, *args, **kwargs)   
        self.Title = ttk.Label(self,text=frTxt, anchor='w')
        self.Title.grid(row = 0, column = 0, columnspan=2, padx = 5, pady = 5)
        self.lbLgdLoc = ttk.Label(self,text='Label Location:')
        self.lbLgdLoc.grid(row = 2, column = 0, sticky = 'W')
        
        self.entLgdLoc = ttk.Entry(self)
        self.entLgdLoc.grid(row = 2, column = 1)
        try:
            self.entLgdLoc.insert(0,lbInfo[1][1])
        except TypeError:
            self.entLgdLoc.insert(0,'0')
        

        self.lbLgdTxtFs = ttk.Label(self,text='Label Font Size:')
        self.lbLgdTxtFs.grid(row = 3, column = 0, sticky = 'W')
        
        self.entLgdTxtFs = ttk.Entry(self)
        self.entLgdTxtFs.grid(row = 3, column = 1)
        try:
            self.entLgdTxtFs.insert(0,lbInfo[1][2])
        except TypeError:
            self.entLgdTxtFs.insert(0,str(glTextFs))
        
        try:
            self.lstLb = lbInfo[1][0]
        except TypeError:
            self.lstLb = None
         
        self.scbH = ttk.Scrollbar(self, orient=HORIZONTAL)
        self.scbH.grid(row = 1, column = 0,columnspan=2, padx = 5, pady = 5, sticky = 'WE')
        
        self.scbV = ttk.Scrollbar(self)
        self.scbV.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = 'NS')

        self.tbx = tk.Text(self, wrap = NONE, width = 10, height = 10, xscrollcommand=self.scbH.set,yscrollcommand=self.scbV.set)
        self.tbx.grid(row = 0, column = 0,columnspan=2, padx = 5, pady = 5, sticky = 'WE')
        if self.lstLb != None:
            self.UpdLb()
        self.scbH.config(command=self.tbx.xview)
        self.scbV.config(command=self.tbx.yview)
        self.lgdIf = []
   
    def UpdLb(self): # to update the box with the list of labels
        self.tbx.delete(1.0,END)
        if self.lstLb != None:
            for x in self.lstLb: 
                self.tbx.insert(END,x+'\n')
    def get(self):
        lstTemp = []
        for i in range(int(self.tbx.index('end').split('.')[0]) - 1):
            tstart = str(i+1)+'.0'
            tstop = str(i+1)+'.end'
            s = self.tbx.get(tstart,tstop)
            if s != "":
                lstTemp.append(self.tbx.get(tstart,tstop)) 
        return lstTemp
    def getLgdIf(self,*args, **kwargs):
        self.lgdIf = [#self.chbIncludeLbVar.get(),
                       self.get(),
                       self.entLgdLoc.get(),
                       self.entLgdTxtFs.get()]
        return self.lgdIf
    

class clsDataEntDlg(ttk.Frame): 
    def __init__(self,parent,frTxt,fields,DefaultVal, *args, **kwargs):
        self.fields = fields
        self.DefaultVal =  DefaultVal
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        self.Title = ttk.Label(self,text=frTxt)
        self.Title.grid(row = 1, column = 0, sticky = 'nw')
        self.ents = clsMakeForm(self,self.fields)
        self.ents.grid(row = 1, column = 0, sticky = 'nw')
        InsertVal(self.ents.entries,self.DefaultVal)    
    #Get all values in the entries for plot configuration    
    def getAxConfig(self):
        Temp = [] 
        for field in self.fields:
            Temp.append(self.ents.entries[field].get())
        return Temp

class clsOneAxisConfigDlg(clsDataEntDlg):
    global fldOneAxisConfig,dvOneAxisConfig 
    def __init__(self,parent,frTxt, axInfo = dvOneAxisConfig, *args, **kwargs):
        clsDataEntDlg.__init__(self,parent,frTxt,fldOneAxisConfig,axInfo,*args, **kwargs)
        
class clsAddLabelDlg(ttk.Frame):
    def __init__(self,parent,YAx, lbInfo = None, *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        #self.Title = ttk.Label(self,text=frTx, sticky='w')
        #self.Title.grid(row = 0, column = 1)
        self.YAxNum = len(YAx)
        self.YAx = YAx
        self.tbxLstLb = []
        self.lstLb = []
        self.lstLbLct = []
        self.chbAddLbVar = tk.IntVar(master = parent)
        self.chbAddLb = ttk.Checkbutton(self,text = 'Add Line Labels',variable = self.chbAddLbVar, command = lambda: self.AddTbx())
        self.chbAddLb.grid(row=0,column=0, columnspan = self.YAxNum, sticky = 'W')
        if lbInfo != None:
            self.Info = lbInfo
            self.chbAddLbVar.set(lbInfo[0])
            if self.chbAddLbVar.get() == 1:
                self.AddTbx()
        else:
            self.Info = None
    def AddTbx(self):
        if self.chbAddLbVar.get() == 1:
            for i in range(self.YAxNum):
                self.tbxLstLb.append(clsOneAxisDataLbDlg(self,self.YAx[i],[], lbInfo = self.Info))
                self.tbxLstLb[i].grid(row = 1, column = i, sticky = 'w', padx=5, pady=5)
                self.tbxLstLb[i].lstLb = []
            self.btnGetLb = ttk.Button(self, text = 'Get Labels', command = lambda : self.GetLabels)
            self.btnGetLb.grid(row = 2, column = 0, padx=5, pady=5, sticky = 'w')
        else:
            self.lstLb = []
            self.lstLbLct = []
            if self.tbxLstLb != None:
                for tbx in self.tbxLstLb:
                    tbx.destroy()
            self.btnGetLb.destroy()
            self.tbxLstLb = []
            
    def GetLabels(self):
        tempLstLb = []
        tempLstLbLct = []
        for tbx in self.tbxLstLb:
            tempLstLb.append(tbx.get())
            tempLstLbLct.append(tbx.entLgdLoc.get())
        self.lstLb = tempLstLb
        self.lstLbLct = tempLstLbLct
    def UpdateTextBoxes(self):
        i = 0
        for tbx in self.tbxLstLb:
            tbx.lstLb =self.lstLb[i]
            tbx.UpdLb()
            i += 1
    def get(self, *args, **kwargs):
        self.Info = [self.chbAddLbVar.get(), self.tbxLstLb[0].getLgdIf()]
        
        return self.Info
        
class clsFrameWScrollBar(tk.Frame):
    def __init__(self,parent,frSize,AddScbH = True, AddScbV = True, *args, **kwargs):
        #Create a storing Frame
        self.Size = frSize
        tk.Frame.__init__(self,parent,width = frSize[0], height = frSize[1], *args, **kwargs)
        #Create a canvas inside the storing frame
        self.canvas = tk.Canvas(self, 
                                #background = 'White', 
                                width = frSize[0]-30, height = frSize[1]-30)
        self.canvas.grid(row=0, column = 0, sticky = 'WENS')
        #Create a horizontal scroll bar
        if AddScbH:
            self.scbH = ttk.Scrollbar(self, orient=HORIZONTAL)
            self.scbH.grid(row = 1, column = 0,sticky = 'WE')
            #Conect the canvas with the horizontal  scroll bar
            self.canvas.config(xscrollcommand=self.scbH.set)
            self.scbH.config(command=self.canvas.xview)
        #Create a vertical scroll bar
        if AddScbV:
            self.scbV = ttk.Scrollbar(self)
            self.scbV.grid(row = 0, column = 1, sticky = 'NS')
            #Conect the canvas with the vertical scroll bar
            self.canvas.config(yscrollcommand=self.scbV.set)
            self.scbV.config(command=self.canvas.yview)
        #create a frame inside the canvas
        self.frame=ttk.Frame(self.canvas,width = self.canvas.winfo_width(), height = self.canvas.winfo_height())
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        # binding  the function Configure of the frame with the Canvas - Not sure what is it for?
        def cnvConfig(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=self.Size[0]-30,height=self.Size[1]-30)
        self.frame.bind("<Configure>",cnvConfig)
    
class clsPlotOneAxisDlg(clsDataEntDlg):
    global fldPlotSetup, dvfldPlotSetup
    def __init__(self,parent,frTxt, *args, **kwargs):
        clsDataEntDlg.__init__(self,parent,frTxt,fldPlotSetup,dvfldPlotSetup,*args, **kwargs)

###-----------------------------------------------general GUI classes -----------------------------------------------------
###-----------------------------------------------general GUI function -----------------------------------------------------
class clsMakeForm(ttk.Frame):
    def __init__(self,parent,fields, *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        self.entries = {}
        i = 0
        for field in fields:
            lab = ttk.Label(self, text=field+": ")
            ent = ttk.Entry(self)
            ent.insert(0,"")
            lab.grid(row = i, column = 0, padx = 5, pady = 5, sticky = 'nw')
            ent.grid(row = i, column = 1, padx = 5, pady = 5, sticky = 'nw')
            i +=1
            self.entries[field] = ent              
def InsertVal(entries,DefaultValues):
    i = 0
    for entry in entries:
      entries[entry].insert(0,DefaultValues[i])
      i +=1

class clsMakeFrame(ttk.Frame):
    def __init__(self,parent,dctWidgets,cbbSetDftlVal = True, *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        self.comboboxes = {}
        self.entries = {}
        self.buttons = {}
        self.listboxes = {}
        self.If = []
        i = 0
        for wdg in dctWidgets.keys():
            if wdg == "comboboxes":
                k = 0
                for field in dctWidgets[wdg]["fields"]:
                    lab = ttk.Label(self, text=field+": ")
                    cbb = ttk.Combobox(self)
                    cbb['values'] = dctWidgets[wdg]["default values"][k]
                    if cbbSetDftlVal == True:
                        cbb.set(cbb['values'][0])
                    lab.grid(row = i, column = 0, padx = 5, pady = 5, sticky = 'nw')
                    cbb.grid(row = i, column = 1, padx = 5, pady = 5, sticky = 'nw')
                    self.comboboxes[field] = cbb
                    k +=1
                    i +=1
            if wdg == "entries":
                k = 0
                for field in dctWidgets[wdg]["fields"]:
                    lab = ttk.Label(self, text=field+": ")
                    ent = ttk.Entry(self)
                    ent.insert(0,dctWidgets[wdg]["default values"][k])
                    lab.grid(row = i, column = 0, padx = 5, pady = 5, sticky = 'nw')
                    ent.grid(row = i, column = 1, padx = 5, pady = 5, sticky = 'nw')
                    self.entries[field] = ent
                    k +=1
                    i +=1
            if wdg == "buttons":
                k = 0
                btnNum = []
                for field in dctWidgets[wdg]["fields"]:
                    btnNum.append(k)
                    btn = ttk.Button(self, 
                                     text=field)
                    btn.grid(row = i, column = k, padx = 5, pady = 5, sticky = 'nw')
                    btn.bind("<Button-1>",lambda x=self: dctWidgets[wdg]["default values"][k](self))
                    k +=1
                    i +=1
            if wdg == "listboxes":
                k = 0
                for field in dctWidgets[wdg]["fields"]:
                    lab = ttk.Label(self, text=field+": ")
                    lstb = tk.Listbox(self)
                    for item in dctWidgets[wdg]["default values"][k]:
                        lstb.insert(END,item)
                    lab.grid(row = i, column = 0, padx = 5, pady = 5, sticky = 'nw')
                    lstb.grid(row = i, column = 1, padx = 5, pady = 5, sticky = 'nw')
                    self.listboxes[field] = lstb
                    k +=1
                    i +=1
    def setInfo(self,*args,**kwargs):
        
        if self.If != None:
            i = 0
            try:
                for cbb in list(self.comboboxes.values()):
                    cbb.set(str(self.If[i]))
                    i += 1
            except (IndexError,TypeError,ValueError) as e:
                i +=1
            try: 
                for ent in list(self.entries.values()):
                    ent.delete(0,'end')
                    ent.insert(0,str(self.If[i]))
                    i += 1
            except (IndexError,TypeError,ValueError) as e:
                i +=1 
    def get(self,*args,**kwargs):
        self.If = []
        try:
            for cbb in list(self.comboboxes.values()):
                self.If.append(cbb.get())
        except TypeError:
            pass
        try: 
            for ent in list(self.entries.values()):
                self.If.append(ent.get())
        except TypeError:
            pass
        return self.If
        
###-----------------------------------------------general GUI function -----------------------------------------------------
##-----------------------------------------------general GUIs----------------------------------------------------------- 


##-----------------------------------------------Excel GUIs------------------------------------------------------------- 
###-----------------------------------------------Excel GUIs classes----------------------------------------------------
# a Load Work Book class to load multiple excel wook books and 

class clsLoadWorkBook(tk.Frame):
    
    def opnFl(self, frNum,*args, **kwargs):
        FileName = filedialog.askopenfilename(defaultextension = ".xlsx",
                                            filetypes=[('Excel File', "*.xlsx"),
                                                       ('Python Plot GUI file','*.pypGUI'), 
                                                       ('Data File', "*.DAT"),
                                                       ('Text File', "*.txt"),
                                                       ('All files','*.*')],
                                            parent = self,
                                            title = "Load Excel Data")
        self.CmnFlNameEntLst[frNum-1].delete(0,'end')
        self.CmnFlNameEntLst[frNum-1].insert(0,os.path.basename(FileName))
        try:
            self.txtFldName = FileName.replace(os.path.basename(FileName),"")
        finally:
            pass
    def LoadData(self, *args, **kwargs):
        for i in range(len(self.CmnFlNameEntLst)):
            CmnFlName = self.CmnFlNameEntLst[i].get()
            SltStr = self.txtFldName+'*'+CmnFlName+'*'
            FileNames = glob(SltStr)
            for FileName in FileNames:            
                wb = xl.load_workbook(FileName, data_only=True)
                self.AllWbks.update({os.path.basename(FileName): wb})
            global glDataFolder
            glDataFolder = self.txtFldName
        global glDataSource, glWbkData, glPlotStt 
        glWbkData = self.AllWbks
        glDataSource["Workbooks"] = glWbkData
        glDataSource["Data Folder"] = glDataFolder
        glPlotStt["Plot Data Source"] = glDataSource
        
            
    def __init__(self,parent, *args, **kwargs):
        #global glPlotStt
        #glPlotSttReset()
        self.AllWbks = {}
        tk.Frame.__init__(self,parent, *args, **kwargs)
        self.frOperBtns = ttk.Frame(self)
        self.frOperBtns.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.btnLdDt = ttk.Button(self.frOperBtns,text = 'Load Data', command = self.LoadData)
        self.btnLdDt.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.btnAddFrame = ttk.Button(self.frOperBtns, text = "+", width = 3, command = lambda: self.AddFrame())
        self.btnAddFrame.grid(row=0,column=1, padx = 5, pady = 5, sticky = 'nw')
        self.btnRemoveFrame = ttk.Button(self.frOperBtns, text = "-", width = 3, command = lambda: self.RemoveFrame())
        self.btnRemoveFrame.grid(row=0,column=2, padx = 5, pady = 5, sticky = 'nw')
        #self.btnOK = ttk.Button (self.frOperBtns,text = 'OK', command = parent.destroy)
        self.btnOK = ttk.Button (self.frOperBtns,text = 'OK', command = lambda: self.CloseProc(parent))
        self.btnOK.grid(row=0, column=3, padx = 5, pady = 5, sticky = 'nw')
        self.txtFldName = "" #Folder contains the workbooks
        self.frLst = [] 
        self.CmnFlNameEntLst = []
        self.frNum = 0
        self.AddFrame()
    def CloseProc(self,parent, *args, **kwargs):
        global glWbkData
        glWbkData = self.AllWbks
        glPlotSttReset()
        parent.destroy()
    def AddFrame(self,*args, **kwargs):
        self.frNum += 1
        fr = ttk.Frame(self)
        fr.grid(row=self.frNum,column=0, padx = 5, pady = 5, sticky = 'nw')
        lb=ttk.Label(fr,text = "Common File Name")
        lb.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        ent = ttk.Entry(fr)
        ent.grid(row=0,column=1, padx = 5, pady = 5, sticky = 'nw')
        ent.insert(0,"")
        btn = ttk.Button(fr,text = "Browse",command = lambda m = self.frNum: self.opnFl(m))
        btn.grid(row=0,column=2, padx = 5, pady = 5, sticky = 'nw') 
        self.CmnFlNameEntLst.append(ent)
        self.frLst.append(fr)       
             
    def RemoveFrame(self, *args, **kwargs):
        if self.frNum > 1:
            self.frNum -= 1
            self.frLst[self.frNum].destroy()
            self.frLst = self.frLst[:self.frNum]
class clsExlPlotDlg(ttk.Frame):
    def __init__(self,parent,wbks,YAx,XSeparate = False, *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        YAxNum = len(YAx)
        # Create a tab Control
        self.tabControl = ttk.Notebook(parent)          
        
        
        # Create a tab to store necessary data
        self.frAx = []
        self.tbAx = []
        
        for i in range(YAxNum):
            self.tbAx.append(ttk.Frame(self.tabControl))            
            self.tabControl.add(self.tbAx[i], text=YAx[i])
            self.frAx.append(clsOneAxisExlDataTbDlg(self.tbAx[i],wbks))
            self.frAx[i].grid(row = 0,column = 0, padx = 5, pady = 5, sticky = 'nw')
        # Create a tab to store initial Plot Configuration
        self.tbPl = ttk.Frame(self.tabControl)            
        self.tabControl.add(self.tbPl, text='Plot Setup')
        self.tabControl.pack(expand=1, fill="both")
        self.frAxPl = []
        for i in range(YAxNum):
            self.frAxPl.append(clsPlotOneAxisDlg(self.tbPl,'Initial '+YAx[i]))
            self.frAxPl[i].grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
            self.frAxPl[i].ents.entries['y Axis Title'].delete(0,'end')
            self.frAxPl[i].ents.entries['y Axis Title'].insert(0,YAx[i])
        
        self.btnPl = ttk.Button(self.tbPl, text='Plot',command=(lambda : self.PlotData()))
        self.btnPl.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        
        # Create a tab to store further details Plot Configuration
        self.tbAxConfig = ttk.Frame(self.tabControl)            
        self.tabControl.add(self.tbAxConfig, text='Axis Configuration')
        self.tabControl.pack(expand=1, fill="both")
        
        #A frame storing all parameters of all axes
        self.frAxParams = ttk.Frame(self.tbAxConfig)
        if XSeparate:
            
            self.XAxConfig = []
            self.YAxConfig = []
            self.frAxParams.grid(row = 0, column = 0,columnspan = 2 * YAxNum, padx = 5, pady = 5, sticky = 'nw')
            
            for i in range(YAxNum):
                self.XAxConfig.append(clsOneAxisConfigDlg(self.frAxParams,YAx[i].replace('Y ','X ')))
                self.XAxConfig[i].grid(row = 0, column = i*2, padx=5, pady=5, sticky = 'nw')
                self.YAxConfig.append(clsOneAxisConfigDlg(self.frAxParams,YAx[i]))
                self.YAxConfig[i].grid(row = 0, column = 1+i*2, padx=5, pady=5, sticky = 'nw')
        else:
            self.XAxConfig = []
            self.YAxConfig = []
            self.frAxParams.grid(row = 0, column = 0,columnspan = 1 + YAxNum)
            self.XAxConfig.append(clsOneAxisConfigDlg(self.frAxParams,'X Axis Configuration'))
            self.XAxConfig[0].grid(row = 0, column = 0, padx=5, pady=5, sticky = 'nw')
            for i in range(YAxNum):
                self.YAxConfig.append(clsOneAxisConfigDlg(self.frAxParams,YAx[i]))
                self.YAxConfig[i].grid(row = 0, column = 1+i, padx=5, pady=5, sticky = 'nw')
        
        # A frame storing all operating buttons
        self.frOperBtns = ttk.Frame(self.tbAxConfig)
        self.frOperBtns.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        self.btnConfig = ttk.Button(self.frOperBtns, text='Configure',command=lambda : self.ConFigAxes())
        self.btnConfig.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        self.btnPpl = ttk.Button(self.frOperBtns, text='Poputlate Label Text Boxes',command=lambda : self.populate())
        self.btnPpl.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'nw')
        
        # A frame storing an Add Text frame
        self.frAddTxt = ttk.Frame(self.tbAxConfig)
        self.frAddTxt.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.frAddTxtDlg = clsAddTxtDlg(self.frAddTxt)
        self.frAddTxtDlg.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing line label frames
        self.frLnLbs = ttk.Frame(self.tbAxConfig)
        self.frLnLbs.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        self.frAddLbDlg = clsAddLabelDlg(self.frLnLbs,YAx)
        self.frAddLbDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 

    def populate(self):
        if self.frAddLbDlg.chbAddLbVar.get() == 1:
            self.frAddLbDlg.lstLb = []
            for fr in self.frAx:
                self.frAddLbDlg.lstLb.append(fr.lstLb)
            self.frAddLbDlg.UpdateTextBoxes()
    def ConFigAxes(self):
        a = 1
       
    def PlotData(self):
        a = 1

global dctAddTxtDlg 
dctAddTxtDlg = {"fields" : ["Text","Location","Font Size", "Color"], "default values": ["(a)","[0.1,0.1]","40", "black"]}
class clsBasicAddTxtDlg(ttk.Frame):
    global dctAddTxtDlg
    def __init__(self,parent,txtLb, txtInfo = None, *args, **kwargs):
        ttk.Frame.__init__(self,parent,*args, **kwargs)
        self.lbTxt = ttk.Label(self,text=dctAddTxtDlg["fields"][0] + " " + txtLb)
        self.lbTxt.grid(row = 0, column = 0, padx = 5, pady = 5,sticky = 'w')
        self.tbxTxt = tk.Text(self, width = 15, height = 4)
        self.tbxTxt.grid(row = 1, column = 0, rowspan = 2, padx = 5, pady = 5,sticky = 'w')
        try:
            self.tbxTxt.insert("1.0",txtInfo[0])
        except TypeError: 
            self.tbxTxt.insert("1.0",dctAddTxtDlg["default values"][0])
        
        self.lbTxtLoc = ttk.Label(self,text=dctAddTxtDlg["fields"][1], width = 10)
        self.lbTxtLoc.grid(row = 0, column = 1, padx = 5, pady = 5,sticky = 'w')
        self.entTxtLoc = ttk.Entry(self, width = 10)
        self.entTxtLoc.grid(row = 0, column = 2, padx = 5, pady = 5,sticky = 'w')
        try:
            self.entTxtLoc.insert(0,str(txtInfo[1]))      
        except TypeError: 
            self.entTxtLoc.insert(0,dctAddTxtDlg["default values"][1])
        
        self.lbTxtFs = ttk.Label(self,text=dctAddTxtDlg["fields"][2], width = 10)
        self.lbTxtFs.grid(row = 1, column = 1, padx = 5, pady = 5,sticky = 'w')
        self.entTxtFs = ttk.Entry(self, width = 10)
        self.entTxtFs.grid(row = 1, column = 2, padx = 5, pady = 5,sticky = 'w')
        try:
            self.entTxtFs.insert(0,str(txtInfo[2]))      
        except TypeError: 
            self.entTxtFs.insert(0,dctAddTxtDlg["default values"][2])
        
        
        self.lbTxtCl = ttk.Label(self,text=dctAddTxtDlg["fields"][3], width = 10)
        self.lbTxtCl.grid(row = 2, column = 1, padx = 5, pady = 5,sticky = 'w')
        self.entTxtCl = ttk.Entry(self, width = 10)
        self.entTxtCl.grid(row = 2, column = 2, padx = 5, pady = 5,sticky = 'w')
        try:
            self.entTxtCl.insert(0,txtInfo[3])      
        except TypeError:
            self.entTxtCl.insert(0,dctAddTxtDlg["default values"][3])
    
        
class clsAddTxtDlg(ttk.Frame):
    def __init__(self,parent,txtInfo = None, *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        self.frAddTxtSz = [500,150]
        self.TxtDlgNum = 0
        self.chbAddTxtVar = tk.IntVar(master = parent)
        self.chbAddTxt = ttk.Checkbutton(self,text = 'Add Text',variable = self.chbAddTxtVar, command = lambda: self.AddTbx())
        self.chbAddTxt.grid(row=0,column=0, columnspan = 2, sticky = 'W')
        self.lstTxtDlg = []
        self.lstTxt = []
        self.lstTxtLoc = []
        self.lstTxtFs = []
        self.lstTxtCl = []
        self.txtIf = txtInfo
        try:
            self.chbAddTxtVar.set(self.txtIf[0])
            if self.chbAddTxtVar.get() == 1:
                self.AddTbx()    
        except TypeError:
            self.chbAddTxtVar.set(0)       
    def AddTbx(self):
        if self.chbAddTxtVar.get() == 1:
            self.frScb =clsFrameWScrollBar(self,self.frAddTxtSz)
            self.frScb.grid(row = 1, column = 0)
            try:
                self.TxtDlgNum = len(self.txtIf[1])
            except TypeError:
                self.TxtDlgNum +=1
            for i in range(self.TxtDlgNum):
                try:
                    self.lstTxtDlg.append(clsBasicAddTxtDlg(self.frScb.frame,str(i), self.txtIf[1][i]))
                except TypeError:
                    self.lstTxtDlg.append(clsBasicAddTxtDlg(self.frScb.frame,str(i)))
                self.lstTxtDlg[i].grid(row = i, column = 0, sticky = 'w')
                i +=1
            self.btnAdd = ttk.Button(self.frScb.frame,text = 'Add', width = 5,command = lambda: AddBasicAddTxtDlg(self))
            self.btnAdd.grid(row = 0, column = 1, padx = 5, pady = 5,sticky = 'nw')
            def AddBasicAddTxtDlg(self):
                self.TxtDlgNum +=1
                txtLb = str(self.TxtDlgNum)
                self.lstTxtDlg.append(clsBasicAddTxtDlg(self.frScb.frame,txtLb))
                self.lstTxtDlg[self.TxtDlgNum-1].grid(row = self.TxtDlgNum, column = 0, sticky = 'w')        
        else:
            self.lstTxt = []
            self.lstTxtLoc = []
            self.lstTxtDlg = []
            self.lstTxtFs = []
            self.lstTxtCl = []
            self.TxtDlgNum = 0
            self.frScb.destroy()
    def GetTxtDlg(self):
        self.lstTxt = []
        self.lstTxtLoc = []
        self.lstTxtFs = []
        self.lstTxtCl = []
        for TxtDlg in self.lstTxtDlg:           
            self.lstTxt.append(RemoveLastChar(TxtDlg.tbxTxt.get("1.0",END)))
            self.lstTxtLoc.append(TxtDlg.entTxtLoc.get())
            self.lstTxtFs.append(TxtDlg.entTxtFs.get())
            self.lstTxtCl.append(TxtDlg.entTxtCl.get())
        return (self.lstTxt,self.lstTxtLoc,self.lstTxtFs,self.lstTxtCl)
    def getTxtIf(self, *args, **kwargs):
        self.GetTxtDlg()
        self.txtIf = [self.chbAddTxtVar.get(),
		      [[self.lstTxt[i],self.lstTxtLoc[i],self.lstTxtFs[i],self.lstTxtCl[i]] 
		      for i in range(len(self.lstTxt))]]
        return self.txtIf
            
         
class clsInsetExlPlotDlg(clsExlPlotDlg):
    def __init__(self,parent,wbks,YAx, *args, **kwargs):
        clsExlPlotDlg.__init__(self,parent,wbks,YAx,True, *args, **kwargs) 
        global glInsetPos
        # A frame to store the Inset Postion Dialog
        self.frInsetPos = ttk.Frame(self.tbAxConfig)
        self.frInsetPos.grid(row = 4, column = 0, sticky = 'w')
        self.InsetPosDlg = clsAddAxPosDlg(self.frInsetPos, frTxt = "Inset Position",axPosInfo = [0,glInsetPos])
        self.InsetPosDlg.grid(row = 0, column = 0, sticky = 'w')
    def ConFigAxes(self):
        global glFs, glInsetFs
        if self.InsetPosDlg.chbAddAxPosVar.get() == 1:
            self.InsetPosDlg.getAxPos()
            self.InsetFig = FigInset(self.frAx[0].XYData,self.frAx[1].XYData,self.frAxPl[0].getAxConfig(),self.frAxPl[1].getAxConfig(),self.InsetPosDlg.AxPosIf[1])
        else:
            self.InsetFig = FigInset(self.frAx[0].XYData,self.frAx[1].XYData,self.frAxPl[0].getAxConfig(),self.frAxPl[1].getAxConfig())
        if self.frAddTxtDlg.chbAddTxtVar.get()==1:
            k = 0
            self.frAddTxtDlg.GetTxtDlg()
            for TxtDlg in self.frAddTxtDlg.lstTxtDlg:
                self.InsetFig.axes[0].text(self.frAddTxtDlg.lstTxtLoc[k][0],self.frAddTxtDlg.lstTxtLoc[k][1], self.frAddTxtDlg.lstTxt[k],
                                         verticalalignment='bottom', horizontalalignment='right',
                                         transform=self.InsetFig.axes[0].transAxes,
                                         color=self.frAddTxtDlg.lstTxtCl[k], fontsize=self.frAddTxtDlg.lstTxtFs[k])
                k += 1
        ConFigXScale(self.InsetFig.axes[0],self.XAxConfig[0].getAxConfig())
        ConFigYScale(self.InsetFig.axes[0],self.YAxConfig[0].getAxConfig(),'left')
        ConFigXScale(self.InsetFig.axes[1],self.XAxConfig[1].getAxConfig())
        ConFigYScale(self.InsetFig.axes[1],self.YAxConfig[1].getAxConfig(),'left')
        
        if self.frAddLbDlg.chbAddLbVar.get()== 1:
            self.frAddLbDlg.GetLabels()
            for k in range(len(self.frAddLbDlg.tbxLstLb)):
                if k == 0:
                    fs = glFs
                if k == 1:
                    fs == glInsetFs
                if self.frAddLbDlg.tbxLstLb[k].chbIncludeLbVar.get() == 1:
                    j = 0
                    for line in self.InsetFig.axes[0].get_lines():
                        line.set_label(self.frAddLbDlg.lstLb[k][j])
                        j += 1
                    self.InsetFig.axes[k].legend([line for line in self.InsetFig.axes[k].get_lines()],self.frAddLbDlg.lstLb[k],loc = StrToLctTup(self.frAddLbDlg.lstLbLct[k]), fontsize = glFs)            
        
        self.InsetFig.show()
        
    def PlotData(self):
        self.InsetFig = FigInset(self.frAx[0].XYData,self.frAx[1].XYData,self.frAxPl[0].getAxConfig(),self.frAxPl[1].getAxConfig())
        self.InsetFig.show()
        
class clsMonoAxisExlPlotDlg(clsExlPlotDlg):
    def __init__(self,parent,wbks,YAx, *args, **kwargs):
        clsExlPlotDlg.__init__(self,parent,wbks,YAx, *args, **kwargs)
    
    def ConFigAxes(self):
        
        self.PlotData()
        ConFigXScale(self.MnFig.axes[0],self.XAxConfig[0].getAxConfig())
        ConFigYScale(self.MnFig.axes[0],self.YAxConfig[0].getAxConfig(),'left')
        ConFigYScale(self.MnFig.axes[0],self.YAxConfig[0].getAxConfig(),'right')
        if self.frAddTxtDlg.chbAddTxtVar.get()==1:
            k = 0
            self.frAddTxtDlg.GetTxtDlg()
            for TxtDlg in self.frAddTxtDlg.lstTxtDlg:
                self.MnFig.axes[0].text(self.frAddTxtDlg.lstTxtLoc[k][0],self.frAddTxtDlg.lstTxtLoc[k][1], self.frAddTxtDlg.lstTxt[k],
                                         verticalalignment='bottom', horizontalalignment='right',
                                         transform=self.MnFig.axes[0].transAxes,
                                         color=self.frAddTxtDlg.lstTxtCl[k], fontsize=self.frAddTxtDlg.lstTxtFs[k])
                k += 1
        if self.frAddLbDlg.chbAddLbVar.get()== 1:
            self.frAddLbDlg.GetLabels()
            for k in range(len(self.frAddLbDlg.tbxLstLb)):
                if self.frAddLbDlg.tbxLstLb[k].chbIncludeLbVar.get() == 1:
                    j = 0
                    for line in self.MnFig.axes[0].get_lines():
                        line.set_label(self.frAddLbDlg.lstLb[k][j])
                        j += 1
                    self.MnFig.axes[k].legend([line for line in self.MnFig.axes[k].get_lines()],self.frAddLbDlg.lstLb[k],loc = StrToLctTup(self.frAddLbDlg.lstLbLct[k]), fontsize = glFs)            
            
        self.MnFig.show()
    def PlotData(self):
        self.MnFig = GnFg()
        self.MnFig.add_subplot(1,1,1)
        MonoAxis2(self.MnFig.axes[0],self.frAx[0].XYData,self.frAxPl[0].getAxConfig())#self.MnFig.axes[0]
        self.MnFig.show()

###-----------------------------------------------Excel GUIs classes----------------------------------------------------
###-----------------------------------------------Excel GUIs functions--------------------------------------------------

                
def fncLoadWorkbook():
    wdnLWB = Tk()
    wdnLWB.title('Load Excel Workbooks')
    LWB = clsLoadWorkBook(wdnLWB)
    LWB.grid(row = 0, column = 0)
    global glWbkData
    glWbkData = LWB.AllWbks
    wdnLWB.mainloop()
def fncPlotMonoAxis():
    global XYData, glWbkData
    PltMn = Tk()                             
    PltMn.title("Plot Mono Axis")
    PltMn.geometry("1000x750")
    #try:
    frPltMn = clsMonoAxisExlPlotDlg(PltMn,glWbkData,['Y Axis'])    
    PltMn.mainloop()
def fncTripleAxes():
    global XYData, glWbkData
    PltTr = Tk()                             
    PltTr.title("Plot Triple Axes")
    PltTr.geometry("1000x750")
    #try:
    frPltTr = clsExlPlotDlg(PltTr,glWbkData,['Left Axis','Middle Axis','Right Axis'])    
    #except NameError:
        #tk.messagebox.showwarning('Data Not Loaded','Please, load excel files.')
    PltTr.mainloop()
        
    
           
        
def PlotDoubleAxes(root):
    global glWbkData,lXYData,rXYData
    #global ttk
    PltDb = Tk()                             
    PltDb.title("Plot Double Axes")
    PltDb.geometry("1000x750")
    
    tabControl = ttk.Notebook(PltDb)          
    tbLAx = tk.ttk.Frame(tabControl)            
    tabControl.add(tbLAx, text='Left Axis Data')
    
    tbRAx = tk.ttk.Frame(tabControl)            
    tabControl.add(tbRAx, text='Right Axis Data')      
    tabControl.pack(expand=1, fill="both")
    
    tbPl = tk.ttk.Frame(tabControl)            
    tabControl.add(tbPl, text='Plot Setup')
    tabControl.pack(expand=1, fill="both")
    
    frLAx = clsOneAxisExlDataTbDlg(tbLAx,glWbkData)
    frLAx.grid(row = 0,column = 0)
    frRAx = clsOneAxisExlDataTbDlg(tbRAx,glWbkData)
    frRAx.grid(row = 0,column = 0)
   
    frLAxPl = clsPlotOneAxisDlg(tbPl,'Left Initial Axis Configuration')
    frLAxPl.pack(side = LEFT)
    frLAxPl.ents.entries['y Axis Title'].delete(0,'end')
    frLAxPl.ents.entries['y Axis Title'].insert(0,'Y Left Axis Title')
    
    frRAxPl = clsPlotOneAxisDlg(tbPl,'Right Initial Axis Configuration')
    frRAxPl.pack(side = RIGHT)
    frRAxPl.ents.entries['y Axis Title'].delete(0,'end')
    frRAxPl.ents.entries['y Axis Title'].insert(0,'Y Right Axis Title')
    
    lXYData = frLAx.XYData
    rXYData = frRAx.XYData
    
    btnPl = ttk.Button(tbPl, text='Plot',command=(lambda : PlotData()))
    btnPl.pack()
    
    
    
    tbAxConfig = tk.ttk.Frame(tabControl)            
    tabControl.add(tbAxConfig, text='Axes Configuration')
    tabControl.pack(expand=1, fill="both")
    
    
    XAxConfig = clsOneAxisConfigDlg(tbAxConfig,'X Axis Configuration')
    XAxConfig.grid(row = 0, column = 0, padx=2, pady=5)
    
    lYAxConfig = clsOneAxisConfigDlg(tbAxConfig,'Left Y Axis Configuration')
    lYAxConfig.grid(row = 0, column = 1, padx=2, pady=5)
    
    rYAxConfig = clsOneAxisConfigDlg(tbAxConfig,'Right Y Axis Configuration')
    rYAxConfig.grid(row = 0, column = 2, padx=2, pady=5)
    
    
    
    btnConfig = Button(tbAxConfig, text='Configure',command=lambda : ConFigAxes())
    btnConfig.grid(row = 1, column = 2, padx=5, pady=5)
    DblFig = GnFg()
    
    lblCbbAddLb = ttk.Label(tbAxConfig,text= 'Add Label', anchor='w')
    lblCbbAddLb.grid(row = 1, column = 0)
   
    def AddLabels(event):
        nonlocal tbAxConfig
        nonlocal DblFig
        if cbbAddLb.get()=='Add Labels' :
            tbxLAxLb = clsOneAxisDataLbDlg(tbAxConfig,'Left Axis Labels',frLAx.lstLb)
            tbxLAxLb.grid(row = 2, column = 0, padx=5, pady=5)
            tbxLAxLb.UpdLb()
            
            tbxRAxLb = clsOneAxisDataLbDlg(tbAxConfig,'Right Axis Labels',frRAx.lstLb)
            tbxRAxLb.grid(row = 2, column = 1, padx=5, pady=5)
            tbxRAxLb.UpdLb()
            
            def GetLabels():
                nonlocal tbxLAxLb, tbxRAxLb
                tbxLAxLb.lstLb = tbxLAxLb.get()
                tbxRAxLb.lstLb = tbxRAxLb.get()
                frLAx.lstLb = tbxLAxLb.get()
                frRAx.lstLb = tbxRAxLb.get()
                frLAx.lbLoc = tbxLAxLb.entLgdLoc.get()
                frRAx.lbLoc = tbxRAxLb.entLgdLoc.get()
            
            btnGetLb = ttk.Button(tbAxConfig, text = 'Get Labels', command = GetLabels)
            btnGetLb.grid(row = 3, column = 0, padx=5, pady=5)
    cbbAddLb= ttk.Combobox(tbAxConfig)
    cbbAddLb.grid(row=1,column = 1)
    cbbAddLb['values'] = ['No Labels','Add Labels']
    cbbAddLb.bind('<<ComboboxSelected>>', AddLabels)     
    
    def ConFigAxes():
        nonlocal DblFig,cbbAddLb
        PlotData()
        ConFigXScale(DblFig.axes[0],XAxConfig.getAxConfig())
        ConFigYScale(DblFig.axes[0],lYAxConfig.getAxConfig(),'left')
        ConFigYScale(DblFig.axes[1],rYAxConfig.getAxConfig(),'right')
        DblFig.axes[1].spines['left'].set_visible(False)
        DblFig.axes[1].spines['bottom'].set_visible(False)
        DblFig.axes[1].spines['top'].set_visible(False)
        
        if cbbAddLb.get()=='Add Labels' :
            i = 0
            for line in DblFig.axes[0].get_lines():
                line.set_label(frLAx.lstLb[i])
                i += 1
            i = 0
            for line in DblFig.axes[1].get_lines():
                line.set_label(frRAx.lstLb[i])
                i += 1
            DblFig.axes[0].legend([line for line in DblFig.axes[0].get_lines()],frLAx.lstLb,loc = StrToLctTup(frLAx.lbLoc), fontsize = glFs)
            DblFig.axes[1].legend([line for line in DblFig.axes[1].get_lines()],frRAx.lstLb,loc = StrToLctTup(frRAx.lbLoc), fontsize = glFs)
        DblFig.show()
    def PlotData():
        nonlocal DblFig
        DblFig = DoubleAxes(frLAx.XYData,frRAx.XYData,frLAxPl.getAxConfig(),frRAxPl.getAxConfig())
        DblFig.show()
    PltDb.mainloop()
def fncPlotInset():
    global XYData, glWbkData
    PltInset = Tk()                             
    PltInset.title("Plot a Figure with an Inset")
    PltInset.geometry("1000x750")
    #try:
    frPltInset = clsInsetExlPlotDlg(PltInset,glWbkData,['Main Y Axis', 'Inset Y Axis'])    
    #except NameError:
        #tk.messagebox.showwarning('Data Not Loaded','Please, load excel files.')
    PltInset.mainloop()

  
def fncSettings():
    Settings = Tk()                             
    Settings.title("Settings")
    Settings.geometry("1000x750")
    frSettings = clsSettingsDlg(Settings)    
    Settings.mainloop()

class clsSettingsDlg(ttk.Frame):
    global glSettings
    def __init__(self,parent, *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        self.dicStt = {}
        self.SttVar = tk.IntVar(master = parent)
        self.SttVar.set(1)
        #frame to store list of settings objects
        self.frLstSttObj = tk.Frame(parent,background = 'white', highlightbackground="red", highlightcolor="red", highlightthickness=3, height = 700, width = 220)
        self.frLstSttObj.grid_propagate(0)
        self.frLstSttObj.grid(row = 0,column = 0, padx = 5, pady = 5)
        i = 1
        for k,v in glSettings.items():
            self.dicStt.update({k: tk.Radiobutton(self.frLstSttObj, 
                  text=k,
                  indicatoron = 0,
                  width = 20,
                  padx = 20, 
                  variable=self.SttVar, 
                  command= lambda : self.DisplaySettings(),
                  value=i)})
            self.dicStt[k].grid(row = i, column = 0, padx = 5, pady = 5, sticky = 'w')
            i +=1
        self.frObjDtl = clsFrameWScrollBar(parent,[760,700], background = 'white', highlightbackground="green", highlightcolor="green", highlightthickness=3)
        self.frObjDtl.grid_propagate(0)
        self.frObjDtl.grid(row = 0,column = 1, padx = 5, pady = 5, sticky = 'w')
        self.btnSave = ttk.Button(parent, text = 'Save', command = lambda : self.SaveSettings())
        self.btnSave.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'E')
    
    def SaveSettings(self):
        a = 1
    def DisplaySettings(self):
        self.frObjDtl.canvas.delete('all')
        if self.SttVar.get() == 1:
            self.frGlPar = clsGlParDlg(self.frObjDtl.canvas, 'Global Parameters')
            self.frGlPar.grid(row = 0, column = 0, sticky = 'w')
        if self.SttVar.get() == 2:
            a = 1
        if self.SttVar.get() == 3:
            self.frAxPl = clsPlotOneAxisDlg(self.frObjDtl.canvas,'Initial Y Axis')
            self.frAxPl.grid(row = 0, column = 0, sticky = 'w')
        if self.SttVar.get() == 4:
            self.frAxPl = clsOneAxisConfigDlg(self.frObjDtl.canvas,'Initial Y Axis')
            self.frAxPl.grid(row = 0, column = 0, sticky = 'w')
    def LoadSettings(self):
        a = 1
class clsGlParDlg(clsDataEntDlg):
    global fldGlPar, dvGlPar
    def __init__(self,parent,frTxt, *args, **kwargs):
        clsDataEntDlg.__init__(self,parent,frTxt,fldGlPar,dvGlPar,*args, **kwargs)

class clsFilePathDlg(ttk.Frame):
    a = 1       
class clsSaveFig(ttk.Frame):
    def __init__(self,parent,*args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        self.lbDpi = ttk.Label(self, text = 'Resolution in dpi')
        self.lbDpi.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.entDpi = ttk.Entry(self)
        self.entDpi.grid(row = 0, column = 1, padx = 5, pady = 5)
        self.entDpi.insert(0,'300')
        
        self.lbFigSize = ttk.Label(self, text = 'Figure width (mm)')
        self.lbFigSize.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.entFigSize = ttk.Entry(self)
        self.entFigSize.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.entFigSize.insert(0,'85')
        """
        self.lbFigName = ttk.Label(self, text = 'Figure Name', anchor = 'w')
        self.lbFigName.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.entFigName = ttk.Entry(self)
        self.entFigName.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'w')
        self.entFigName.insert(0,'TestFig')
        """
        self.btnSave = ttk.Button(self, text='Save Figure',command=(lambda : self.SaveFigure()))
        self.btnSave.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')
    def SaveFigure(self):
        
        try:
            FileName = filedialog.asksaveasfilename(defaultextension = ".tif",
                                                    filetypes=[("Tagged Image File Format *.tif *.tiff","*.tif *.tiff"),
                                                               ("Encapsulated Postscript *.eps","*.eps"),
                                                               ("Joint Photographic Experts Group *.jpg","*.jpg"),
                                                               ("PGF code for LaText *.pgf","*.pgf"),
                                                               ("Portable Document Format *.pdf", "*.pdf"),
                                                               ("Portable Network Graphics *.png", "*.png"),
                                                               ("Postscript *.ps", "*.ps"),
                                                               ("Bitmap *.bmp", "*.bmp"),
                                                               ("Scalable Vector Graphics *.svg *.svgz", "*.svg *.svgz"),
                                                               ("All files *.*","*.*")],
                                                    parent = self,
                                                    title = "Save the Figure")
        except FileNotFoundError:
            pass
        TempFig = plt.gcf()
        plt.savefig(FileName, dpi = int(self.entDpi.get()))
        image = Image.open(FileName)
        #Current image size
        CSize = inch2mm(TempFig.get_size_inches()) #
        CSizePx = image.size
        #Target image size 
        #a = int(self.entFigSize.get())
        #TSize = int(self.entFigSize.get()),127.5
        TSize = int(self.entFigSize.get()), int(self.entFigSize.get())*CSize[0][1]/CSize[0][0]#
        
        
        Ratio = tuple(CSize[0][i]/TSize[i] for i in range(2))
        TSizePx =tuple(int(CSizePx[i]/Ratio[i]) for i in range(2))
        image = image.resize (TSizePx, Image.ANTIALIAS)
        global glPlotStt
        image.save(FileName)
        image.close()
        
    
def fncSaveFigure():
    SaveFig = Tk()                             
    SaveFig.title("Save Figure")
    SaveFig.geometry("400x300")
    frSaveFig = clsSaveFig(SaveFig)    
    frSaveFig.grid(row = 0, column = 0, padx = 5, pady = 5)
    frSaveFig.mainloop()
    
class clsFrameWScrollBar2(tk.Frame):
    def __init__(self,parent,AddScbH = True, AddScbV = True, *args, **kwargs):
        tk.Frame.__init__(self,parent, *args, **kwargs)
        #Create a canvas inside the scroling frame
        self.canvas = tk.Canvas(self, 
                                #background = 'White', 
                                width = self.winfo_width()-30, height = self.winfo_height()-30)
        self.canvas.grid(row=0, column = 0, sticky = 'WENS')
        #Create a horizontal scroll bar
        if AddScbH:
            self.scbH = ttk.Scrollbar(self, orient=HORIZONTAL)
            self.scbH.grid(row = 1, column = 0,sticky = 'WE')
            #Conect the canvas with the horizontal  scroll bar
            self.canvas.config(xscrollcommand=self.scbH.set)
            self.scbH.config(command=self.canvas.xview)
        #Create a vertical scroll bar
        if AddScbV:
            self.scbV = ttk.Scrollbar(self)
            self.scbV.grid(row = 0, column = 1, sticky = 'NS')
            #Conect the canvas with the vertical scroll bar
            self.canvas.config(yscrollcommand=self.scbV.set)
            self.scbV.config(command=self.canvas.yview)
        #create a frame inside the canvas
        self.frame=ttk.Frame(self.canvas,width = self.canvas.winfo_width(), height = self.canvas.winfo_height())
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        # binding  the function Configure of the frame with the Canvas - Not sure what is it for?
        def cnvConfig(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=self.winfo_width()-30,height=self.winfo_height()-30)
        self.frame.bind("<Configure>",cnvConfig)
      
   

def fncSaveInfo(Info,pr,endTxt = ""):
    try:
        File = filedialog.asksaveasfilename(defaultextension = ".inf",
                                                filetypes=[('Python pypGUI Info File','*.inf'), ('All files','*.*')],
                                                parent = pr,
                                                title = "Save a pypGUI Info File")
    except FileNotFoundError:
        pass
    path, filename = os.path.split(File)
    filename = os.path.splitext(filename)[0]
    newfilename = '%s_%s.inf' % (filename,endTxt)
    newFile = os.path.join(path, newfilename)
    file = open( newFile, "wb" )
    pickle.dump(Info, file, protocol=pickle.HIGHEST_PROTOCOL )
    file.close()

def fncLoadInfo(pr):
    FileName = filedialog.askopenfilename(defaultextension = ".inf",
                                                filetypes=[('Python pypGUI Info File','*.inf'), ('All files','*.*')],
                                                parent = pr,
                                                title = "Open a pypGUI Info File")
    file = open( FileName, "rb" )
    return pickle.load(file)

class clsSaveLoadInfoDlg(ttk.Frame):
    def __init__(self,parent,endTxt = "",  *args, **kwargs):      
        ttk.Frame.__init__(self, parent, *args, **kwargs) 
        self.endTxt = endTxt
        self.btnSaveInfo = ttk.Button(self, text="Save Info", command = lambda: self.SaveInfo(parent))
        self.btnSaveInfo.grid(row =0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.btnLoadInfo = ttk.Button(self, text="Load Info", command = lambda: self.LoadInfo(parent))
        self.btnLoadInfo.grid(row =0, column = 1, padx = 5, pady = 5, sticky = 'nw')
    def SaveInfo(self, parent, *args, **kwargs):
        parent.get()
        fncSaveInfo(parent.If,parent,self.endTxt)
    def LoadInfo(self, parent, *args, **kwargs):
        parent.If = fncLoadInfo(parent)
        parent.populate()

class clsFigLayDlg(ttk.Frame):# A class to handle data from excel workbook for one sub plot
    global fldGlFigLayout, dvGlFigLayout
    def __init__(self,parent, Info = dvGlFigLayout, *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)        
        self.fields = fldGlFigLayout
        self.frSaveLoadInfo = clsSaveLoadInfoDlg(self, "FigLay")
        self.frSaveLoadInfo.grid(row = 0, column = 0, padx= 5, pady = 5, sticky = 'nw')
        try:
            self.If = Info
            self.DefaultVal = [str(self.If[i]) for i in range(len(self.If))]
        except TypeError:
            self.DefaultVal =  [str(dvGlFigLayout[i]) for i in range(len(dvGlFigLayout))]
            self.If = []    
        self.frFigLay = clsMakeFrame(self,{"entries": {"fields": self.fields,"default values": self.DefaultVal}})
        self.frFigLay.grid(row = 1, column = 0, sticky = 'nw')
        
        # A frame storing an Subplot Layout frame
        self.frSpLayout = ttk.Frame(self)
        self.frSpLayout.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            SpLtIf = self.If[3]
        except IndexError:
            SpLtIf = None
        self.frSpLayoutDlg = clsAddSpLayoutDlg(self.frSpLayout, SpLayoutInfo = SpLtIf)
        self.frSpLayoutDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        """
        self.RowNumVar = tk.StringVar(master = parent)
        self.frFigLay.entries["Number of Rows"].textvariable = self.RowNumVar
        self.Updating = False
        self.RowNumVar.trace("w",lambda : self.UpdateFigSize())
        """
        
    def get(self, *args, **kwargs):
        self.If = []
        i = 0
        for field in self.fields:
            if i < 2:
                self.If.append(int(self.frFigLay.entries[field].get()))
            else:
                self.If.append(StrToInsetLctTup(self.frFigLay.entries[field].get()))
            i += 1
        self.If.append(self.If.append(self.frSpLayoutDlg.get()))
        return self.If
    def populate(self, *args, **kwargs):
        self.frFigLay.If = self.If
        self.frFigLay.setInfo()
    def UpdateFigSize(self,*args):
        if self.Updating: return
        self.frFigLay.entries["Figure Size"].delete(0,"end")
        
        self.Updating = True
        h = int(self.frFigLay.entries["Number of Rows"].get())*self.If[2][1]
        self.If[2][1] = h
        self.frFigLay.entries["Figure Size"].set(str(self.If[2]))
        self.Updating = False
        
class clsOneAxisExlDataDlg(ttk.Frame):   # A class to store data from excel workbooks 
    global glDctExlData
    def __init__(self,parent,wbks,Info = None, dct = glDctExlData, *args, **kwargs):
        self.dct = dct
        if Info == None:
            self.If = {}
        else:
            self.If = Info
        def UpdateShtCbb(event):
            a = self.WbksCbb.get()
            self.ShtCbb['values'] = self.dctShts[a]
        self.lstWbks = list(wbks.keys())
        self.dctShts = {}
        for Wbk in self.lstWbks:
            self.dctShts.update({Wbk:wbks[Wbk].get_sheet_names()})
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        self.WbksLb = ttk.Label(self,text = dct["fields"][0])
        self.WbksLb.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nw")
        self.WbksCbb = ttk.Combobox(self)
        self.WbksCbb.grid(row=0,column = 1, padx = 5, pady = 5, sticky = "nw")
        self.WbksCbb['values'] = self.lstWbks
        
        """
        #donot delete yet 20180716
        if Info != None:
            self.WbksCbb.set(Info["Workbook"])
        """
        self.WbksCbb.bind('<<ComboboxSelected>>', UpdateShtCbb)
        
        #Sheet Combobox Options
        self.ShtLb = ttk.Label(self,text = dct["fields"][1])
        self.ShtLb.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nw")
        self.ShtCbb = ttk.Combobox(self)
        self.ShtCbb.grid(row=1,column = 1, padx = 5, pady = 5, sticky = "nw")
        """
        #donot delete yet 20180716
        if Info != None:
            self.ShtCbb.set(Info["Sheet"])
        else:
            self.ShtCbb['values'] = []
        """
        
        self.XrangeLb = ttk.Label(self, text = dct["fields"][2])
        self.XrangeLb.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nw")
        self.XrangeEnt = ttk.Entry(self)
        self.XrangeEnt.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nw")
        
        """
        #donot delete yet 20180716
        if Info != None:
            self.XrangeEnt.insert(0,Info["X Range"])
        else:
            self.XrangeEnt.insert(0,dct["default values"][2])
        """
        self.YrangeLb = ttk.Label(self,text = dct["fields"][3])
        self.YrangeLb.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nw")
        self.YrangeEnt = ttk.Entry(self)
        self.YrangeEnt.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nw")
        
        self.chbAddZAxisVar = tk.IntVar(master = parent)
        self.chbAddZAxis = ttk.Checkbutton(self,text = "Add Z Axis", variable = self.chbAddZAxisVar, command = lambda: self.AddZAxis())
        self.chbAddZAxis.grid(row=4,column=0, padx = 5, pady = 5, sticky = 'nw')
        
        
        """
        #donot delete yet 20180716
        if Info != None:
            self.YrangeEnt.insert(0,Info["Y Range"])
        else:
            self.YrangeEnt.insert(0,dct["default values"][3])
        """
        self.populate()
    def AddZAxis(self, *args, **kwargs):
        if self.chbAddZAxisVar.get() == 1:
            self.ZrangeLb = ttk.Label(self,text = self.dct["fields"][4])
            self.ZrangeLb.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "nw")
            self.ZrangeEnt = ttk.Entry(self)
            self.ZrangeEnt.grid(row = 5, column = 1, padx = 5, pady = 5, sticky = "nw")
        else:
            self.ZrangeLb.destroy()
            self.ZrangeEnt.destroy()
    def get(self,*args,**kwargs):
        self.If.clear()
        self.If["Workbook"] = self.WbksCbb.get()
        self.If["Sheet"] = self.ShtCbb.get()
        self.If["X Range"] = self.XrangeEnt.get()
        self.If["Y Range"] = self.YrangeEnt.get()
        if self.chbAddZAxisVar.get() == 1:
            self.If["Z Range"] = self.ZrangeEnt.get()
        self.If["Workbook List"] = self.lstWbks
        self.If["Sheet Dictionary"] = self.dctShts
        return self.If
    def populate(self,*args,**kwargs):
        if self.If != None:
            try:
                self.WbksCbb.set(self.If["Workbook"])
                self.WbksCbb['values'] = self.If["Workbook List"]
                
            except (KeyError,TypeError,NameError) as e:
                pass
            try:
                self.ShtCbb.set(self.If["Sheet"])
                self.ShtCbb['values'] = self.If["Sheet Dictionary"][self.If["Workbook"]]
                
            except (KeyError,TypeError,NameError) as e:
                pass
            try:
                self.XrangeEnt.delete(0,'end')
                self.XrangeEnt.insert(0,self.If["X Range"])
            except (KeyError,TypeError,NameError) as e:
                pass
            try:
                self.YrangeEnt.delete(0,'end')
                self.YrangeEnt.insert(0,self.If["Y Range"])
            except (KeyError,TypeError,NameError) as e:
                pass
            try:
                self.ZrangeEnt.delete(0,'end')
                self.ZrangeEnt.insert(0,self.If["Z Range"])
            except (AttributeError,KeyError,TypeError,NameError) as e:
                pass


class clsOneAxisExlDataTbDlg(ttk.Frame): # A class to handle data from excel workbooks
    global glDctExlData
    global dctErrBar
    
    dctErrBar = {"fields" : ["Workbooks", "Sheets", "X err range", "Y err range","Z err range"], "default values" : ["","","","",""]}
    def __init__(self,parent,wbks, lstInfo = None, *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        self.frSaveLoadInfo = clsSaveLoadInfoDlg(self,"1AxDat")
        self.frSaveLoadInfo.grid(row = 0, column = 0, padx= 5, pady = 5, sticky = 'nw')
        self.frMain = ttk.Frame(self)
        self.frMain.grid(row = 1, column = 0,  padx = 5, pady = 5, sticky = 'nw')
        
        self.btnLoadData = ttk.Button(self.frMain,text = 'Load Data', width = 10, command = lambda : self.LoadData())  
        self.btnLoadData.grid(row = 0, column = 0,  padx = 5, pady = 5, sticky = 'nw') 
        self.btnAdd = ttk.Button(self.frMain,text = 'Add', width = 8, command = lambda : self.AddOneAxisExlDataDlg())  
        self.btnAdd.grid(row =0,column = 1, padx = 5, pady = 5, sticky = 'nw')
        self.btnRemove = ttk.Button(self.frMain,text = 'Remove', width = 10, command = lambda : self.RemoveOneAxisExlDataDlg())  
        self.btnRemove.grid(row =0, column = 2, padx = 5, pady = 5, sticky = 'nw')
        self.chbErrBarVar = tk.IntVar(master = parent)
        self.chbErrBar = ttk.Checkbutton(self.frMain,text = 'Add Error Bar',variable = self.chbErrBarVar, command = lambda: self.AddErrBar()) 
        self.chbErrBar.grid(row = 0,column = 3, padx = 5, pady = 5, sticky = 'nw')
        self.wbks = wbks
        try:
            self.If = lstInfo[:(len(lstInfo)-1)]
            self.lstErrBarIf = lstInfo[(len(lstInfo)-1)]
        except (TypeError, IndexError) as e:
            self.If = None
            self.lstErrBarIf = None
        self.frLst = []
        if self.If == None:
            self.frLst.append(clsOneAxisExlDataDlg(self.frMain,wbks, Info = None))
            self.frLst[0].grid(row = 1,column = 0, columnspan =3, padx = 5, pady = 5, sticky = 'nw')
        else:
            for i in range(len(self.If)):
                self.frLst.append(clsOneAxisExlDataDlg(self.frMain,wbks, Info = self.If[i]))
                self.frLst[i].grid(row = 1+i,column = 0, columnspan =3, padx = 5, pady = 5, sticky = 'nw')
        
        self.frErrBarLst = []
        if self.lstErrBarIf != None:
            self.chbErrBarVar.set(1)
            self.AddErrBar()
        
        self.XYData = []
        self.XYErrBarData = []
        self.lstLb = []
        self.lstWbks =self.frLst[0].lstWbks
        if self.If != None:
            self.LoadData()
            self.get()
       
        
        
    def LoadData(self,*args,**kwargs):
        self.XYData = []
        self.XYErrBarData = []
        self.lstLb = []
        for fr in self.frLst:
            for Wbk in fr.lstWbks:
                CmnWbkName = fr.WbksCbb.get()
                wb = self.wbks[Wbk]
                if CmnWbkName in Wbk:
                    CmnShtName = fr.ShtCbb.get()
                    for SheetName in fr.dctShts[Wbk]:
                        if CmnShtName in SheetName:
                            try:
                                Xrange = GetRange(wb[SheetName][fr.XrangeEnt.get()])
                            except IndexError:
                                Xrange = []
                            try:
                                Yrange = GetRange(wb[SheetName][fr.YrangeEnt.get()])
                            except IndexError:
                                Yrange = []     
                            self.XYData.append([Xrange,Yrange])
                            self.lstLb.append(fr.XrangeEnt.get()+'-'+fr.YrangeEnt.get()+'-'+SheetName+'-'+Wbk)
        
        if self.chbErrBarVar.get() == 1:
            for fr in self.frErrBarLst:
                for Wbk in fr.lstWbks:
                    CmnWbkName = fr.WbksCbb.get()
                    wb = self.wbks[Wbk]
                    if CmnWbkName in Wbk:
                        CmnShtName = fr.ShtCbb.get()
                        for SheetName in fr.dctShts[Wbk]:
                            if CmnShtName in SheetName:
                                try:
                                    Xrange = GetRange(wb[SheetName][fr.XrangeEnt.get()])
                                except IndexError:
                                    Xrange = []
                                try:
                                    Yrange = GetRange(wb[SheetName][fr.YrangeEnt.get()])
                                except IndexError:
                                    Yrange = []     
                                self.XYErrBarData.append([Xrange,Yrange])
        for i in range(len(self.XYErrBarData)):
            for j in range(len(self.XYErrBarData[i])):
                self.XYData[i].append(self.XYErrBarData[i][j])
        
        return self.XYData  
    def AddOneAxisExlDataDlg(self,*args,**kwargs):
        global glDctExlData
        global dctErrBar
        self.frLst.append(clsOneAxisExlDataDlg(self.frMain,self.wbks))
        
        self.frLst[len(self.frLst)-1].grid(row=len(self.frLst),column = 0, columnspan =3, padx = 5, pady = 5, sticky = 'nw')
        if self.chbErrBarVar.get() == 1:
            #fr = clsOneAxisExlDataDlg(self.frMain,self.wbks,dct = dctErrBar)
            #fr.grid(row=len(self.frErrBarLst)+1,column = 3, columnspan = 2, padx = 5, pady = 5, sticky = 'nw')
            #self.frErrBarLst.append(fr)
            self.frErrBarLst.append(clsOneAxisExlDataDlg(self.frMain,self.wbks,dct = dctErrBar))
            self.frErrBarLst[len(self.frErrBarLst)-1].grid(row=len(self.frErrBarLst),column = 3, columnspan = 2, padx = 5, pady = 5, sticky = 'nw')
            
            
    def RemoveOneAxisExlDataDlg(self,*args,**kwargs):
        if (len(self.frLst)) > 0:
            self.frLst[len(self.frLst)-1].destroy()
            self.frLst = self.frLst[:(len(self.frLst)-1)]
        if self.chbErrBarVar.get() == 1:
            if (len(self.frErrBarLst)) > 0:
                self.frErrBarLst[len(self.frErrBarLst)-1].destroy()
                self.frErrBarLst = self.frErrBarLst[:(len(self.frErrBarLst)-1)]
                if (len(self.frErrBarLst)) == 0:
                    self.chbErrBarVar.set(0)
    def get(self,*args,**kwargs):
        self.If = []
        for fr in self.frLst:
            self.If.append(fr.get())
        self.lstErrBarIf = []
        for fr in self.frErrBarLst:
            self.lstErrBarIf.append(fr.get())
        self.If.append(self.lstErrBarIf)
        return self.If
    def populate(self,*args,**kwargs):
        self.chbErrBarVar.set(1)
        ErrBarNum = len(self.If[len(self.If)-1])
        nonErrBarNum = len(self.If)-1-ErrBarNum
        for i in range(len(self.frLst)):
            self.RemoveOneAxisExlDataDlg()
        self.chbErrBarVar.set(0)
        for i in range(nonErrBarNum):
            self.AddOneAxisExlDataDlg()
        if ErrBarNum > 0:
            self.chbErrBarVar.set(1)
            for i in range(ErrBarNum):
                self.AddOneAxisExlDataDlg()
        self.lstErrBarIf = self.If[len(self.If)-1]
        i = 0
        j = len(self.If) -1
        for fr in self.frErrBarLst:
            try:
                fr.If = self.lstErrBarIf[i]
                fr.populate()
            except (IndexError, KeyError, NameError, TypeError) as e:
                pass
            i +=1
        i = 0
        
        
        for fr in self.frLst:
            try:
                fr.If = self.If[i]
                fr.populate()
            except (IndexError, KeyError, NameError, TypeError) as e:
                pass
            i +=1
        
    def getLbLst(self,*args,**kwargs):
        if len(self.lstLb) == 0:
            self.LoadData()
        return self.lstLb
    def AddErrBar(self,*args,**kwargs):
        global dctErrBar
        if self.chbErrBarVar.get() == 1:
            if self.lstErrBarIf == None:
                self.frErrBarLst.append(clsOneAxisExlDataDlg(self.frMain,self.wbks, Info = None, dct = dctErrBar))
                self.frMain.frErrBarLst[0].grid(row = 1,column = 3, columnspan = 2, padx = 5, pady = 5, sticky = 'nw')
            else:
                for i in range(len(self.lstErrBarIf)):
                    self.frErrBarLst.append(clsOneAxisExlDataDlg(self.frMain,self.wbks, Info = self.lstErrBarIf[i], dct = dctErrBar))
                    self.frErrBarLst[i].grid(row = 1+i,column = 3, columnspan = 2, padx = 5, pady = 5, sticky = 'nw')
        else:
            if len(self.frErrBarLst) > 0:
                for fr in self.frErrBarLst:
                    fr.destroy()
                self.frErrBarLst = []
                
class clsSubPlotExlDataTbDlg(clsFrameWScrollBar):# A class to handle data from excel workbook for one sub plot
    
    def __init__(self,parent,frSize,spLb = 'Sub Plot', spInfo = None, *args, **kwargs):
        global glWbkData
        global glFigTypes
        clsFrameWScrollBar.__init__(self,parent,frSize,*args, **kwargs)
        self.frSaveLoadInfo = clsSaveLoadInfoDlg(self,"spDat")
        self.frSaveLoadInfo.grid(row = 0, column = 0, padx= 5, pady = 5, sticky = 'nw')
        self.frMain = ttk.Frame(self.frame)
        self.frMain.grid(row = 1, column = 0, sticky = 'nw')
        lbSubPlot = ttk.Label(self.frMain,text = spLb)
        lbSubPlot.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.FigType = clsMakeFrame(self.frMain,{"comboboxes" : {"fields" : ["Figure Type"], "default values" : [glFigTypes]}})
        self.FigType.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.conData = ttk.Frame(self.frMain)
        self.conData.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.FigType.comboboxes["Figure Type"].bind('<<ComboboxSelected>>', self.DisplayDataEnts)
        self.frData = []
        if spInfo == None:
            self.If ={}
        else:
            self.If = spInfo
            self.FigType.comboboxes["Figure Type"].set(spInfo["Figure Type"])
        self.DisplayDataEnts()
    def DisplayDataEnts(self, *args, **kwargs):
        global glWbkData
        if self.FigType.comboboxes["Figure Type"].get() == "Mono Axis":
            Axes = ["Mono Axis Data"]    
        if self.FigType.comboboxes["Figure Type"].get() == "Double Axes":
            Axes = ["Left Axis Data", "Right Axis Data"]
        if self.FigType.comboboxes["Figure Type"].get() == "Double Axes with an Inset":
            Axes = ["Main Axis", "Inset Axis"]
        if self.FigType.comboboxes["Figure Type"].get() == "Triple Axes":
            Axes = ["Left Axis", "Middle Axis", "Right Axis"]
        for wdg in self.conData.winfo_children():
            wdg.destroy()
        i = 0
        self.frData = []
        for ax in Axes:
            lb = ttk.Label(self.conData, text = ax)
            lb.grid(row = 0, column = i, padx = 5, pady = 5, sticky = 'nw')
            fr = ttk.Frame(self.conData)
            fr.grid(row = 1, column = i, padx = 5, pady = 5, sticky = 'nw')
            if not self.If:
                dtSc = None
            else:
                try:
                    dtSc = self.If["Data Load Setup"][i]
                except IndexError:
                    dtSc = None
            self.frData.append(clsOneAxisExlDataTbDlg(fr,glWbkData, lstInfo = dtSc))
            self.frData[i].grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
            i += 1
    def get(self, *args, **kwargs):
        self.If.clear()
        self.If["Figure Type"] = self.FigType.comboboxes["Figure Type"].get()  
        self.If["Data"] = []
        self.If["Data Load Setup"] = []
        self.If["Data Source"] = []
        if self.frData != None:
            for fr in self.frData:
                self.If["Data"].append(fr.LoadData())
                self.If["Data Load Setup"].append(fr.get())
                self.If["Data Source"].append(fr.getLbLst())
        return self.If
    def populate(self,*args,**kwargs):
        self.FigType.comboboxes["Figure Type"].set(self.If["Figure Type"])
        self.DisplayDataEnts()
        for fr in self.frData:
            fr.populate()

class clsExlDataTbDlg(ttk.Frame):# A class to handle data from excel workbook for DataTab   
    def __init__(self,parent, FigLayInfo = None, Info = None, *args, **kwargs):
        global glWbkData
        global glFigTypes
        ttk.Frame.__init__(self,parent,*args, **kwargs)
        
        self.frSize =[max(parent.winfo_width(),1000),max(parent.winfo_height(),750)]
        self.frData = []
        self.FigLayIf = FigLayInfo
        self.If = Info
        self.frMain = ttk.Frame(self)
        self.frMain.grid(row = 0, column = 0, sticky = 'nw')
        self.frSaveLoadInfo = clsSaveLoadInfoDlg(self,"Dat")
        self.frSaveLoadInfo.grid(row = 1, column = 0, padx= 5, pady = 5, sticky = 'nw')
        
        if self.FigLayIf != None:
            for i in range(self.FigLayIf[0]):
                for j in range(self.FigLayIf[1]):
                    try:
                        spIf = self.If[i*self.FigLayIf[1]+j]
                    except (NameError, TypeError, KeyError,IndexError) as e:
                        spIf = None
                    
                    SubPlotData = clsSubPlotExlDataTbDlg(self.frMain,
                                                         [(self.frSize[0]-20)/(self.FigLayIf[1]),
                                                          (self.frSize[1]-60)/(self.FigLayIf[0])-60], 
                                                          spLb = "Sub Plot " + str(i*self.FigLayIf[1]+j+1),
                                                          spInfo = spIf) #(self,parent,frSize,wbks,spLabel, *args, **kwargs)
                    SubPlotData.grid(row = i, column = j, padx = 5, pady = 5, sticky = 'nw')
                    self.frData.append(SubPlotData) 
    def get(self, *args, **kwargs):
        self.If = []
        if self.frData != None:                      
            for fr in self.frData:
                self.If.append(fr.get())
        return self.If
    def populate(self, *args, **kwargs):
        i = 0
        for fr in self.frData:
            try:
                fr.If = self.If[i]
                fr.populate()
            except (IndexError, NameError, TypeError, KeyError) as e:
                pass
            i += 1
        
    
class clsAxSetup(ttk.Frame):    
    def __init__(self,parent, Info = None, *args, **kwargs):
        ttk.Frame.__init__(self,parent,*args, **kwargs)
        global glDctSubPlotSetup
        #self.frMain = ttk.Frame(self)
        #self.frMain.grid(row = 0, column = 0, sticky = 'nw')
        
        self.If = Info
         
        
        #if self.If != None:
        self.populate()
    #Get all values in the entries for plot configuration    
    def get(self,*args,**kwargs):
        Temp = []
        if self.fr.comboboxes != None:
            for field in list(self.fr.comboboxes.keys()):
                Temp.append(self.fr.comboboxes[field].get())
        if self.fr.entries != None:
            for field in list(self.fr.entries.keys()):
                Temp.append(self.fr.entries[field].get())
        if self.frLogBaseDlg.chbAddVar.get() == 1:
            Temp.append(self.frLogBaseDlg.get())
        self.If = Temp
        
        return self.If
    def populate(self,*args,**kwargs):
        for wdg in self.winfo_children():
            wdg.destroy()
        self.frSaveLoadInfo = clsSaveLoadInfoDlg(self,"1Su")
        self.frSaveLoadInfo.grid(row = 0, column = 0, padx= 5, pady = 5, sticky = 'nw')
        self.fr=clsMakeFrame(self,glDctSubPlotSetup)
        self.fr.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')#pack(expand=1, fill="both")
        
        i = 0
        if self.If != None:
            for field in list(self.fr.comboboxes.keys()):
                self.fr.comboboxes[field].set(self.If[i])
                i += 1
            for field in list(self.fr.entries.keys()):
                self.fr.entries[field].delete(0, 'end')
                self.fr.entries[field].insert(0,self.If[i])
                i += 1
        # A frame storing an Add Log Base frame
        self.frAddLogBase = ttk.Frame(self.fr)
        self.frAddLogBase.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            lgbIf = self.If[6]#None#self.If["Log Base"]
        except (TypeError,IndexError) as e:
            lgbIf = None
        self.frLogBaseDlg = clsAddLogBaseDlg(self.frAddLogBase, lgbInfo = lgbIf)
        self.frLogBaseDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')

class clsSubPlotSetupTbDlg(clsFrameWScrollBar):# A class to handle data for one sub plot
    def __init__(self,parent,frSize,spLb = 'Sub Plot', spInfo = {"Figure Type": 'Mono Axis', "Data" : [[]], "Data Load Setup" : [[]], "Data Source" : [[]]}, spSetup = None, fig = None, gs = None, *args, **kwargs):
        clsFrameWScrollBar.__init__(self,parent,frSize,*args, **kwargs)
        self.parent = parent
        self.Fig = fig
        self.gs = gs
        self.Info = spInfo
        self.title = spLb + " " + spInfo["Figure Type"]
        self.frConfigLst = []
        lbSubPlot = ttk.Label(self.frame,text = self.title)
        lbSubPlot.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.frSaveLoadInfo = clsSaveLoadInfoDlg(self,"2Su")
        self.frSaveLoadInfo.grid(row = 0, column = 0, padx= 5, pady = 5, sticky = 'nw')
        self.conData = ttk.Frame(self.frame)
        self.conData.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
        if self.Info["Figure Type"] == "Mono Axis":
            self.Axes = ["Mono Axis"]
        if self.Info["Figure Type"] == "Double Axes":
            self.Axes = ["Left Axis", "Right Axis"]
        if self.Info["Figure Type"] == "Double Axes with an Inset":
            self.Axes = ["Main Axis", "Inset Axis"]
        if self.Info["Figure Type"] == "Triple Axes":
            self.Axes = ["Left Axis", "Middle Axis", "Right Axis"]
        if spSetup == None:
            self.If = []
        else:
            self.If = spSetup
        self.populate()
        """
        self.frData = []
        if spInfo["Figure Type"] == "Mono Axis":
            self.Axes = ["Mono Axis"]
        if spInfo["Figure Type"] == "Double Axes":
            self.Axes = ["Left Axis", "Right Axis"]
        if spInfo["Figure Type"] == "Double Axes with an Inset":
            self.Axes = ["Main Axis", "Inset Axis"]
        if spInfo["Figure Type"] == "Triple Axes":
            self.Axes = ["Left Axis", "Middle Axis", "Right Axis"]
        if self.conData.winfo_children() != None:
            for wdg in self.conData.winfo_children():
                wdg.destroy()
        i = 0
        self.frPlotSetup = []
        if spSetup == None:
            self.If = []
        else:
            self.If = spSetup
        for ax in self.Axes:
            lb = ttk.Label(self.conData, text = ax)
            lb.grid(row = 0, column = i, padx = 5, pady = 5, sticky = 'nw')
            fr = ttk.Frame(self.conData)
            fr.grid(row = 1, column = i, padx = 5, pady = 5, sticky = 'nw')
            try:
                Su = self.If[i]
            except IndexError:
                Su = None
            self.frPlotSetup.append(clsAxSetup(fr, Info = Su))
            self.frPlotSetup[i].grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
            i +=1
        self.btnPlot = ttk.Button(self.frame, text = 'Plot Axes', command = lambda : self.PlotAxes())
        self.btnPlot.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.btnConfig = ttk.Button(self.frame, text = 'Configure Axes', command = lambda : self.ConfigAxes())
        self.btnConfig.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'nw')
        """
    def get(self, *args, **kwargs):
        self.If = []
        if self.frPlotSetup != None:
            for fr in self.frPlotSetup:
                self.If.append(fr.get())
        #self.If.append(self.Info)
        return self.If
    def populate(self, *args, **kwargs):
        self.frConfigLst = []
        self.frData = []
        """
        try:
            Temp = self.If[len(self.If)-1]
            if Temp["Figure Type"] != None:
                self.Info = Temp
        except (NameError, IndexError, TypeError) as e:
            pass
        """
        
        if self.conData.winfo_children() != None:
            for wdg in self.conData.winfo_children():
                wdg.destroy()
        i = 0
        self.frPlotSetup = []
        
        for ax in self.Axes:
            lb = ttk.Label(self.conData, text = ax)
            lb.grid(row = 0, column = i, padx = 5, pady = 5, sticky = 'nw')
            fr = ttk.Frame(self.conData)
            fr.grid(row = 1, column = i, padx = 5, pady = 5, sticky = 'nw')
            try:
                Su = self.If[i]
            except IndexError:
                Su = None
            self.frPlotSetup.append(clsAxSetup(fr, Info = Su))
            self.frPlotSetup[i].grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
            i +=1
        self.btnPlot = ttk.Button(self.frame, text = 'Plot Axes', command = lambda : self.PlotAxes())
        self.btnPlot.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.btnConfig = ttk.Button(self.frame, text = 'Configure Axes', command = lambda : self.ConfigAxes())
        self.btnConfig.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'nw')
        
    def PlotAxes(self, FigShow = True,*args, **kwargs):
        self.get()
        self.Fig = PlotSub(spType = self.Info["Figure Type"], spData = self.Info["Data"], spSetup = self.If)
        if FigShow == True:
            self.Fig.show()
    def ConfigAxes(self,con = None, *args, **kwargs):
        if self.Fig != None:
            self.Fig = None
        self.PlotAxes()
        plt.ion()
        self.frConfig = Tk()
        self.frConfig.geometry("1000x750")
        self.frConfig.title(self.title)
        sz = [900/(len(self.Axes)),650]
        self.frConfigLst = []   
        i = 0
        for t in self.Axes:
            self.frConfigLst.append(clsAxConfigDlg(self.frConfig,sz,t,ax = self.Fig.axes[i]))
            self.frConfigLst[i].grid(row = 0, column = i, padx = 5, pady = 5, sticky = 'nw')
            i += 1
        self.frConfig.mainloop() 
        
class clsPlotSetupTbDlg(ttk.Frame):# A class to handle data from excel workbook for DataTab   
    def __init__(self,parent, FigLayInfo = None, spInfo = None, Info = None, *args, **kwargs):
        global glWbkData
        global glFigTypes
        ttk.Frame.__init__(self,parent,*args, **kwargs)
        
        self.frSize =[max(parent.winfo_width(),1000),max(parent.winfo_height(),750)]
        #self.frData = []
        self.FigLayIf = FigLayInfo
        self.spIf = spInfo
        self.If = Info
        self.frPlotSetup = []  
        self.frMain = ttk.Frame(self)
        self.frMain.grid(row = 0, column = 0, sticky = 'nw')
        self.frSaveLoadInfo = clsSaveLoadInfoDlg(self,"3Su")
        self.frSaveLoadInfo.grid(row = 1, column = 0, padx= 5, pady = 5, sticky = 'nw')
        self.populate()
        
        """
        if self.FigLayIf != None:
            for i in range(self.FigLayIf[0]):
                for j in range(self.FigLayIf[1]):
                    try:
                        spIf = self.If[i*self.FigLayIf[1]+j]
                    except (NameError, TypeError, KeyError,IndexError) as e:
                        spIf = None
                    
                    SubPlotData = clsSubPlotExlDataTbDlg(self.frMain,
                                                         [(self.frSize[0]-20)/(self.FigLayIf[1]),
                                                          (self.frSize[1]-60)/(self.FigLayIf[0])-60], 
                                                          spLb = "Sub Plot " + str(i*self.FigLayIf[1]+j+1),
                                                          spInfo = spIf) #(self,parent,frSize,wbks,spLabel, *args, **kwargs)
                    SubPlotData.grid(row = i, column = j, padx = 5, pady = 5, sticky = 'nw')
                    self.frData.append(SubPlotData) 
                    
        """
                    
              
        
    def get(self, *args, **kwargs):
        self.If = []
        for fr in self.frPlotSetup:
            self.If.append(fr.get())
        """
        if self.frData != None:                      
            for fr in self.frData:
                self.If.append(fr.get())
        """
        return self.If
        
    def populate(self, *args, **kwargs):
        for wdg in self.frMain.winfo_children():
            wdg.destroy()
        if self.FigLayIf != None:
            for i in range(self.FigLayIf[0]):
                for j in range(self.FigLayIf[1]):
                    if self.If != None:
                        try:
                            spSu = self.If[i*self.FigLayIf[1]+j]
                        except IndexError:
                            spSu = None
                        try: 
                            spInf = self.spIf[i*self.FigLayIf[1]+j]
                        except IndexError:
                            spInf = {"Figure Type": 'Mono Axis', "Data" : [[]], "Data Load Setup" : [[]], "Data Source" : [[]]}
                        SubPlotSetup = clsSubPlotSetupTbDlg(self.frMain,
                                                      [(self.frSize[0]-20)/(self.FigLayIf[1]),
                                                          (self.frSize[1]-60)/(self.FigLayIf[0])-60], 
                                                      spLb = "Sub Plot " + str(i*self.FigLayIf[1]+j+1), 
                                                      spInfo = spInf,
                                                      spSetup = spSu)
                                                               
                        SubPlotSetup.grid(row = i, column = j, padx = 5, pady = 5, sticky = 'nw')
                        self.frPlotSetup.append(SubPlotSetup)
        """                        
        i = 0
        for fr in self.frData:
            try:
                fr.If = self.If[i]
                fr.populate()
            except (IndexError, NameError, TypeError, KeyError) as e:
                pass
            i += 1
        """
                
def PlotSub(spFig = None, spGs = None, spType = "Mono Axis", spData = [[[[0,1],[0,1]]]], spSetup = [dvfldPlotSetup]):
    if spType == "Mono Axis":
        spFig = MonoAxis(spData[0],spSetup[0], fig = spFig, gs = spGs)
    if spType == 'Double Axes':
        spFig = DoubleAxes(spData[0],spData[1],spSetup[0],spSetup[1], fig = spFig, gs = spGs)
    if spType == "Double Axes with an Inset":
        spFig = FigInset(spData[0],spData[1],spSetup[0],spSetup[1], fig = spFig, gs = spGs)
    if spType == "Triple Axes":
        spFig = TripleAxes(spData[0],spData[1],spData[2],spSetup[0],spSetup[1],spSetup[2], fig = spFig, gs = spGs)
    return spFig   
        
class clsAxConfigDlg(clsFrameWScrollBar):
    global dvOneAxisConfig
    def __init__(self, parent,  frSize, frTxt, ax = None, axInfo = None, axMLStyleInfo = None, *args, **kwargs):
        clsFrameWScrollBar.__init__(self,parent,frSize,*args, **kwargs)
        if axInfo == None:
            self.If = {}
        else:
            self.If = axInfo
        self.FigType = frTxt
        self.ax = ax
        self.axMLStyleIf = axMLStyleInfo
        self.frMain = ttk.Frame(self.frame)
        self.frMain.grid(row = 1, column = 0, sticky = 'nw')
        self.frSaveLoadInfo = clsSaveLoadInfoDlg(self,"2Config")
        self.frSaveLoadInfo.grid(row = 0, column = 0, padx= 5, pady = 5, sticky = 'nw')
        self.populate() 
        """
        lb = ttk.Label(self.frMain,text = self.FigType)
        lb.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            xIf = self.If["Scales"][0]["Scale"]
            yIf = self.If["Scales"][1]["Scale"]
        except KeyError:
            xIf = dvOneAxisConfig
            yIf = dvOneAxisConfig
        self.xScale = clsOneAxisConfigDlg(self.frMain, "X Scale", axInfo = xIf)
        self.xScale.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.yScale = clsOneAxisConfigDlg(self.frMain, "Y Scale",axInfo = yIf)
        self.yScale.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'nw')
        
        # A frame storing all operating buttons
        self.frOperBtns = ttk.Frame(self.frMain)
        self.frOperBtns.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        self.btnConfig = ttk.Button(self.frOperBtns, text='Configure',command=lambda : self.ConfigAx())
        self.btnConfig.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        self.btnPpl = ttk.Button(self.frOperBtns, text='Poputlate Label Text Boxes',command=lambda : self.populateLabel())
        self.btnPpl.grid(row = 0, column = 1,padx = 5, pady = 5, sticky = 'nw')
        
        # A frame storing line label frames
        self.frLnLbs = ttk.Frame(self.frMain)
        self.frLnLbs.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            lbIf = self.If["Add Label"]
        except KeyError:
            lbIf = None
        self.frAddLbDlg = clsAddLabelDlg(self.frLnLbs,[frTxt],lbInfo = lbIf)
        self.frAddLbDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing Marker and Line Style
        self.frMkNLn = ttk.Frame(self.frMain)
        self.frMkNLn.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            axLb = axMLStyleInfo["Line List"]
        except (TypeError,AttributeError) as e:
            axLb = None
        try:
            mkLnIf = axInfo["Marker and Line Style"]
            
        except (KeyError, TypeError, AttributeError) as e:
            mkLnIf = [0,axMLStyleInfo["Marker and Line Style List"]]
            
            
        self.frMkNLnDlg = clsAddMarkerNLineConfigDlg(self.frMkNLn, lstLabel = axLb, MarkerNLineInfo = mkLnIf)
        self.frMkNLnDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing an Add Text frame
        self.frAddTxt = ttk.Frame(self.frMain)
        self.frAddTxt.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            txtIf = self.If["Add Text"]
        except KeyError:
            txtIf = None
        self.frAddTxtDlg = clsAddTxtDlg(self.frAddTxt, txtInfo = txtIf)
        self.frAddTxtDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing an Add Arrow frame
        self.frAddArr = ttk.Frame(self.frMain)
        self.frAddArr.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            arrIf = self.If["Add Arrow"]
        except KeyError:
            arrIf = None
        self.frAddArrDlg = clsAddArrDlg(self.frAddArr, arrInfo = arrIf)
        self.frAddArrDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing an Add Ellipse frame
        self.frAddElp = ttk.Frame(self.frMain)
        self.frAddElp.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            elpIf = self.If["Add Ellipse"]
        except KeyError:
            elpIf = None
        self.frAddElpDlg = clsAddElpDlg(self.frAddElp, elpInfo = elpIf)
        self.frAddElpDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing an Axis Position frame
        self.frAxPos = ttk.Frame(self.frMain)
        self.frAxPos.grid(row = 8, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            posIf = self.If["Axis Position"]
        except KeyError:
            posIf = None    
        self.frAddAxPosDlg = clsAddAxPosDlg(self.frAxPos, frTxt = "Axis Position", axPosInfo = posIf)
        self.frAddAxPosDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        # A frame storing an Add Tick Label frame
        self.frAddRemoveTlb = ttk.Frame(self.frMain)
        self.frAddRemoveTlb.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            tlbIf = self.If["Remove Tick Labels"]
        except KeyError:
            tlbIf = None
        self.frRemoveTlbDlg = clsAddRemoveTickLabelDlg(self.frAddRemoveTlb, tlbInfo = tlbIf)
        self.frRemoveTlbDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        # A frame storing an Add Log Base frame
        self.frAddLogBase = ttk.Frame(self.frMain)
        self.frAddLogBase.grid(row = 10, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            lgbIf = self.If["Log Base"]
        except KeyError:
            lgbIf = None
        self.frLogBaseDlg = clsAddLogBaseDlg(self.frAddLogBase, lgbInfo = lgbIf)
        self.frLogBaseDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        """
    def populateLabel(self, *args, **kwargs):
        if self.frAddLbDlg.chbAddLbVar.get() == 1:
            self.frAddLbDlg.lstLb = []
            for fr in self.frAx:
                self.frAddLbDlg.lstLb.append(fr.lstLb)
            self.frAddLbDlg.UpdateTextBoxes()       
    def get(self, *args, **kwargs):
        self.If.clear()
        xScale = {"Scale" : self.xScale.getAxConfig(), "Sides" : "both"}
        yScale = {"Scale" : self.yScale.getAxConfig(), "Sides" : "both"}
        self.If["Scales"] = [xScale,yScale]
        self.If["Marker and Line Style"] = self.frMkNLnDlg.get()
        
        if self.frAddLbDlg.chbAddLbVar.get() == 1:
            self.If["Add Label"] = self.frAddLbDlg.get()#self.frAddLbDlg.tbxLstLb[0].getLgdIf()
        else:
            self.If["Add Label"] = None
        
        if self.frAddTxtDlg.chbAddTxtVar.get() == 1:
            self.If["Add Text"] = self.frAddTxtDlg.getTxtIf()
        else:
            self.If["Add Text"] = None    
        
        if self.frAddArrDlg.chbAddVar.get() == 1:
            self.If["Add Arrow"] = self.frAddArrDlg.get()
        else:
            self.If["Add Arrow"] = None
        
        if self.frAddElpDlg.chbAddVar.get() == 1:
            self.If["Add Ellipse"] = self.frAddElpDlg.get()
        else:
            self.If["Add Ellipse"] = None
            
        if self.frAddAxPosDlg.chbAddAxPosVar.get() == 1:
            self.If["Axis Position"] = self.frAddAxPosDlg.getAxPos()
        else:
            self.If["Axis Position"] = None
            
        if self.frRemoveTlbDlg.chbAddVar.get() == 1:
            self.If["Remove Tick Labels"] = self.frRemoveTlbDlg.get()
        else:
            self.If["Remove Tick Labels"] = None
            
        if self.frLogBaseDlg.chbAddVar.get() == 1:
            self.If["Log Base"] = self.frLogBaseDlg.get()
        else:
            self.If["Log Base"] = None
        
        if self.frPhotoDlg.chbAddVar.get() == 1:
            self.If["Photo"] = self.frPhotoDlg.get()
        else:
            self.If["Photo"] = None
        if self.frAddAnnDlg.chbAddVar.get() == 1:
            
            self.If["Add Annotation"] = self.frAddAnnDlg.get()
        else:
            self.If["Add Annotation"] = None
        
        return self.If
        
        
        
        
    def populate(self, *args, **kwargs):
        for wdg in self.frMain.winfo_children():
            wdg.destroy()
        lb = ttk.Label(self.frMain,text = self.FigType)
        lb.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            xIf = self.If["Scales"][0]["Scale"]
            yIf = self.If["Scales"][1]["Scale"]
        except KeyError:
            xIf = dvOneAxisConfig
            yIf = dvOneAxisConfig
        self.xScale = clsOneAxisConfigDlg(self.frMain, "X Scale", axInfo = xIf)
        self.xScale.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.yScale = clsOneAxisConfigDlg(self.frMain, "Y Scale",axInfo = yIf)
        self.yScale.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'nw')
        
        # A frame storing all operating buttons
        self.frOperBtns = ttk.Frame(self.frMain)
        self.frOperBtns.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        self.btnConfig = ttk.Button(self.frOperBtns, text='Configure',command=lambda : self.ConfigAx())
        self.btnConfig.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        self.btnPpl = ttk.Button(self.frOperBtns, text='Poputlate Label Text Boxes',command=lambda : self.populateLabel())
        self.btnPpl.grid(row = 0, column = 1,padx = 5, pady = 5, sticky = 'nw')
        
        # A frame storing line label frames
        self.frLnLbs = ttk.Frame(self.frMain)
        self.frLnLbs.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            lbIf = self.If["Add Label"]
        except KeyError:
            lbIf = None
        self.frAddLbDlg = clsAddLabelDlg(self.frLnLbs,[self.FigType],lbInfo = lbIf)
        self.frAddLbDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing Marker and Line Style
        self.frMkNLn = ttk.Frame(self.frMain)
        self.frMkNLn.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            axLb = self.axMLStyleIf["Line List"]
        except (TypeError,AttributeError) as e:
            axLb = None
        try:
            mkLnIf = self.If["Marker and Line Style"]
            
        except (KeyError, TypeError, AttributeError) as e:
            mkLnIf = [0,self.axMLStyleIf["Marker and Line Style List"]]
            
            
        self.frMkNLnDlg = clsAddMarkerNLineConfigDlg(self.frMkNLn, lstLabel = axLb, MarkerNLineInfo = mkLnIf)
        self.frMkNLnDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing an Add Text frame
        self.frAddTxt = ttk.Frame(self.frMain)
        self.frAddTxt.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            txtIf = self.If["Add Text"]
        except KeyError:
            txtIf = None
        self.frAddTxtDlg = clsAddTxtDlg(self.frAddTxt, txtInfo = txtIf)
        self.frAddTxtDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing an Add Arrow frame
        self.frAddArr = ttk.Frame(self.frMain)
        self.frAddArr.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            arrIf = self.If["Add Arrow"]
        except KeyError:
            arrIf = None
        self.frAddArrDlg = clsAddArrDlg(self.frAddArr, arrInfo = arrIf)
        self.frAddArrDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing an Add Ellipse frame
        self.frAddElp = ttk.Frame(self.frMain)
        self.frAddElp.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            elpIf = self.If["Add Ellipse"]
        except KeyError:
            elpIf = None
        self.frAddElpDlg = clsAddElpDlg(self.frAddElp, elpInfo = elpIf)
        self.frAddElpDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing an Axis Position frame
        self.frAxPos = ttk.Frame(self.frMain)
        self.frAxPos.grid(row = 8, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            posIf = self.If["Axis Position"]
        except KeyError:
            posIf = None    
        self.frAddAxPosDlg = clsAddAxPosDlg(self.frAxPos, frTxt = "Axis Position", axPosInfo = posIf)
        self.frAddAxPosDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        # A frame storing an Add Tick Label frame
        self.frAddRemoveTlb = ttk.Frame(self.frMain)
        self.frAddRemoveTlb.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            tlbIf = self.If["Remove Tick Labels"]
        except KeyError:
            tlbIf = None
        self.frRemoveTlbDlg = clsAddRemoveTickLabelDlg(self.frAddRemoveTlb, tlbInfo = tlbIf)
        self.frRemoveTlbDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        # A frame storing an Add Log Base frame
        self.frAddLogBase = ttk.Frame(self.frMain)
        self.frAddLogBase.grid(row = 10, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            lgbIf = self.If["Log Base"]
        except KeyError:
            lgbIf = None
        self.frLogBaseDlg = clsAddLogBaseDlg(self.frAddLogBase, lgbInfo = lgbIf)
        self.frLogBaseDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw') 
        
        # A frame storing an Add Photo frame
        self.frAddPhoto = ttk.Frame(self.frMain)
        self.frAddPhoto.grid(row = 11, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            phtIf = self.If["Photo"]
        except KeyError:
            phtIf = None
        self.frPhotoDlg = clsAddPhotoDlg(self.frAddPhoto, phtInfo = phtIf)
        self.frPhotoDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        # A frame storing an Add Arrow frame
        self.frAddAnn = ttk.Frame(self.frMain)
        self.frAddAnn.grid(row = 12, column = 0, padx = 5, pady = 5, sticky = 'nw')
        try:
            annIf = self.If["Add Annotation"]
        except KeyError:
            annIf = None
        self.frAddAnnDlg = clsAddAnnDlg(self.frAddAnn, annInfo = annIf)
        self.frAddAnnDlg.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
    def ConfigAx(self, *args, **kwargs):
        self.get()
        if self.ax != None:
            
            plt.ion()
            plt.figure(self.ax.figure.number)
            ConfigAx(self.ax,self.If)
            
            plt.show()
            plt.ioff() 
        
# A general class to add something on an axis
class clsAddDlg(ttk.Frame):
    def __init__(self,parent, cls,frLb, Info = None, btnPlusVisible = True, btnMinusVisible = True,  *args, **kwargs):      
        ttk.Frame.__init__(self,parent, *args, **kwargs)        
        self.If = Info
        self.Cls = cls
        self.btnPlusVis = btnPlusVisible
        self.btnMinusVis = btnMinusVisible
        #frame to store the Checkbox and Add Frame Button
        self.frStore = ttk.Frame(self)
        self.frStore.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.chbAddVar = tk.IntVar(master = parent)
        self.chbAdd = ttk.Checkbutton(self.frStore,text = frLb, variable = self.chbAddVar, command = lambda: self.Add())
        self.chbAdd.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.frLst = []
        self.frNum = 0
        try:
            self.chbAddVar.set(self.If[0])
            if self.chbAddVar.get() == 1:
                self.Add()
        except TypeError:
            self.chbAddVar.set(0)
    def Add(self, *args, **kwargs):
        if self.chbAddVar.get() == 1:
            self.btnAddFrame = ttk.Button(self.frStore, text = "+", width = 3, command = lambda: self.AddFrame())
            if self.btnPlusVis:
                self.btnAddFrame.grid(row=0,column=1, padx = 5, pady = 5, sticky = 'nw')
            self.btnRemoveFrame = ttk.Button(self.frStore, text = "-", width = 3, command = lambda: self.RemoveFrame())
            if self.btnMinusVis:
                self.btnRemoveFrame.grid(row=0,column=2, padx = 5, pady = 5, sticky = 'nw')
            try:
                self.frNum = len(self.If[1])
                for i in range(self.frNum):
                    fr = self.Cls(self,frTxt = str(i+1), Info = self.If[1][i])
                    fr.grid(row=i+1,column=0, padx = 5, pady = 5, sticky = 'nw')
                    self.frLst.append(fr)
            except (IndexError,TypeError) as e:
                self.frNum += 1
                fr = self.Cls(self,frTxt = str(1), Info = None)
                fr.grid(row=1,column=0, padx = 5, pady = 5, sticky = 'nw')
                self.frLst.append(fr)
        else:
            self.btnAddFrame.destroy()
            self.btnRemoveFrame.destroy()
            for fr in self.frLst:
                fr.destroy()
            self.frLst = []
            self.frNum = 0
    def AddFrame(self, *args, **kwargs):
        self.frNum += 1
        fr = self.Cls(self,frTxt = str(self.frNum), Info = None)
        fr.grid(row=self.frNum,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.frLst.append(fr)
    def RemoveFrame(self, *args, **kwargs):
        if self.frNum > 1:
            self.frNum -= 1
            self.frLst[self.frNum].destroy()
            self.frLst = self.frLst[:self.frNum]
    def get(self, *args, **kwargs):
        self.If = [self.chbAddVar.get(),[]]
        for fr in self.frLst:
            self.If[1].append(fr.get())
        return self.If
    def populate(self, *args, **kwargs):
        curFrNum = self.frNum
        if len(self.If[1]) > curFrNum:
            for i in range(curFrNum,len(self.If[1])):
                self.AddFrame()
        else:
            for i in range (len(self.If[1]),curFrNum):
                self.RemoveFrame()
        Temp = self.If[1]
        i = 0
        for fr in self.frLst:
            fr.If = Temp[i]
            try:
                fr.setInfo()
            except:
                pass

        
global glDctArrow
glDctArrow = {"entries":{"fields" : ["Position", "Width", "Face Color","Edge Color"],"default values" : ["[0.5,0.5,0.1,0]", "0.01","Black", "None"]}}
class clsArrDlg(ttk.Frame):
    global glDctArrow
    def __init__(self,parent, frTxt = "", Info = None,  *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        lb = ttk.Label(self, text="Arrow " + frTxt)
        lb.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.fr = clsMakeFrame(self,glDctArrow)
        self.fr.grid(row=1,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.If = Info
        self.fr.If = self.If
        self.fr.setInfo()
    def get(self,  *args, **kwargs):
        self.If = self.fr.get()
        #self.If[0] = StrToInsetLctTup(self.If[0])
        #self.If[1] = float(self.If[1])
        return self.If
    

global glDctEllipse
glDctEllipse = {"entries":{"fields" : ["Position","Width", "Height", "Face Color","Edge Color"],"default values" : ["[0.5,0.5]",0.15,0.3,"None", "Black"]}}        
class clsElpDlg(ttk.Frame):
    global glDctEllipse
    def __init__(self,parent, frTxt = "", Info = None,  *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        lb = ttk.Label(self, text="Ellipse " + frTxt)
        lb.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.fr = clsMakeFrame(self,glDctEllipse)
        self.fr.grid(row=1,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.If = Info
        self.fr.If = self.If
        self.fr.setInfo()
    def get(self,  *args, **kwargs):
        self.If = self.fr.get()
        return self.If
global glDctTickLabel
glDctTickLabel = {"comboboxes":{"fields":["X Axis All", "Y Axis All"],
                                "default values":[["Not Remove","Remove"], ["Not Remove","Remove"]]},
                    "entries":{"fields":["X Axis Remove Specified Indices","Y Axis Remove Specified Indices"], "default values":["",""]}                    
                    }
class clsRemoveTickLabelDlg(ttk.Frame):
    global glDctTickLabel
    def __init__(self,parent, frTxt = "", Info = None,  *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        lb = ttk.Label(self, text="Tick Label " + frTxt)
        lb.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.fr = clsMakeFrame(self,glDctTickLabel)
        self.fr.grid(row=1,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.If = Info
        self.fr.If = self.If
        self.fr.setInfo()
    def get(self,  *args, **kwargs):
        self.If = self.fr.get()
        return self.If
global glDctLogBase
glDctLogBase = {"comboboxes":{"fields":["Axis"],
                                "default values":[["X","Y"]]},
                "entries": {"fields": ["Base"],"default values":["10"]}}
class clsLogBaseDlg(ttk.Frame):
    global glDctLogBase
    def __init__(self,parent, frTxt = "", Info = None,  *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        lb = ttk.Label(self, text="Log Base " + frTxt)
        lb.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.fr = clsMakeFrame(self,glDctLogBase)
        self.fr.grid(row=1,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.If = Info
        self.fr.If = self.If
        self.fr.setInfo()
    def get(self,  *args, **kwargs):
        self.If = self.fr.get()
        return self.If
    def populate(self,  *args, **kwargs):
        self.fr.setInfo()

global glDctPhoto
glDctPhoto = {"comboboxes":{"fields":["Arrow Type", "Arrow Connection Type"],
                            "default values":[["->","<-","<->","-|>","<|-","<|-|>","]-["],["angle","angle3","arc","arc3","bar"]]},
              "entries":{"fields" : ["Zoom", "XY Data Point", "XY Photo Box","Arrow Line Width", "Arrow Color"],"default values" : ["1", "1,1","50.0,50.0","20","blue"]}
              }
class clsPhotoDlg(ttk.Frame):
    global glDctPhoto
    def opnPhoto(self,*args, **kwargs):
        try:
            FileName = filedialog.askopenfilename(defaultextension = ".tif",
                                                        filetypes=[("Tagged Image File Format *.tif *.tiff","*.tif *.tiff"),
                                                                   ("Encapsulated Postscript *.eps","*.eps"),
                                                                   ("Joint Photographic Experts Group *.jpg","*.jpg"),
                                                                   #("PGF code for LaText *.pgf","*.pgf"),
                                                                   #("Portable Document Format *.pdf", "*.pdf"),
                                                                   ("Portable Network Graphics *.png", "*.png"),
                                                                   #("Postscript *.ps", "*.ps"),
                                                                   ("Bitmap *.bmp", "*.bmp"),
                                                                   #("Scalable Vector Graphics *.svg *.svgz", "*.svg *.svgz"),
                                                                   ("All files *.*","*.*")],
                                                        parent = self,
                                                        title = "Open Image")
        except FileNotFoundError:
            pass
        self.entPhoto.delete(0,'end')
        self.entPhoto.insert(0,FileName)
        try:
            self.phtPath = FileName
        finally:
            pass
        try:
            self.Photo = Image.open(FileName)
        except:
            self.Photo = None
    def __init__(self,parent, frTxt = "", Info = None,  *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        
        self.frPhoto = ttk.Frame(self)
        self.frPhoto.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.entPhoto = ttk.Entry(self.frPhoto)
        self.entPhoto.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.entPhoto.insert(0,"")
        self.btnPhoto = ttk.Button(self.frPhoto,text = "Open Photo",command = lambda: self.opnPhoto())
        self.btnPhoto.grid(row=0,column=1, padx = 5, pady = 5, sticky = 'nw') 
        self.frPhotoConfig = clsMakeFrame(self,glDctPhoto)
        self.frPhotoConfig.grid(row=1,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.If = Info
        try:
            self.Photo = self.If[0]
            self.phtPath = self.If[1]
            self.frPhotoConfig.If = self.If[2]
        except (AttributeError,KeyError,IndexError,TypeError):
            self.Photo = None
            self.phtPath = None
            self.frPhotoConfig.If = None
        self.populate()
    def get(self,  *args, **kwargs):
        self.If = [self.Photo,self.phtPath,self.frPhotoConfig.get()]
        return self.If
    def populate(self,  *args, **kwargs):
        try:
            self.entPhoto.insert(0,self.phtPath)
        except:
            pass
        self.frPhotoConfig.setInfo()

global glDctSpLayout
glDctSpLayout = {"entries":{"fields" : ["Bottom","Top" , "Left","Right", "Horizontal Space", "Vertical Space" ],
                         "default values" : ["Not Change", "Not Change","Not Change","Not Change","0","0"]
                         }
              }
class clsSpLayoutDlg(ttk.Frame):
    global glDctSpLayout
    def __init__(self,parent, frTxt = "", Info = None,  *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        lb = ttk.Label(self, text="Suplot Layout " + frTxt)
        lb.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.fr = clsMakeFrame(self,glDctSpLayout)
        self.fr.grid(row=1,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.If = Info
        self.fr.If = self.If
        self.fr.setInfo()
    def get(self,  *args, **kwargs):
        self.If = self.fr.get()
        return self.If
    def populate(self,  *args, **kwargs):
        self.fr.setInfo()
global glDctAnnotation
glDctAnnotation = {"entries":{"fields" : ["Text", "Text Size","Text Color", "Annotated Point Coordinate", "Text Coordinate",
                                          "Arrow Color", "Arrow Width","Arrow Head Width","Shrink",
                                          "Horizontal Alignment", "Vertical Alignmet"],
                              "default values" : ["Annotation Text", "20","black", "(1,1)","(2,1)", "Black","0.01","0","0.001","left","bottom"]}}
class clsAnnDlg(ttk.Frame):
    global glDctAnnotation
    def __init__(self,parent, frTxt = "", Info = None,  *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        lb = ttk.Label(self, text="Annotation " + frTxt)
        lb.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.fr = clsMakeFrame(self,glDctAnnotation)
        self.fr.grid(row=1,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.If = Info
        self.fr.If = self.If
        self.fr.setInfo()
    def get(self,  *args, **kwargs):
        self.If = self.fr.get()
        return self.If
    
class clsAddArrDlg(clsAddDlg):
    def __init__(self,parent, arrInfo = None,  *args, **kwargs):      
        clsAddDlg.__init__(self,parent, clsArrDlg, "Add Arrow", Info = arrInfo, *args, **kwargs)
class clsAddElpDlg(clsAddDlg):
    def __init__(self,parent, elpInfo = None,  *args, **kwargs):      
        clsAddDlg.__init__(self,parent, clsElpDlg, "Add Ellipse", Info = elpInfo, *args, **kwargs)
class clsAddRemoveTickLabelDlg(clsAddDlg):
    def __init__(self,parent, tlbInfo = None,  *args, **kwargs):      
        clsAddDlg.__init__(self,parent, clsRemoveTickLabelDlg, "Remove Major Tick Label", Info = tlbInfo, btnPlusVisible = False, btnMinusVisible = False, *args, **kwargs)
class clsAddLogBaseDlg(clsAddDlg):
    def __init__(self,parent, lgbInfo = None,  *args, **kwargs):      
        clsAddDlg.__init__(self,parent, clsLogBaseDlg, "Logarithm Base", Info = lgbInfo, btnPlusVisible = True, btnMinusVisible = True, *args, **kwargs)
class clsAddPhotoDlg(clsAddDlg):
    def __init__(self,parent, phtInfo = None,  *args, **kwargs):      
        clsAddDlg.__init__(self,parent, clsPhotoDlg, "Add Photo", Info = phtInfo, btnPlusVisible = True, btnMinusVisible = True, *args, **kwargs)
class clsAddSpLayoutDlg(clsAddDlg):
    def __init__(self,parent, SpLayoutInfo = None,  *args, **kwargs):      
        clsAddDlg.__init__(self,parent, clsSpLayoutDlg, "Subplot Layout", Info = SpLayoutInfo, btnPlusVisible = True, btnMinusVisible = True, *args, **kwargs)



class clsAddAxPosDlg(ttk.Frame):
    def __init__(self,parent, frTxt = None, axPosInfo = None,  *args, **kwargs):      
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        
        self.AxPosIf = axPosInfo
        self.chbAddAxPosVar = tk.IntVar(master = parent)
        try:
            self.chbAddAxPos = ttk.Checkbutton(self,text = frTxt,variable = self.chbAddAxPosVar, command = lambda: self.AddAxPos())
        except ValueError:
            self.chbAddAxPos = ttk.Checkbutton(self,text = "Axis Position",variable = self.chbAddAxPosVar, command = lambda: self.AddAxPos())
        self.chbAddAxPos.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        try:
            self.chbAddAxPosVar.set(self.AxPosIf[0])
            if self.chbAddAxPosVar.get() == 1:
                self.AddAxPos()
        except TypeError:
            self.chbAddAxPosVar.set(0)
    def AddAxPos(self):
        global glAxPos
        if self.chbAddAxPosVar.get() == 1:
            dct = {"entries": {"fields":["Axis Position", "Bottom Spine", "Left Spine", "Top Spine", "Right Spine"], "default values": None}}
            try:
                dct["entries"]["default values"] = self.AxPosIf[1]
            except TypeError:
                dct["entries"]["default values"] = [str([0,0,1,1]),0,0,1,1]
            self.frAxPos = clsMakeFrame(self,dct)
            self.frAxPos.grid(row = 0, column = 1, padx = 5, pady = 5,sticky = 'nw')
        else:
            #self.AxPosIf.clear()
            self.frAxPos.destroy()
    def getAxPos(self):
        self.AxPosIf = [self.chbAddAxPosVar.get(),self.frAxPos.get()]
        #self.AxPosIf[1][0] = StrToInsetLctTup(self.AxPosIf[1][0])
        #for i in range(1,len(self.AxPosIf)):
            #self.AxPosIf[1][i] = float(self.AxPosIf[1][i])
        return self.AxPosIf

class clsAddAnnDlg(clsAddDlg):
    def __init__(self,parent, annInfo = None,  *args, **kwargs):      
        clsAddDlg.__init__(self,parent, clsAnnDlg, "Add Annotation", Info = annInfo, *args, **kwargs)

class clsMarkerStyleDlg(ttk.Frame):
    global glDctMarker 
    def __init__(self,parent, MarkerStyleInfo = None,  *args, **kwargs):      
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        
        try:
            self.MarkerStyleIf = map(str,MarkerStyleInfo)
            
        except (TypeError,ValueError) as e:
            self.MarkerStyleIf = ["None", "6", "Black", "None", "1"]
        self.frMarkerStyle = clsMakeFrame(self,glDctMarker)
        self.frMarkerStyle.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.setInfo()
    def setInfo(self,*args,**kwargs):
        self.frMarkerStyle.If = self.MarkerStyleIf
        self.frMarkerStyle.setInfo()
        
    def get(self,*args,**kwargs):
        self.MarkerStyleIf = []
        self.MarkerStyleIf = self.frMarkerStyle.get()
        #self.MarkerStyleIf[1] = float(self.MarkerStyleIf[1])
        #self.MarkerStyleIf[4] = float(self.MarkerStyleIf[4])
        return self.MarkerStyleIf
        
    
class clsLineStyleDlg(ttk.Frame):
    global glDctLineStyle 
    def __init__(self,parent, LineStyleInfo = None,  *args, **kwargs):      
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        try:
            self.LineStyleIf = map(str,LineStyleInfo)
        except (TypeError,ValueError) as e:
            self.LineStyleInf = ["solid", "Default", "Black", "1.5"]
        self.LineStyleIf = LineStyleInfo
        self.frLineStyle = clsMakeFrame(self,glDctLineStyle)
        self.frLineStyle.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        self.setInfo()
        
    def setInfo(self,*args,**kwargs):
        self.frLineStyle.If = self.LineStyleIf
        self.frLineStyle.setInfo()
    def get(self,*args,**kwargs):
        self.LineStyleIf = []
        self.LineStyleIf = self.frLineStyle.get()
        #self.LineStyleIf[3] = float(self.LineStyleIf[3])
        return self.LineStyleIf
        
class clsMarkerNLineStyleDlg(ttk.Frame):
    global glDefaultFont
    def __init__(self,parent, MarkerNLineStyleInfo = None,  *args, **kwargs):      
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        try:
            self.MarkerNLineStyleIf = {"Marker Style": MarkerNLineStyleInfo["Marker Style"],
                                  "Line Style": MarkerNLineStyleInfo["Line Style"]}
        except TypeError:
            self.MarkerNLineStyleIf = {"Marker Style": None,
                                  "Line Style": None}
        lb = ttk.Label(self, text = "Marker", font = "Bold")
        lb.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.frMarkerStyle = clsMarkerStyleDlg(self, MarkerStyleInfo = self.MarkerNLineStyleIf["Marker Style"])
        self.frMarkerStyle.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
        lb = ttk.Label(self, text = "Line", font = "Bold")
        lb.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.frLineStyle = clsLineStyleDlg(self, LineStyleInfo = self.MarkerNLineStyleIf["Line Style"])
        self.frLineStyle.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.setInfo()
    def setInfo(self,*args,**kwargs):
        self.frMarkerStyle.MarkerStyleIf = self.MarkerNLineStyleIf["Marker Style"]
        self.frMarkerStyle.setInfo()
        self.frLineStyle.LineStyleIf = self.MarkerNLineStyleIf["Line Style"]
        self.frLineStyle.setInfo()
    def get(self,*args,**kwargs):
        self.MarkerNLineStyleIf["Marker Style"] = self.frMarkerStyle.get()
        self.MarkerNLineStyleIf["Line Style"] = self.frLineStyle.get()
        return self.MarkerNLineStyleIf
class clsAddMarkerNLineConfigDlg(ttk.Frame):# A class to handle marker and line styles of a line
    def __init__(self,parent,lstLabel = None, MarkerNLineInfo = None , *args, **kwargs):
        ttk.Frame.__init__(self,parent,*args, **kwargs)
        self.lstLb = lstLabel
        self.MarkerNLineIf = MarkerNLineInfo
        self.chbMarkerNLineConfigVar = tk.IntVar(master = parent)
        self.chbMarkerNLineConfig = ttk.Checkbutton(self,text = "Line and Marker Config", variable = self.chbMarkerNLineConfigVar, command = lambda: self.populate())
        self.chbMarkerNLineConfig.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')                
        try:
            self.chbMarkerNLineConfigVar.set(self.MarkerNLineIf[0])
        except TypeError as e:
            self.chbMarkerNLineConfigVar.set(0)
        self.cbblstLbVar = tk.StringVar(master = parent)
        self.frMarkerNLine = []
        self.populate()

    def populate(self,*args,**kwargs):
        if self.chbMarkerNLineConfigVar.get() == 1:
            self.lbLine = ttk.Label(self, text = "Lines")
            self.lbLine.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
            self.cbbLstLb = ttk.Combobox(self, textvariable = self.cbblstLbVar)
            self.cbbLstLb.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'nw')
            self.cbbLstLb.bind('<<ComboboxSelected>>', lambda x = self: self.UpdateMarkerNLineStyle(x))
            try:
                self.cbbLstLb["values"] = self.lstLb
                self.cbbLstLb.set(self.lstLb[0])
            except (TypeError,IndexError) as e:
                self.cbbLstLb["values"] = []
                self.cbbLstLb.set("")
            if len(self.lstLb) == 0:
                fr = clsMarkerNLineStyleDlg(self,MarkerNLineStyleInfo = None)
                fr.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = 'nw')
                self.frMarkerNLine.append(fr)
            else:    
                for i in range(len(self.lstLb)):    
                    try:
                        Stl = self.MarkerNLineIf[1][i]
                    except (TypeError,IndexError) as e:
                        Stl = {"Marker Style" : None,
                               "Line Style" : None}
                    
                    fr = clsMarkerNLineStyleDlg(self,MarkerNLineStyleInfo = Stl)
                    fr.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = 'nw')
                    self.frMarkerNLine.append(fr)
                    self.frMarkerNLine[i].grid_remove()
                self.frMarkerNLine[0].grid()
        else:
            try:
                self.lbLine.destroy()
                self.cbbLstLb.destroy()
                for fr in self.frMarkerNLine:
                    fr.destroy()
            except (AttributeError,TypeError):
                pass
    def UpdateMarkerNLineStyle(self,*args,**kwargs):
        i = self.cbbLstLb.current()
        for fr in self.frMarkerNLine:
            fr.grid_remove()
        self.frMarkerNLine[i].grid()
        
    def get(self,*args,**kwargs):
        self.MarkerNLineIf = [self.chbMarkerNLineConfigVar.get(), None]
        if self.chbMarkerNLineConfigVar.get() == 1:
            if  len(self.cbbLstLb["values"]) > 0:
                self.MarkerNLineIf[1] = []
                j = self.cbbLstLb.current()
                i = 0
                for fr in self.frMarkerNLine:
                    try:
                        fr.grid()
                    finally:
                        pass
                    try:
                        self.MarkerNLineIf[1][i] = fr.get()
                    except IndexError:
                        self.MarkerNLineIf[1].append(fr.get())
                    fr.grid_remove()
                    i += 1
                self.frMarkerNLine[j].grid()
        
        return self.MarkerNLineIf
    
dctMarkerStyleToStyleName = dict(zip(glMarkerStyles,glMarkerStyleNames))
dctMarkerStyleNameToStyle = dict(zip(glMarkerStyleNames,glMarkerStyles))
dctLineStyleToStyleName = dict(zip(glLineStyles,glLineStyleNames))
dctLineStyleNameToStyle = dict(zip(glLineStyleNames,glLineStyles))
def IsErrBarLine(ln):
    stl = ln.get_marker()
    if stl == "_" or stl == "|":
        return True
    else:
        return False
def getMarkerNLineStyle(ln):
    if not IsErrBarLine():
        try:
            stl = ln.get_marker()
        except KeyError:
            if stl == None:
                stl = "None"        
        MarkerStyle = [stl, ln.get_markersize(), ln.get_markerfacecolor(), ln.get_markeredgecolor(), ln.get_markeredgewidth()]
        try:
            stl = dctLineStyleToStyleName[ln.get_linestyle()]
        except KeyError:
            if stl == None:
                stl = "None"
        LineStyle = [stl,ln.get_drawstyle(),ln.get_color(),ln.get_linewidth()]
        return {"Marker Style" : MarkerStyle, "Line Style" : LineStyle}
    else:
        return None
    
def setMarkerNLineStyle(ln,mkLnIf):
    if not IsErrBarLine(ln):
        ln.set_marker(dctMarkerStyleNameToStyle[mkLnIf["Marker Style"][0]])
        ln.set_markersize(mkLnIf["Marker Style"][1])
        ln.set_markerfacecolor(mkLnIf["Marker Style"][2])
        ln.set_markeredgecolor(mkLnIf["Marker Style"][3])
        ln.set_markeredgewidth(mkLnIf["Marker Style"][4])
        ln.set_linestyle(dctLineStyleNameToStyle[mkLnIf["Line Style"][0]])
        #ln.set_linestyle((0, (5, 10)))
        ln.set_drawstyle(mkLnIf["Line Style"][1])
        ln.set_color(mkLnIf["Line Style"][2])
        ln.set_linewidth(mkLnIf["Line Style"][3])
    


def ConFigXYScale(ax,xScale,yScale):
    ConFigXScale(ax,xScale["Scale"],tb = xScale["Sides"]) # xScale example = {"Scale":dvOneAxisConfig,"Sides": "both"}
    ConFigYScale(ax,yScale["Scale"],lr = yScale["Sides"]) # yScale example = {"Scale":dvOneAxisConfig,"Sides": "both"}
#Configure an axis with parameters such as Min, Max, Multiple Locator, Minor Locator, and color, add Text, add Labels
def ConfigAx(ax,axIf):
    """
    axIf example = {"Scales":[xScale,yScale],
                    "Add Label": [1,["Label 1"],"0", str(glTextFs)],
                    "Add Text": [1,[["Insert Text in the Axis", [0.95,0.01],glTextFs,"green"]]],
                    "Axis Position": [1,[[0.2,0.3,0.4,0.5],0,0,1,1]]}
    """
    
    plt.ion()
   
    
    ConFigXYScale(ax,axIf["Scales"][0],axIf["Scales"][1])
    
    
    if axIf["Marker and Line Style"] != None:
       
        try:
            if axIf["Marker and Line Style"][0] == True:
                i = 0
                for ln in ax.get_lines():
                    if not IsErrBarLine(ln):
                        setMarkerNLineStyle(ln,axIf["Marker and Line Style"][1][i])
                        i += 1
                    
                    else:
                        if axIf["Marker and Line Style"][1][i-1]["Marker Style"][2] != "None":
                            ln.set_markerfacecolor(axIf["Marker and Line Style"][1][i-1]["Marker Style"][2])
                        if axIf["Marker and Line Style"][1][i-1]["Marker Style"][3] != "None":
                            ln.set_markeredgecolor(axIf["Marker and Line Style"][1][i-1]["Marker Style"][3])
                        
                   
        except (TypeError, KeyError, IndexError, AttributeError):#(KeyError,IndexError) as e (TypeError, KeyError, IndexError, AttributeError)
            pass
            tk.messagebox.showwarning('Marker and Line Style is in wrong format','Please, refill Marker and Line Style') 
            
    if axIf["Axis Position"] != None:
        try:
            if axIf["Axis Position"][0] == True:
                pos = StrToInsetLctTup(axIf["Axis Position"][1][0])
                if pos != [0,0,1,1]:
                    ax.set_position(pos)
                if axIf["Axis Position"][1][1] != 0:
                    ax.spines["bottom"].set_position(("axes", float(axIf["Axis Position"][1][1])))
                if axIf["Axis Position"][1][2] != 0:
                    ax.spines["left"].set_position(("axes", float(axIf["Axis Position"][1][2])))
                if axIf["Axis Position"][1][3] != 1:
                    ax.spines["top"].set_position(("axes", float(axIf["Axis Position"][1][3])))
                if axIf["Axis Position"][1][4] != 1:
                    ax.spines["right"].set_position(("axes", float(axIf["Axis Position"][1][4])))
        except (TypeError, KeyError, IndexError, AttributeError):
            pass
            tk.messagebox.showwarning('Axis Position is in wrong format','Please, refill Axis Position') 
    if axIf["Add Label"] != None:
        try:
            if axIf["Add Label"][0] == True:
                i = 0
                NormalLines = []
                for ln in ax.get_lines():
                    if not IsErrBarLine(ln):
                        try:
                            ln.set_label(axIf["Add Label"][1][0][i])
                        except (TypeError, KeyError, IndexError, AttributeError):
                            ln.set_label("line "+str(i))
                        NormalLines.append(ln)
                        i += 1
                ax.legend([ln for ln in NormalLines],
                           [ln.get_label() for ln in NormalLines],
                           loc = StrToLctTup(axIf["Add Label"][1][1]), 
                           fontsize = int(axIf["Add Label"][1][2]))  
        except (TypeError, KeyError, IndexError, AttributeError):
            pass
            tk.messagebox.showwarning('Add Label is in wrong format','Please, refill Add Label') 
        
    if axIf["Add Text"] != None:
        
        try:
            if axIf["Add Text"][0] == True:
                for i in range(len(axIf["Add Text"][1])):
                    pos = StrToInsetLctTup(axIf["Add Text"][1][i][1])
                    ax.text(pos[0],pos[1], 
                            axIf["Add Text"][1][i][0],
                            verticalalignment = 'bottom', horizontalalignment = 'left',
                            transform = ax.transAxes,
                            color = axIf["Add Text"][1][i][3], 
                            fontsize = int(axIf["Add Text"][1][i][2]))
        except (TypeError, KeyError, IndexError, AttributeError):
            pass
            tk.messagebox.showwarning('Add Text Info is in wrong format','Please, refill Add Text')     
    if axIf["Add Arrow"] != None:
        try:
            if axIf["Add Arrow"][0] == True:
                for i in range(len(axIf["Add Arrow"][1])):
                    pos = StrToInsetLctTup(axIf["Add Arrow"][1][i][0]) 
                    ax.arrow(pos[0],pos[1], pos[2],pos[3],
                            #verticalalignment = 'bottom', horizontalalignment = 'right',
                            transform = ax.transAxes,
                            width = float(axIf["Add Arrow"][1][i][1]),
                            facecolor = axIf["Add Arrow"][1][i][2], 
                            edgecolor = axIf["Add Arrow"][1][i][3])
                    
        except (TypeError, KeyError, IndexError, AttributeError):
            pass
            tk.messagebox.showwarning('Add Arrow Info is in wrong format','Please, refill Add Arrow') 
    if axIf["Add Ellipse"] != None:
        try:
            if axIf["Add Ellipse"][0] == True:
                for i in range(len(axIf["Add Ellipse"][1])):
                    pos = StrToInsetLctTup(axIf["Add Ellipse"][1][i][0])
                    e = Ellipse(pos, float(axIf["Add Ellipse"][1][i][1]), float(axIf["Add Ellipse"][1][i][2]),
                                facecolor = axIf["Add Ellipse"][1][i][3], 
                                edgecolor = axIf["Add Ellipse"][1][i][4])                   
                    e.set_clip_box(ax.bbox)
                    #e.set_alpha(0.1)
                    e.set_transform(ax.transAxes)
                    ax.add_artist(e)    
        except (TypeError, KeyError, IndexError, AttributeError):
            pass
            tk.messagebox.showwarning('Add Ellipse Info is in wrong format','Please, refill Add Ellipse') 
    try:        
        if axIf["Remove Tick Labels"] != None:
            try:
                if axIf["Remove Tick Labels"][0] == True:
                    if axIf["Remove Tick Labels"][1][0][0] == "Remove":
                        ax.set_xticklabels([])
                    else:
                        if axIf["Remove Tick Labels"][1][0][2]!= "":
                            xticks = ax.xaxis.get_major_ticks()
                            for i in StrToInsetLctTup(axIf["Remove Tick Labels"][1][0][2]):
                                xticks[int(i)].label1.set_visible(False)
                    if axIf["Remove Tick Labels"][1][0][1] == "Remove":
                        ax.set_yticklabels([])
                    else:
                        if axIf["Remove Tick Labels"][1][0][3]!= "":
                            yticks = ax.yaxis.get_major_ticks()
                            for i in StrToInsetLctTup(axIf["Remove Tick Labels"][1][0][3]):
                                yticks[int(i)].label1.set_visible(False)
            except (TypeError, KeyError, IndexError, AttributeError):
                pass
                tk.messagebox.showwarning('Remove Tick Labels entry is in wrong format','Please, refill Remove Tick Labels entry') 
    except KeyError:
        pass
        tk.messagebox.showwarning('Remove Tick Labels entry has not been added to Config Info','Please, do Config All, Save Data and Try Again')
    try:
        if axIf["Photo"] != None:
            if axIf["Photo"][0] == True:
                for i in range(len(axIf["Photo"][1])):
                    
                    Photo = Image.open(axIf["Photo"][1][i][1])#axIf["Photo"][1][i][0]
                    # We need a float array between 0-1, rather than
                    # a uint8 array between 0-255
                    Photo = np.array(Photo).astype(np.float) / 255
                    phtBox = OffsetImage(Photo, zoom=float(axIf["Photo"][1][i][2][2]))#float(axIf["Photo"][1][i][2][2])
                    
                    
                    phtBox.image.axes = ax
                    XYAnnoPoint = StrToLctTup(axIf["Photo"][1][i][2][3])# axIf["Photo"][1][i][2][4]
                    PhotoAnno = AnnotationBbox(phtBox,XYAnnoPoint,
                                               xybox= StrToLctTup(axIf["Photo"][1][i][2][4]),
                                               xycoords="data",
                                               boxcoords="offset points",
                                               #pad=0.5,
                                               arrowprops=dict(arrowstyle=axIf["Photo"][1][i][2][0],
                                                               linewidth = float(axIf["Photo"][1][i][2][5]),
                                                               color = axIf["Photo"][1][i][2][6],
                                                               ),
                                                               
                                               )
                    ax.add_artist(PhotoAnno)
    except KeyError:
        pass
    
    try:
                
        if axIf["Add Annotation"] != None:
            try:
                if axIf["Add Annotation"][0] == True:
                    for i in range(len(axIf["Add Annotation"][1])): 
                        ax.annotate(axIf["Add Annotation"][1][i][0],
                                    size = float(axIf["Add Annotation"][1][i][1]), 
                                    color = axIf["Add Annotation"][1][i][2], 
                                    xy=StrToInsetLctTup(axIf["Add Annotation"][1][i][3]), 
                                    xytext=StrToInsetLctTup(axIf["Add Annotation"][1][i][4]),
                                    horizontalalignment =axIf["Add Annotation"][1][i][9] ,
                                    verticalalignment = axIf["Add Annotation"][1][i][10],
                                    arrowprops=dict(edgecolor=axIf["Add Annotation"][1][i][5], 
                                                    width = float(axIf["Add Annotation"][1][i][6]), 
                                                    headwidth = float(axIf["Add Annotation"][1][i][7]), 
                                                    shrink=float(axIf["Add Annotation"][1][i][8]))
                                    )
                        
                        """
                        
                        xypos = StrToInsetLctTup(axIf["Add Arrow"][1][i][0]) 
                        ax.arrow(pos[0],pos[1], pos[2],pos[3],
                                #verticalalignment = 'bottom', horizontalalignment = 'right',
                                transform = ax.transAxes,
                                width = float(axIf["Add Arrow"][1][i][1]),
                                facecolor = axIf["Add Arrow"][1][i][2], 
                                edgecolor = axIf["Add Arrow"][1][i][3])
                        """
                    
            except (TypeError, KeyError, IndexError, AttributeError):
                pass
                tk.messagebox.showwarning('Add Annotation Info is in wrong format','Please, refill Add Annotation')  
    except KeyError:
        pass
        tk.messagebox.showwarning('Add Annotation entry has not been added to Config Info','Please, do Config All, Save Data and Try Again')
    """
    if axIf["Add Annotation"] != None:
        try:
            if axIf["Add Annotation"][0] == True:
                for i in range(len(axIf["Add Annotation"][1])):
                    
                    
                    xypos = StrToInsetLctTup(axIf["Add Arrow"][1][i][0]) 
                    ax.arrow(pos[0],pos[1], pos[2],pos[3],
                            #verticalalignment = 'bottom', horizontalalignment = 'right',
                            transform = ax.transAxes,
                            width = float(axIf["Add Arrow"][1][i][1]),
                            facecolor = axIf["Add Arrow"][1][i][2], 
                            edgecolor = axIf["Add Arrow"][1][i][3])
                    
                    
        except (TypeError, KeyError, IndexError, AttributeError):
            pass
            tk.messagebox.showwarning('Add Annotation Info is in wrong format','Please, refill Add Annotation') 
    """
    
    
    plt.ioff()
        
            
class clsExlPlotMulSubDlg(tk.Tk):
    global glPlotStt, dvGlFigLayout, glFigSize
    def __init__(self,parent, stt = glPlotStt,  *args, **kwargs):
        tk.Tk.__init__(self,parent, *args, **kwargs)
        self.title("Multiple Subplots")
        self.geometry("1000x750")
        self.frSize =[1000,750]
        # Create a tab Control
        self.tabControl = ttk.Notebook(self)
        
        if glPlotStt["Plot Layout"] == None:
            self.FigLayout = dvGlFigLayout  
        else:
            self.FigLayout = glPlotStt["Plot Layout"]
        self.populateFigLayoutTab()
        
        """
        self.tabControl.add(self.tbFigLayout, text='Figure Layout')
        self.tabControl.pack(expand=1, fill="both")
        try:
            self.FigLayout = stt["Plot Layout"]
        except TypeError:
            self.FigLayout = dvGlFigLayout
        self.frFigLayout = clsFigLayDlg(self.tbFigLayout,Info = self.FigLayout)
        self.frFigLayout.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.btnSaveFigLayout = ttk.Button(self.tbFigLayout, text='Save Layout',command=(lambda : self.SaveFigLayout()))
        self.btnSaveFigLayout.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
        
        """
        
        
        # Create a tab to load data
        self.tbData = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tbData, text='Data')
        self.tabControl.pack(expand=1, fill="both")
        #self.frData = []
        
        
        
        if glPlotStt["Plot Info"] == None:
            self.spIf = []    
        else:
            self.spIf = glPlotStt["Plot Info"]
            self.populateDataTab()
        
       
        # Create a tab to store initial Plot Setup
        self.tbPl = ttk.Frame(self.tabControl)           
        self.tabControl.add(self.tbPl, text='Plot Setup')
        self.tabControl.pack(expand=1, fill="both")
        #self.frPlotSetup = []
        # Get Plot the setup for all lines if they exist in the loaded file
        try:
            self.spMLStyle = []
            for i in range(len(glPlotStt["Plot Config"])):
                self.spMLStyle.append(glPlotStt["Plot Config"]["Marker and Line Style"][1])
        except (TypeError,IndexError) as e:
            self.spMLStyle = []
        
        if glPlotStt["Plot Setup"] == None:
            self.spSetup = []   
        else:
            self.spSetup = glPlotStt["Plot Setup"]
            self.populatePlotSetupTab()
        
        # Create a tab to Configure the plots
        self.tbConfig = ttk.Frame(self.tabControl)            
        self.tabControl.add(self.tbConfig, text='Plot Configuration')
        self.tabControl.pack(expand=1, fill="both")
        self.frPlotConfig = []
        
        
        if glPlotStt["Plot Config"] == None:
            self.spConfig = []  
        else:
            self.spConfig = glPlotStt["Plot Config"]
            self.populatePlotConfigTab()
        
    def populateFigLayoutTab(self, *args, **kwargs):
        self.tbFigLayout = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tbFigLayout, text='Figure Layout')
        self.tabControl.pack(expand=1, fill="both")
        self.frFigLayout = clsFigLayDlg(self.tbFigLayout,Info = self.FigLayout)
        self.frFigLayout.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.btnSaveFigLayout = ttk.Button(self.tbFigLayout, text='Save Layout',command=(lambda : self.SaveFigLayout()))
        self.btnSaveFigLayout.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
    def SaveFigLayout(self, *args, **kwargs):
        self.FigLayout = []
        self.FigLayout = self.frFigLayout.get()
        self.populateDataTab()
        self.tabControl.select(self.tbData)
    def populateDataTab(self, *args, **kwargs):
        #self.frData = []
        for wdg in self.tbData.winfo_children():
            wdg.destroy()
        self.frSize =[max(self.winfo_width(),1000),max(self.winfo_height(),750)]
        self.frAllData = clsExlDataTbDlg(self.tbData,self.FigLayout,self.spIf)
        self.frAllData.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.btnGetData = ttk.Button(self.tbData, text = 'Load all data', command = lambda : self.LoadAllData())
        self.btnGetData.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
    def LoadAllData(self,*args, **kwargs):
        self.spIf = []
        self.spIf = self.frAllData.get()
        self.populatePlotSetupTab()
        self.tabControl.select(self.tbPl)
        return self.spIf
    def populatePlotSetupTab(self, *args, **kwargs):
        #self.tbPl.rowconfigure(0, weight = 6)
        #self.tbPl.rowconfigure(1,weight = 1)
        for wdg in self.tbPl.winfo_children():
            wdg.destroy()
            
        self.frAllPlotSetup = clsPlotSetupTbDlg(self.tbPl,self.FigLayout,self.spIf,self.spSetup)
        self.frAllPlotSetup.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        """
        self.frSize =[max(self.winfo_width(),1000),max(self.winfo_height(),750)]
        if self.FigLayout != None:
            for i in range(self.FigLayout[0]):
                for j in range(self.FigLayout[1]):
                    if self.spIf != None:
                        try:
                            spSu = self.spSetup[i*self.FigLayout[1]+j]
                        except IndexError:
                            spSu = None
                        try: 
                            spInf = self.spIf[i*self.FigLayout[1]+j]
                        except IndexError:
                            spInf = {"Figure Type": 'Mono Axis', "Data" : [[]], "Data Load Setup" : [[]], "Data Source" : [[]]}
                        SubPlotSetup = clsSubPlotSetupTbDlg(self.tbPl,
                                                      [(self.frSize[0]-20)/(self.FigLayout[1]),
                                                      (self.frSize[1]-80)/(self.FigLayout[0])], 
                                                      spLb = "Sub Plot " + str(i*self.FigLayout[1]+j+1), 
                                                      spInfo = spInf,
                                                      spSetup = spSu)
                                                               
                        SubPlotSetup.grid(row = i, column = j, padx = 5, pady = 5, sticky = 'nw')
                        self.frPlotSetup.append(SubPlotSetup)
        """
        self.frSuBtns = ttk.Frame(self.tbPl)
        self.frSuBtns.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.btnPlotAll = ttk.Button(self.frSuBtns, text = 'Plot All', command = lambda : self.PlotAll())
        self.btnPlotAll.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.btnConfigAll = ttk.Button(self.frSuBtns, text = 'populate Configuration Tab', command = lambda : self.populatePlotConfigTab())
        self.btnConfigAll.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'nw')
    def PlotAll(self, *args, **kwargs):
        self.spSetup = []
        self.InGs = []
        self.Fig = None
        self.Fig = GnFg(tuple(self.FigLayout[2]))
        if self.FigLayout != None:
            self.OutGs = gridspec.GridSpec(self.FigLayout[0],self.FigLayout[1])
            for i in range(self.FigLayout[0]):
                for j in range(self.FigLayout[1]):
                    if (self.spIf[i*self.FigLayout[1]+j] != None) and self.frAllPlotSetup.frPlotSetup[i*self.FigLayout[1]+j] != None:
                        self.InGs.append(gridspec.GridSpecFromSubplotSpec(1,1,self.OutGs[i,j]))
                        self.spSetup.append(self.frAllPlotSetup.frPlotSetup[i*self.FigLayout[1]+j].get())
                        self.Fig = PlotSub(spFig = self.Fig, spGs = self.InGs[i*self.FigLayout[1]+j], 
                                            spType = self.spIf[i*self.FigLayout[1]+j]["Figure Type"], 
                                            spData = self.spIf[i*self.FigLayout[1]+j]["Data"], 
                                            spSetup = self.spSetup[i*self.FigLayout[1]+j])
                        
        plt.tight_layout()
        self.Fig.show()
        
    def populatePlotConfigTab(self, *args, **kwargs):
        self.tbConfig.rowconfigure(0, weight = 5)
        self.tbConfig.rowconfigure(1,weight = 1)
        self.frPlotConfig = []
        self.tbSubPlotConfig = []
        for wdg in self.tbConfig.winfo_children():
            wdg.destroy()
        self.tabConfigControl = ttk.Notebook(self.tbConfig)
        k = 0
        tbSz  = [max(self.winfo_width(),1000),max(self.winfo_height(),750)]
        axNum = 0 
        if self.FigLayout != None:
            for i in range(self.FigLayout[0]):
                for j in range(self.FigLayout[1]):
                    self.tbSubPlotConfig.append(ttk.Frame(self.tabConfigControl))            
                    self.tabConfigControl.add(self.tbSubPlotConfig[i*self.FigLayout[1]+j], text="Sub Plot " + str(i*self.FigLayout[1]+j+1))
                    self.tabConfigControl.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
                    k = 0
                    frNum = len(self.frAllPlotSetup.frPlotSetup[i*self.FigLayout[1]+j].Axes)
                    for t in self.frAllPlotSetup.frPlotSetup[i*self.FigLayout[1]+j].Axes:
                        try:
                            spCf = self.spConfig[axNum]
                        except (AttributeError,IndexError) as e:
                            spCf = None
                        try:
                            spLbLst = self.spConfig[axNum]["Add Label"][1][0]
                            
                            if len(spLbLst) <= len(self.spIf[i*self.FigLayout[1]+j]["Data Source"][k]):
                                for m in range(len(spLbLst),len(self.spIf[i*self.FigLayout[1]+j]["Data Source"][k])):
                                    spLbLst.append(self.spIf[i*self.FigLayout[1]+j]["Data Source"][k][m])       
                            else:   
                                temp = []
                                for m in range(len(self.spIf[i*self.FigLayout[1]+j]["Data Source"][k])):
                                    temp.append(spLbLst[m])
                                spLbLst = []
                                spLbLst = temp 
                        except (TypeError,KeyError,AttributeError,IndexError) as e:
                            
                            spLbLst = self.spIf[i*self.FigLayout[1]+j]["Data Source"][k]
                        try:
                            spMLIf = {"Line List" : spLbLst, "Marker and Line Style List" : self.spMLStyle[axNum]}
                            
                        except (AttributeError,IndexError) as e:
                            
                            spMLIf = {"Line List" : spLbLst, "Marker and Line Style List" : None}    
                        sz = [(tbSz[0]-20)/frNum,tbSz[1]-80]
                        fr = clsAxConfigDlg(self.tbSubPlotConfig[i*self.FigLayout[1]+j],sz,t,ax = None, axInfo = spCf, axMLStyleInfo = spMLIf)
                        fr.grid(row = 0, column = k, padx = 5, pady = 5, sticky = 'nw')
                        self.frPlotConfig.append(fr)                        
                        k += 1
                        axNum += 1            
        self.btnConfigAll = ttk.Button(self.tbConfig, text = 'Configure All', command = lambda : self.ConfigAll())
        self.btnConfigAll.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nw')
        self.tabControl.select(self.tbConfig)
    
    def ConfigAll(self, *args, **kwargs):
        self.spConfig = []
        self.PlotAll()
        plt.ion()
        i = 0
        for ax in self.Fig.axes:
            self.spConfig.append(self.frPlotConfig[i].get())
            ConfigAx(ax,self.spConfig[i])
            i +=1
        self.FigLayout = self.frFigLayout.get()
        try:
            self.Fig.set_tight_layout(not self.FigLayout[3][0])
            for i in range(len(self.FigLayout[3][1][0])):
                try:
                    a = float(self.FigLayout[3][1][0][i])
                    if i == 0:
                        self.Fig.subplots_adjust(bottom=a)
                    if i == 1:
                        self.Fig.subplots_adjust(top=a)
                    if i == 2:
                        self.Fig.subplots_adjust(left=a)
                    if i == 3:
                        self.Fig.subplots_adjust(right=a)
                    if i == 4:
                        self.Fig.subplots_adjust(hspace=a)
                    if i == 5:
                        self.Fig.subplots_adjust(wspace=a)
                        
                except ValueError:
                    pass
                    
            #plt.subplots_adjust(bottom=0.1, right=0.8, top=0.8)
            #self.Fig.subplots_adjust(hspace=float(self.FigLayout[3][1][0][4]), wspace=float(self.FigLayout[3][1][0][5]))
             
        except IndexError:
            plt.tight_layout()    
        
        plt.ioff()
        self.SavePlotSettings()
    def SavePlotSettings(self, *args, **kwargs):
        global glPlotStt, glDataSource, glWbkData
        global glDataFolder
            
        glPlotStt.clear()
        glPlotStt["Plot Type"] = "Multiple Axes"
        glPlotStt["Plot Layout"] = self.FigLayout
        
        #Error occurs with pickle loading if glWbkData are not reloaded
        xlFileList = list(glWbkData.keys()) 
        glWbkData.clear()
        for FileName in xlFileList:            
            wb = xl.load_workbook(glDataFolder+FileName, data_only=True)
            glWbkData.update({FileName: wb})
        #Error occurs with pickle loading if glWbkData are not reloaded
        glDataSource["Data Folder"] = glDataFolder
        glDataSource["Workbooks"] = glWbkData
        glPlotStt["Plot Data Source"] = glDataSource
        glPlotStt["Plot Info"] = self.spIf
        glPlotStt["Plot Setup"] = self.spSetup
        glPlotStt["Plot Config"] = self.spConfig
        
        #glPlotStt["Plot Marker and Line Style"] = self.spMLStyle
        
        #glPlotStt["Plot Figure"] = self.Fig
    
        
 
def fncPlotMultipleSubPlots():
    global fldGlFigLayout, dvGlFigLayout
    global glPlotStt
    glPlotSttReset()
    frPltMulSub = clsExlPlotMulSubDlg(None, stt = glPlotStt) 
    frPltMulSub.mainloop()
        
###-----------------------------------------------Excel GUIs functions--------------------------------------------------                


##-----------------------------------------------Excel GUIs-----------------------------------------------------------    



#-----------------------------------------------GUIs------------------------------------------------------------------ 

def fncLoadTextFile():    
    wdnLTF = Tk()
    wdnLTF.title('Load Text Files')
    LTF = clsLoadTextFile(wdnLTF)
    LTF.grid(row = 0, column = 0)
    global glWbkData
    glWbkData = LTF.AllWbks
    wdnLTF.mainloop()
    
def fncLoadTextFile2():    
    wdnLTF = Tk()
    wdnLTF.title('Load Text Files')
    LTF = clsLoadTextFile2(wdnLTF)
    LTF.grid(row = 0, column = 0)
    global glWbkData
    glWbkData = LTF.AllWbks
    wdnLTF.mainloop()
    
global glDctBrowse
glDctBrowse = {"entries":{"fields" : ["Common File Name","Folder Name", "Delimiter", "Output File Name"],
                         "default values" : ["", "", "\t",""]
                         }
              }
global glTxtDelimiter
glTxtDelimiter = ["\t", ",", " "]              
class clsBrowse(ttk.Frame):# A class to browse files
    global glDctBrowse,glTextFileExtentions
    def __init__(self, parent, Info = None, *args, **kwargs):
        ttk.Frame.__init__(self,parent, *args, **kwargs)
        self.fr = clsMakeFrame(self,glDctBrowse)
        self.fr.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.btnBrowse = ttk.Button(self,text = "Browse",command = lambda : self.opnFl())
        self.btnBrowse.grid(row=0,column=1, padx = 5, pady = 5, sticky = 'nw')
        self.If = Info
        self.fr.If = self.If
        self.fr.setInfo()
        self.FldNameLst = []
    def opnFl(self,*args, **kwargs):
        global glTxtDelimiter
        FileName = filedialog.askopenfilename(defaultextension = ".txt",
                                            filetypes=[('Text File', "*.txt"),
                                                       ('CSV File', "*.csv"),
                                                       ('Data File', "*.DAT"),
                                                       ('Excel File', "*.xlsx"),
                                                       ('Python Plot GUI file','*.pypGUI'), 
                                                       ('All files','*.*')],
                                            parent = self,
                                            title = "Load Text Files")
        
        delimiterFound = False
        txtDelimiter = ","
        with open(FileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if isDataLine(line):
                    for dlt in glTxtDelimiter:
                        TempLine = line.split(dlt)  
                        try: 
                            s = float(TempLine[0])
                            txtDelimiter = dlt
                            delimiterFound = True
                        except ValueError:
                            pass
                        if delimiterFound:
                            break
                if delimiterFound:
                            break
        try:
            self.If = [os.path.basename(FileName),FileName.replace(os.path.basename(FileName),""), 
                       txtDelimiter, os.path.basename(FileName)[:-4] + ".xlsx"]
            self.fr.If = self.If
            self.fr.setInfo()
        finally:
            pass 
    def get(self,  *args, **kwargs):
        self.If = self.fr.get()
        return self.If
    def populate(self,  *args, **kwargs):
        self.fr.setInfo()
    def LoadTextNSaveExl(self,  *args, **kwargs):
        self.get()
        self.FlNameLst = []
        SltStr = self.If[1]+'*'+self.If[0]+'*'
        for FileName in glob(SltStr):
            if FileName[-4:] in glTextFileExtentions:
                self.FlNameLst.append(FileName)
        k = 0
        wb = Workbook()
        for FileName in self.FlNameLst: 
            if k == 0:
                ws = wb.active
            else:
                ws = wb.create_sheet() 
            ws.title = os.path.basename(FileName)[:-4]
            with open(FileName, 'r') as f:
                lines = f.readlines()
                for i in range(len(lines)):
                    TempLine = lines[i].split(self.If[2])  
                    for j in range(len(TempLine)):    
                        try: 
                            ws.cell(row = i+1, column = j+1).value = float(TempLine[j])
                        except ValueError:
                            ws.cell(row = i+1, column = j+1).value = TempLine[j] 
            
            k += 1
        wb.save(self.If[1] + self.If[3])
        self.wb = wb
   
class clsLoadTextFile2(tk.Frame):    
    def LoadAllData(self, *args, **kwargs):
        global glDataSource, glWbkData, glPlotStt, glDataFolder
        self.AllWbks = {}
        for fr in self.frLst:
            fr.LoadTextNSaveExl()
            glDataFolder = fr.If[1]
            s = fr.If[0] + " in " + fr.If[1] 
            self.AllWbks.update({s: fr.wb})
         
        glWbkData = self.AllWbks
        glDataSource["Workbooks"] = glWbkData
        glDataSource["Data Folder"] = glDataFolder
        glPlotStt["Plot Data Source"] = glDataSource
        
    def __init__(self,parent, *args, **kwargs):
        tk.Frame.__init__(self,parent, nextFr,*args, **kwargs)
        self.frOperBtns = ttk.Frame(self)
        self.frOperBtns.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.btnLdDt = ttk.Button(self.frOperBtns,text = 'Load Data', command = self.LoadAllData)
        self.btnLdDt.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.btnAddFrame = ttk.Button(self.frOperBtns, text = "+", width = 3, command = lambda: self.AddFrame())
        self.btnAddFrame.grid(row=0,column=1, padx = 5, pady = 5, sticky = 'nw')
        self.btnRemoveFrame = ttk.Button(self.frOperBtns, text = "-", width = 3, command = lambda: self.RemoveFrame())
        self.btnRemoveFrame.grid(row=0,column=2, padx = 5, pady = 5, sticky = 'nw')
        self.btnOK = ttk.Button (self.frOperBtns,text = 'OK', command = lambda : parent.destroy())
        self.btnOK.grid(row=0, column=4, padx = 5, pady = 5, sticky = 'nw')
        self.txtFldName = [] #Folder contains the workbooks
        self.frLst = [] 
        self.CmnFlNameLst = []
        self.FldNameLst = []
        self.frNum = 0
        self.AllWbks = {}
        self.AddFrame()
    def AddFrame(self,*args, **kwargs):
        self.frNum += 1
        If = None
        if self.frNum > 1:
            try:
                If = self.frLst[self.frNum-2].get()
            except IndexError as e:
                pass
        fr = clsBrowse(self, Info = If)
        fr.grid(row=self.frNum,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.frLst.append(fr)                
    def RemoveFrame(self, *args, **kwargs):
        if self.frNum > 1:
            self.frNum -= 1
            self.frLst[self.frNum].destroy()
            self.frLst = self.frLst[:self.frNum]
            self.CmnFlNameLst = self.CmnFlNameLst[:self.frNum]
            self.FldNameLst = self.FldNameLst[:self.frNum]
    def get(self, *args, **kwargs):
        self.CmnFlNameLst = []
        self.FldNameLst = []
        for fr in self.frLst:
            self.CmnFlNameLst.append(fr.get()[0])
            self.FldNameLst.append(fr.get()[1])
    def GotoMainFrame(self,*arg,**kwargs):
        parent.destroy()
        

class clsLoadTextFile(tk.Frame):    
    def LoadNSaveData(self, *args, **kwargs):
        global glDataSource, glWbkData, glPlotStt, glDataFolder
        self.AllWbks = {}
        for fr in self.frLst:
            fr.LoadTextNSaveExl()
            glDataFolder = fr.If[1]
            s = fr.If[0] + " in " + fr.If[1] 
            self.AllWbks.update({s: fr.wb})
         
        glWbkData = self.AllWbks
        glDataSource["Workbooks"] = glWbkData
        glDataSource["Data Folder"] = glDataFolder
        glPlotStt["Plot Data Source"] = glDataSource
        
    def __init__(self,parent, *args, **kwargs):
        tk.Frame.__init__(self,parent,*args, **kwargs)
        self.frOperBtns = ttk.Frame(self)
        self.frOperBtns.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.btnLdDt = ttk.Button(self.frOperBtns,text = 'Load Data and Save to Excel', command = self.LoadNSaveData)
        self.btnLdDt.grid(row=0,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.btnAddFrame = ttk.Button(self.frOperBtns, text = "+", width = 3, command = lambda: self.AddFrame())
        self.btnAddFrame.grid(row=0,column=1, padx = 5, pady = 5, sticky = 'nw')
        self.btnRemoveFrame = ttk.Button(self.frOperBtns, text = "-", width = 3, command = lambda: self.RemoveFrame())
        self.btnRemoveFrame.grid(row=0,column=2, padx = 5, pady = 5, sticky = 'nw')
        self.btnOK = ttk.Button (self.frOperBtns,text = 'OK', command = parent.destroy)
        self.btnOK.grid(row=0, column=4, padx = 5, pady = 5, sticky = 'nw')
        self.txtFldName = [] #Folder contains the workbooks
        self.frLst = [] 
        self.CmnFlNameLst = []
        self.FldNameLst = []
        self.frNum = 0
        self.AllWbks = {}
        self.AddFrame()
    def AddFrame(self,*args, **kwargs):
        self.frNum += 1
        If = None
        if self.frNum > 1:
            try:
                If = self.frLst[self.frNum-2].get()
            except IndexError as e:
                pass
        fr = clsBrowse(self, Info = If)
        fr.grid(row=self.frNum,column=0, padx = 5, pady = 5, sticky = 'nw')
        self.frLst.append(fr)                
    def RemoveFrame(self, *args, **kwargs):
        if self.frNum > 1:
            self.frNum -= 1
            self.frLst[self.frNum].destroy()
            self.frLst = self.frLst[:self.frNum]
            self.CmnFlNameLst = self.CmnFlNameLst[:self.frNum]
            self.FldNameLst = self.FldNameLst[:self.frNum]
    def get(self, *args, **kwargs):
        self.CmnFlNameLst = []
        self.FldNameLst = []
        for fr in self.frLst:
            self.CmnFlNameLst.append(fr.get()[0])
            self.FldNameLst.append(fr.get()[1])
#from subprocess import Popen
def fncRunPyFile(root):
    MainDirectory = os.getcwd()
    FullName = filedialog.askopenfilename(defaultextension = ".py",
                                            filetypes=[('Python File', "*.py"), 
                                                       ('All files','*.*')],
                                            parent = root,
                                            title = "Run .py Files")
    FileName = os.path.basename(FullName)
    FolderName = FullName[:-len(FileName)]
    os.chdir(FolderName)
    os.system(FileName)
    os.chdir(MainDirectory)
    
        
def About():
    a = 1
def fncSaveToText():
    plt.gcf()
    plt.savefig('Myfig.tiff', dpi = 600) 
    image = Image.open('Myfig.tiff')
    image = image.resize (mm2inch(88,66), Image.ANTIALIAS)
    image.save('Myfig.tiff')
    image.close()
def fncSaveFile(root):
    global glPlotStt
    try:
        FileName = filedialog.asksaveasfilename(defaultextension = ".pypGUI",
                                                filetypes=[('Python Plot GUI file','*.pypGUI'), ('All files','*.*')],
                                                parent = root,
                                                title = "Save a Python Plot GUI File")
    except FileNotFoundError:
        pass
    file = open( FileName, "wb" )
    
    pickle.dump(glPlotStt, file, protocol=pickle.HIGHEST_PROTOCOL )
    file.close()
    #pickle.dump(glIns, open( "save.p", "wb" ) )
def fncLoadFile(root):
    global glPlotStt, glIns, glWbkData, glDataFolder
    FileName = filedialog.askopenfilename(defaultextension='.pypGUI',
                       filetypes=[('Python Plot GUI file','*.pypGUI'), ('All files','*.*')],
                       parent = root,
                       title = "Open a Python Plot GUI File")
    file = open( FileName, "rb" )
    glPlotStt.clear()
    glPlotStt = pickle.load(file)
    file.close()
    try:
        glWbkData = glPlotStt["Plot Data Source"]["Workbooks"]
        glDataFolder = glPlotStt["Plot Data Source"]["Data Folder"]
    except KeyError:
        glWbkData = {}
        glDataFolder = ""
    if glPlotStt["Plot Type"] == "Multiple Axes":
        
        frPltMulSub = clsExlPlotMulSubDlg(None, stt = glPlotStt) 
        frPltMulSub.title(os.path.basename(FileName))
        
        frPltMulSub.ConfigAll()
        frPltMulSub.mainloop()



def PlotTrippleAxes():
    global XYData
    BaseFig(XYData,PlNum = 2,PlMul = 'Stack', PlXScale = 'Lin', PlYScale = 'Lin', PlStyle = 'Line', PlLb = 'No Labels', PlXLb = r'2$\theta$ CuK$\alpha_1$ (deg)',PlYLb = "y Axis Title")

if __name__ == '__main__':    
    root = Tk()
    root.title("Graph Plot")
    root.geometry("1000x750")
    
    menu = Menu(root)
    root.config(menu=menu)
    
    LoadDataMenu = Menu(menu)
    menu.add_cascade(label="File", menu=LoadDataMenu)
    
    LoadDataMenu.add_command(label="Open", command=lambda : fncLoadFile(root))
    LoadDataMenu.add_command(label="Load Data from Workbooks", command=fncLoadWorkbook)
    LoadDataMenu.add_command(label="Load Data from Text Files", command=fncLoadTextFile)
    LoadDataMenu.add_command(label="Run .py Files", command=lambda: fncRunPyFile(root))
    LoadDataMenu.add_separator()
    LoadDataMenu.add_command(label="Save", command= lambda : fncSaveFile(root))
    LoadDataMenu.add_separator()
    LoadDataMenu.add_command(label="Exit", command=root.destroy)
    
    PlotGraphMenu = Menu(menu)
    
    menu.add_cascade(label="Plot", menu=PlotGraphMenu)
    PlotGraphMenu.add_command(label="Plot Mono Axis", command=fncPlotMonoAxis)
    
    PlotDoubleMenu = Menu(PlotGraphMenu)
    PlotGraphMenu.add_cascade(label = "Plot Double Axes", menu = PlotDoubleMenu)
    PlotDoubleMenu.add_command(label="Plot Double Y Axes", command= lambda x=root:PlotDoubleAxes(root))
    PlotDoubleMenu.add_command(label="Plot with An Inset", command= fncPlotInset)
    
    PlotGraphMenu.add_command(label="Plot Tripple Axes", command=fncTripleAxes)
    PlotGraphMenu.add_command(label="Plot Multiple SubPlots", command= fncPlotMultipleSubPlots)
    
    OptionMenu = Menu(menu)
    menu.add_cascade(label="Options", menu=OptionMenu)
    OptionMenu.add_command(label="Settings", command=fncSettings)
    
    
    SaveDataMenu = Menu(menu)
    menu.add_cascade(label="Save", menu=SaveDataMenu)
    SaveDataMenu.add_command(label="Resize and Save Figure", command=fncSaveFigure)
    SaveDataMenu.add_command(label="To Txt", command=fncSaveToText)
    
    root.mainloop()
