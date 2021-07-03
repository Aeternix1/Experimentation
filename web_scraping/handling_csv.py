import csv

with open('data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0 
    for row in csv_reader:  
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            header = row  
            line_count += 1
        else: 
            print(f'{header[0]}:{row[0]},{header[1]}:{row[1]},{header[2]}:{row[2]}')
        # else: 
            # print(f'\t{row[0]} works in the {row[1]} department, and was born 
            # line_count += 1
    print(f'Processed {line_count} lines.')
