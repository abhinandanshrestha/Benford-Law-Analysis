import csv
import random
import numpy as np

# Set the number of rows to create
num_rows = 10000

file_list = ['wholeNum','completeRandomData','benfordData']
# Create a list of data for each row (in this case, each row only has one element)
wholeNum = [[i] for i in range(num_rows)]

# Create a list of random data for each row
completeRandomData = [[random.random()] for _ in range(num_rows)]

def benford_data(size):
    # Generate random numbers from Benford's distribution
    # using the NumPy random generator
    benford = np.random.lognormal(mean=0, sigma=1, size=size)
    
    # Normalize the distribution to sum up to 1
    benford /= benford.sum()

    # Return the Benford's distribution as an array
    return benford

# Example usage
benfordData = benford_data(10000)

# Map each file type to its corresponding data list
data_map = {
    'wholeNum': wholeNum,
    'completeRandomData': completeRandomData,
    'benfordData': [[val] for val in benfordData]
}

# Write each data list to a separate CSV file
for file_type in file_list:
    with open('uploads/'+file_type + '.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data_map[file_type])