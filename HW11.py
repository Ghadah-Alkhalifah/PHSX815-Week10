import numpy as np
import matplotlib.pyplot as plt

# Define the distribution to sample from
def dist_fun(x):
    y= 1 / (1 + np.exp(-x))
    return y

np.random.seed(202)
sample1 = np.random.uniform(-5, 5, 40)
# plot the histogram of non-gaussian distribution
dist=dist_fun(sample1)
plt.hist(dist, bins=60, color='red', density=True, alpha=0.75, ec='black')
plt.xlabel("Probablities")
plt.ylabel("Counts")
plt.title("Non-gaussian Distribution")
plt.show()

#  parameters and seed
N = 40
M = 10000
seed = 202
np.random.seed(seed)

# Generate the histogram of averages
samples = np.random.uniform(-5, 5, (M, N))
averages = [np.mean(dist_fun(Nsample)) for Nsample in samples]
plt.hist(averages, bins=40, color='skyblue', density=True, alpha=0.75, ec='black')
plt.title(f"Distribution of {M} averages from {N} samples")
plt.xlabel("Averages")
plt.ylabel("Counts")
plt.show()
