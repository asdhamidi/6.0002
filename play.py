# This file is for trying random codes.

# import random
# import matplotlib.pyplot as plt
# def CLT(size):
#     population = []
#     for r in range(10000):
#         population.append(random.randint(1, 10000))

#     samples = []
#     for r in range(500):
#         currentSample = []
#         for i in range(size):
#             currentSample.append(random.choice(population))
#         samples.append(currentSample)

#     means = []
#     for sample in samples:
#         means.append(sum(sample) / size)

#     return (sum(population) / len(population), sum(means) / len(means))

# size = []
# popMean = []
# meanOfMeans = []
# for r in range(100, 10000, 100):
#     size.append(r)
#     pMean, mMean = CLT(r)
#     popMean.append(pMean)
#     meanOfMeans.append(mMean)
# diff = []
# zero = []
# for r in range(len(popMean)):
#     diff.append(popMean[r] - meanOfMeans[r])
#     zero.append(0)

# plt.plot(size, diff, "r-.")
# plt.plot(size, zero, "k-")
# plt.xlabel("Sample Size")
# plt.ylabel("Difference in Pop. Mean and Mean of Means.")
# plt.show()


