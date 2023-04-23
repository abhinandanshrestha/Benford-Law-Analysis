import csv
import json
import math

BENFORD_PERCENTAGES = [0, 0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
def benfordParams(data_list):

    rows=[]

    # exclude 'first row since it is header'
    for data in data_list[1:]:
        if data!='':
            int_data=int(float(data))
            rows.append(int_data) 

    # Count the number of first digits in the list of rows
    first_digit_counts = {str(i): 0 for i in range(10)}
    for number in rows:
        first_digit = str(number)[0]
        first_digit_counts[first_digit] += 1
    
    results=[]
    for n in range(10):
        data_frequency = first_digit_counts[str(n)]
        # print(data_frequency,' ')
        data_frequency_percent = data_frequency / len(rows)
        benford_frequency = len(rows) * BENFORD_PERCENTAGES[n]
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