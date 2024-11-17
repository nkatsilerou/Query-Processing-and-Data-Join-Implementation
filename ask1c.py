#NEFELI-ELENI KATSILEROU 4385

import csv

def my_composite_query(R_file, S_file, output_file):

    # Dictionary to store sums of E values for each A value from S.csv
    sum_e_dictionary = {}
 
    # Read R.csv and perform the composite query
    with open(R_file, 'r') as R_file, open(output_file, 'w', newline='') as output, open(S_file, 'r') as S_file:
        writer = csv.writer(output)
        R_line = R_file.readline()
        S_line = S_file.readline()
        toadd = []

        while R_line and S_line:
            R_items = R_line.split(',')
            S_items = S_line.split(',')
            a_r = int(R_items[0])
            c = int(R_items[2])
            a_s = int(S_items[1])
            e = int(S_items[2])
            sum_e_dictionary[a_s] = sum_e_dictionary.get(a_s, 0)
            sum_e_dictionary[a_s] += e
            
            if c == 7:
                toadd.append(a_r)
                
            R_line = R_file.readline()
            S_line = S_file.readline()

        for x in toadd:# x = a_r
            if x in sum_e_dictionary:
                writer.writerow([x, sum_e_dictionary[x]])

my_composite_query('R.csv', 'S.csv', 'O3.csv')


