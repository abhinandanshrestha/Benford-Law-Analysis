import csv
import json
import math

def benfordParams(data_list):
    BENFORD_PERCENTAGES = [0, 0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

    first_digits=[]

    # exclude '0'
    for data in data_list[1:]:
        if data!='':
            int_data=int(float(data))
            first_digits.append(int_data) 
    # print("****",len(first_digits))

    # Count the number of first digits in the list of numbers
    first_digit_counts = {str(i): 0 for i in range(10)}
    for number in first_digits:
        first_digit = str(number)[0]
        first_digit_counts[first_digit] += 1
    # print(len(first_digits))
    
    results=[]
    for n in range(10):
        data_frequency = first_digit_counts[str(n)]
        data_frequency_percent = data_frequency / len(first_digits)
        benford_frequency = len(first_digits) * BENFORD_PERCENTAGES[n]
        benford_frequency_percent = BENFORD_PERCENTAGES[n]
        difference_frequency = data_frequency - benford_frequency
        difference_frequency_percent = data_frequency_percent - benford_frequency_percent

        results.append({"n": n,
                        "data_frequency":               data_frequency,
                        "data_frequency_percent":       data_frequency_percent,
                        "benford_frequency":            benford_frequency,
                        "benford_frequency_percent":    benford_frequency_percent,
                        "difference_frequency":         difference_frequency,
                        "difference_frequency_percent": difference_frequency_percent})
        
    conform = all(results[i]["difference_frequency_percent"] < 0.05 for i in range(1, 10))
    return results,conform