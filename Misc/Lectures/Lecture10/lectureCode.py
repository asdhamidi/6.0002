# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:45:20 2016

@author: johnguttag
"""

import random, matplotlib.numpy as numpy, numpy

#set line width
numpy.rcParams['lines.linewidth'] = 4
#set font size for titles 
numpy.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
numpy.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
numpy.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
numpy.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
numpy.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
numpy.rcParams['ytick.major.size'] = 7
#set size of markers
numpy.rcParams['lines.markersize'] = 10
#set number of examples shown in legends
numpy.rcParams['legend.numpoints'] = 1

def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline() #discard header
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)
    
def labelPlot():
    numpy.title('Measured Displacement of Spring')
    numpy.xlabel('|Force| (Newtons)')
    numpy.ylabel('Distance (meters)')

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = numpy.array(xVals)
    yVals = numpy.array(yVals)
    xVals = xVals*9.81  #acc. due to gravity
    numpy.plot(xVals, yVals, 'bo',
               label = 'Measured displacements')
    labelPlot()
    
def fitData(fileName):
    xVals, yVals = getData(fileName)
    xVals = numpy.array(xVals)
    yVals = numpy.array(yVals)
    xVals = xVals*9.81 #get force
    numpy.plot(xVals, yVals, 'bo',
               label = 'Measured points')
    labelPlot()                 
    a,b = numpy.polyfit(xVals, yVals, 1)
    estYVals = a*numpy.array(xVals) + b
    print('a =', a, 'b =', b)
    numpy.plot(xVals, estYVals, 'r',
               label = 'Linear fit, k = '
               + str(round(1/a, 5)))
    numpy.legend(loc = 'best')
    
#fitData('springData.txt')

   
def fitData1(fileName):
    xVals, yVals = getData(fileName)
    xVals = numpy.array(xVals)
    yVals = numpy.array(yVals)
    xVals = xVals*9.81 #get force
    numpy.plot(xVals, yVals, 'bo',
               label = 'Measured points')
    labelPlot()                 
    model = numpy.polyfit(xVals, yVals, 1)
    estYVals = numpy.polyval(model, xVals)
    numpy.plot(xVals, estYVals, 'r',
               label = 'Linear fit, k = '
               + str(round(1/model[0], 5)))
    numpy.legend(loc = 'best')



def rSquared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    meanError = error/len(observed)
    return 1 - (meanError/numpy.var(observed))

def genFits(xVals, yVals, degrees):
    models = []
    for d in degrees:
        model = numpy.polyfit(xVals, yVals, d)
        models.append(model)
    return models

def testFits(models, degrees, xVals, yVals, title):
    numpy.plot(xVals, yVals, 'o', label = 'Data')
    for i in range(len(models)):
        estYVals = numpy.polyval(models[i], xVals)
        error = rSquared(yVals, estYVals)
        numpy.plot(xVals, estYVals,
                   label = 'Fit of degree '\
                   + str(degrees[i])\
                   + ', R2 = ' + str(round(error, 5)))
    numpy.legend(loc = 'best')
    numpy.title(title)

#xVals, yVals = getData('mysteryData.txt')
#degrees = (1, 2)
#models = genFits(xVals, yVals, degrees)
#testFits(models, degrees, xVals, yVals, 'Mystery Data')

##Compare higher-order fits
#degrees = (2, 4, 8, 16)
#models = genFits(xVals, yVals, degrees)
#testFits(models, degrees, xVals, yVals, 'Mystery Data')


def genNoisyParabolicData(a, b, c, xVals, fName):
    yVals = []
    for x in xVals:
        theoreticalVal = a*x**2 + b*x + c
        yVals.append(theoreticalVal\
        + random.gauss(0, 35))
    f = open(fName,'w')
    f.write('x        y\n')
    for i in range(len(yVals)):
        f.write(str(yVals[i]) + ' ' + str(xVals[i]) + '\n')
    f.close()
    
##parameters for generating data
#xVals = range(-10, 11, 1)
#a, b, c = 3.0, 0.0, 0.0
#degrees = (2, 4, 8, 16)
#
##generate data
#random.seed(0)
#genNoisyParabolicData(a, b, c, xVals,
#                      'Dataset 1.txt')
#genNoisyParabolicData(a, b, c, xVals,
#                      'Dataset 2.txt')
#
#xVals1, yVals1 = getData('Dataset 1.txt')
#models1 = genFits(xVals1, yVals1, degrees)
#testFits(models1, degrees, xVals1, yVals1,
#        'DataSet 1.txt')
#
#numpy.figure()
#xVals2, yVals2 = getData('Dataset 2.txt')
#models2 = genFits(xVals2, yVals2, degrees)
#testFits(models2, degrees, xVals2, yVals2,
#         'DataSet 2.txt')
#
#numpy.figure()
#testFits(models1, degrees, xVals2, yVals2,
#         'DataSet 2/Model 1')
#numpy.figure()
#testFits(models2, degrees, xVals1, yVals1,
#         'DataSet 1/Model 2')

##a line
#xVals = (0,1,2,3)
#yVals = xVals
#numpy.plot(xVals, yVals, label = 'Actual values')
#a,b,c = numpy.polyfit(xVals, yVals, 2)
#print('a =', round(a, 4), 'b =', round(b, 4),
#      'c =', round(c, 4))
#estYVals = numpy.polyval((a,b,c), xVals)
#numpy.plot(xVals, estYVals, 'r--', label = 'Predictive values')
#print('R-squared = ', rSquared(yVals, estYVals))
#numpy.legend(loc = 'best')

##OPEN FOR SECOND DEMO
##
#numpy.figure()
##Extend domain
#xVals = xVals + (20,)
#yVals = xVals
#numpy.plot(xVals, yVals, label = 'Actual values')
#estYVals = numpy.polyval((a,b,c), xVals)
#numpy.plot(xVals, estYVals, 'r--', label = 'Predictive values')
#print('R-squared = ', rSquared(yVals, estYVals))
#numpy.legend(loc = 'best')

##OPEN FOR THIRD DEMO
##almost a line
#numpy.figure()
#xVals = (0,1,2,3)
#yVals = (0,1,2,3.1)
#numpy.plot(xVals, yVals, label = 'Actual values')
#model = numpy.polyfit(xVals, yVals, 2)
#print(model)
#estYVals = numpy.polyval(model, xVals)
#numpy.plot(xVals, estYVals, 'r--', label = 'Predicted values')
#print('R-squared = ', rSquared(yVals, estYVals))
#numpy.legend(loc = 'best')

##OPEN FOR FOURTH DEMO

#numpy.figure()
##Extend domain
#xVals = xVals + (20,)
#yVals = xVals
#numpy.plot(xVals, yVals, label = 'Actual values')
#estYVals = numpy.polyval(model, xVals)
#numpy.plot(xVals, estYVals, 'r--', label = 'Predicted values')
#print('R-squared = ', rSquared(yVals, estYVals))
#numpy.legend(loc = 'best')

