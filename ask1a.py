#NEFELI-ELENI KATSILEROU 4385

import csv
import sys

def my_merge_sort(data, clustering_attribute, aggregation_attribute, aggregation_function):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = my_merge_sort(data[:mid], clustering_attribute, aggregation_attribute, aggregation_function)  #sublist
    right = my_merge_sort(data[mid:], clustering_attribute, aggregation_attribute, aggregation_function)  #sublist
    
    return my_merge(left, right, clustering_attribute, aggregation_attribute, aggregation_function)

def my_merge(left, right,  clustering_attribute, aggregation_attribute, aggregation_function):
    result = []  #store results
    i = j = 0  #counters
    aggregation_dictionary = {}
    
    while i < len(left) and j < len(right):
        left_clustering = left[i][clustering_attribute]
        right_clustering = right[j][clustering_attribute]
        
        if left_clustering < right_clustering:
            aggregation_dictionary[left_clustering] = aggregation_dictionary.get(left_clustering, [])
            aggregation_dictionary[left_clustering].append(left[i][aggregation_attribute])
            result.append(left[i])
            i += 1
        elif left_clustering > right_clustering:
            aggregation_dictionary[right_clustering] = aggregation_dictionary.get(right_clustering, [])
            aggregation_dictionary[right_clustering].append(right[j][aggregation_attribute])
            result.append(right[j])
            j += 1
        else:
            aggregation_dictionary[left_clustering] = aggregation_dictionary.get(left_clustering, [])
            aggregation_dictionary[left_clustering].append(left[i][aggregation_attribute])
            aggregation_dictionary[right_clustering] = aggregation_dictionary.get(right_clustering, [])
            aggregation_dictionary[right_clustering].append(right[j][aggregation_attribute])
            
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1
    
    # Append remaining elements from either left or right list
    while i < len(left):
        left_clustering = left[i][clustering_attribute]
        aggregation_dictionary[left_clustering] = aggregation_dictionary.get(left_clustering, [])
        aggregation_dictionary[left_clustering].append(left[i][aggregation_attribute])
        result.append(left[i])
        i += 1
    
    while j < len(right):
        right_clustering = right[j][clustering_attribute]
        aggregation_dictionary[right_clustering] = aggregation_dictionary.get(right_clustering, [])
        aggregation_dictionary[right_clustering].append(right[j][aggregation_attribute])
        result.append(right[j])
        j += 1
    
    # Write the aggregation results to the output file
    with open('O1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for key, values in  aggregation_dictionary.items():
            if aggregation_function == 'sum':
                aggregation_value = sum(values)
            elif aggregation_function == 'max':
                aggregation_value = max(values)
            elif aggregation_function == 'min':
                aggregation_value = min(values)        
            writer.writerow([key, aggregation_value])
    
    return result

def group_by_aggregation(input_file, clustering_attribute, aggregation_attribute, aggregation_function):
    data = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(list([int(row[0]),int(row[1]),int(row[2])]))
    
    print("data:",data)
    data = my_merge_sort(data, clustering_attribute, aggregation_attribute, aggregation_function)



input_file = sys.argv[1]
clustering_attribute = int(sys.argv[2])
aggregation_attribute = int(sys.argv[3])
aggregation_function = sys.argv[4]

group_by_aggregation(input_file, clustering_attribute, aggregation_attribute, aggregation_function)
