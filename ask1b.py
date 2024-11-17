#NEFELI-ELENI KATSILEROU 4385

import csv

def my_merge_join(R_file, S_file, output_file):
    with open(R_file, 'r') as R_file, open(S_file, 'r') as S_file, open(output_file, 'w', newline='') as output:
        writer = csv.writer(output)
        R_reader = csv.reader(R_file)
        S_reader = csv.reader(S_file)     
        
        R_row = next(R_reader, None)
        S_row = next(S_reader, None)
        
        while R_row is not None and S_row is not None:
            R_key = int(R_row[0])
            S_key = int(S_row[1])
            
            if R_key == S_key:
                writer.writerow(R_row + S_row[0:1] + S_row[2:])
                S_row = next(S_reader, None)
            elif R_key < S_key:
                R_row = next(R_reader, None)
            else:
                S_row = next(S_reader, None)

        # Handle remaining rows in either file
        while R_row is not None:
            writer.writerow(R_row + [''] * 4)  # Append empty fields for S.csv
            R_row = next(R_reader, None)

        while S_row is not None:
            writer.writerow([''] * 3 + S_row)  # Append empty fields for R.csv
            S_row = next(S_reader, None)


my_merge_join('R.csv', 'S.csv', 'O2.csv')
