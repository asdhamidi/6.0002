#UNCOVER FOR SECOND DEMO    
numSubsets = 10
dimensions = (1, 2, 3, 4)
rSquares = {}
for d in dimensions:
   rSquares[d] = []
       
for f in range(numSubsets):
   trainX, trainY, testX, testY = splitData(xVals, yVals)
   for d in dimensions:
       model = pylab.polyfit(trainX, trainY, d)
       estYVals = pylab.polyval(model, trainX)
       estYVals = pylab.polyval(model, testX)
       rSquares[d].append(rSquared(testY, estYVals))
print('Mean R-squares for test data')
for d in dimensions:
   mean = round(sum(rSquares[d])/len(rSquares[d]), 4)
   sd = round(numpy.std(rSquares[d]), 4)
   print('For dimensionality', d, 'mean =', mean,
         'Std =', sd)
#print(rSquares[1])