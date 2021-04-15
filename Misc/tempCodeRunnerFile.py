
random.seed(1)
dist, numSamples = [], 1000000

for i in range(numSamples):
   dist.append(random.gauss(0, 100))
   
weights = [1/numSamples]*len(dist)
v = pylab.hist(dist, bins = 100,
              weights = [1/numSamples]*len(dist))
              
print('Fraction within ~200 of mean =',
     sum(v[0][30:70]))

def gaussian(x, mu, sigma):
 factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
 factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
 return factor1*factor2
 
xVals, yVals = [], []
mu, sigma = 0, 1
x = -4
while x <= 4:
   xVals.append(x)
   yVals.append(gaussian(x, mu, sigma))
   x += 0.05
pylab.plot(xVals, yVals)
pylab.title('Normal Distribution, mu = ' + str(mu)\
           + ', sigma = ' + str(sigma))

