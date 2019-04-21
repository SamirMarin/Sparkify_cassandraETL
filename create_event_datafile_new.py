import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv

def get_file_path_list():
    """Obtains the filepath list under currentFolder/event_data"""

    filepath = os.getcwd() + '/event_data'

    for root, dirs, files in os.walk(filepath):
        file_path_list = glob.glob(os.path.join(root,'*'))

    return file_path_list

def create_list_of_data_to_write(file_path_list):
    """Creates a list of data from files in file_path_list
    """

    full_data_rows_list = [] 
    for f in file_path_list:
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            csvreader = csv.reader(csvfile) 
            next(csvreader)
        
            for line in csvreader:
                full_data_rows_list.append(line) 

    return full_data_rows_list

def create_new_csv_file(full_data_rows_list):
    """Creates event_datafile_new.csv using data in full_data_rows_list"""

    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))

def main():
    file_path_list = get_file_path_list()
    full_data_rows_list = create_list_of_data_to_write(file_path_list)
    create_new_csv_file(full_data_rows_list)



if __name__ == "__main__":
    main()

