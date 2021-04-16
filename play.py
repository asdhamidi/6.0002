# This file is for trying random codes.

import random
import matplotlib.pyplot as plt
def CLT(size):
    population = []
    for r in range(size):
        population.append(random.randint(1, 10000))

    samples = []
    for r in range(500):
        currentSample = []
        for i in range(10000):
            currentSample.append(random.choice(population))
        samples.append(currentSample)

    means = []
    for sample in samples:
        means.append(sum(sample) / 10000)

    return (sum(population) / len(population), sum(means) / len(means))

size = []
popMean = []
meanOfMeans = []
for r in (100, 100000):
    size.append(r)
    pMean, mMean = CLT(r)
    popMean.append(pMean)
    meanOfMeans.append(mMean)

plt.scatter(size, popMean, "b--", label = "Population Mean")
plt.scatter(size, meanOfMeans, "r--", label = "Mean of Means")
plt.legend()
plt.show()

        