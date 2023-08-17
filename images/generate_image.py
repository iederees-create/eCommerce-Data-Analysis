import matplotlib.pyplot as plt
import numpy as np

# Generate example data for age distribution
np.random.seed(0)
ages = np.random.randint(18, 65, size=1000)

# Create a histogram plot
plt.figure(figsize=(8, 6))
plt.hist(ages, bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Save the plot as an image file
plt.savefig('age_distribution.png', dpi=300)
