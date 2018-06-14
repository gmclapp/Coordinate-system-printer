import csv

def list_of_lists_to_csv(list1):
    #takes a list of lists and prints it to a csv
    
    output_file = open('output.csv', 'w', newline='')
    writer = csv.writer(output_file, dialect='excel')
    for row in list1:
        writer.writerow(row)
    output_file.close()

list_of_lists_to_csv(test_list)
