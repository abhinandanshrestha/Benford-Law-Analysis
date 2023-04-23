import numpy as np

def benford_data(size):
    # Generate random numbers from Benford's distribution
    # using the NumPy random generator
    benford = np.random.lognormal(mean=0, sigma=1, size=size)
    
    # Normalize the distribution to sum up to 1
    benford /= benford.sum()

    # Return the Benford's distribution as an array
    return benford

# Example usage
data = benford_data(10000)
