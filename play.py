import numpy as np
import math
import matplotlib.pyplot as plt

def collatz(num):
    steps = 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = (3 * num) + 1
        steps += 1
    
    return steps
        

num = []
sqr = []
for r in range(1000):
    num.append(r)
    sqr.append(collatz(r))
plt.plot(num, sqr, 'b^')
plt.xlabel("Number")
plt.ylabel("Steps Taken")
plt.title("Collatz Conjecture Representation")
plt.show()
