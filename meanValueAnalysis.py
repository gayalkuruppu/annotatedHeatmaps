import numpy as np
import matplotlib.pyplot as plt

m = int(input('Enter the concurrency : '))
serviceRates = list(map(int, input('Enter the service rates seperated by commas : ').split(',')))
k = len(serviceRates)  # number of servers
p = 1/k
ET = np.zeros((m, k))
conAxis = np.arange(1, m+1)

for i in range(k):
    ET[0][i] = 1/serviceRates[i]


def lmbda(x):  # we use to get lambda(m-1)
    total = 0
    for t in range(k):
        total += p*ET[x][t]
    return (x+1)/total


for i in range(1, m):
    for j in range(k):
        ET[i][j] = (1 + p*lmbda(i-1)*ET[i-1][j])/serviceRates[j]

ER = np.sum(ET, axis=1)  # Response Time
X = lm/ER  # Throughput

plt.figure()
plt.title('Throughput Vs Concurrency')
plt.xlabel('Concurrency(N)')
plt.ylabel('Throughput')
plt.plot(lm, X)
plt.show()
