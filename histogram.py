import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# NORMAL DISTRIBUTION
# --------------------------

# Create random number generator
rg = np.random.default_rng(1)

# Parameters
mu, sigma = 2, 0.5
num_samples = 10000

# Generate normal data
normal_data = rg.normal(mu, sigma, num_samples)

# Plot Normal Distribution Histogram
plt.figure(figsize=(8, 5))
plt.hist(normal_data, bins=50, density=True, alpha=0.6,
         color='skyblue', edgecolor='black')
plt.title("Normal Distribution Histogram")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.grid(True)
plt.show()


# --------------------------
# UNIFORM DISTRIBUTION
# --------------------------

# Generate uniform data
uniform_data = np.random.uniform(0, 10, 1000)

# Plot Uniform Distribution Histogram
plt.figure(figsize=(8, 5))
plt.hist(uniform_data, bins=30, edgecolor='black')
plt.title("Uniform Distribution Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()