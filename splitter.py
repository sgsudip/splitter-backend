import os
import sys
import csv
import uuid
import pandas as pd

if len(sys.argv) != 4:
    print("Invalid call try 'python3 split_csv.py (input_file) (lines_per_file)")
    exit(1)

file_path = sys.argv[1]
# print(file_path)
file_name = sys.argv[2]
# print(file_name)
no_of_files = int(sys.argv[3])
# print(no_of_files)
no_of_files = max(no_of_files, 1)

rows=[]
with open(os.getcwd()+file_path, 'r') as f:
    reader = csv.reader(f)
    rows=list(reader)

current_data=[]
lines_indexes = []
split_data = []
file_paths = []

if len(rows) % no_of_files == 0:
    # print("if block")
    no_of_rows_per_file = int(len(rows)/no_of_files)
    iter = 0
    while iter < len(rows):
        lines_indexes.append([iter, min(len(rows),iter + no_of_rows_per_file)])
        iter = iter + no_of_rows_per_file

    for interval in lines_indexes:
    #   print(interval)
      current_data = rows[interval[0]:interval[1]]
    #   print("current data")
    #   print(current_data)
      split_data.append(current_data)
    #   print(split_data)
    count = 1
    for data in split_data:
      relative_path = '/tmp/' + str(uuid.uuid4()) + file_name.split('.')[0] + '_' + str(count) + '.' + file_name.split('.')[1]
      path = os.getcwd() + relative_path
      f = open(path, 'w')
      writer = csv.writer(f, delimiter = ',')
      writer.writerows(data)
      file_paths.append(relative_path)  
    
    sys.stdout.flush()     
    print(file_paths)
else:
    rowlength = len(rows)
    divisions = no_of_files
    quotient = int(rowlength/divisions)
    remainder = int(rowlength%divisions)
    lv1array=[]
  
    print(rowlength)
    count=0    
    while count <= rowlength:
        lv1array.append(count)
        count+=quotient
        if(count>=rowlength):
            count=rowlength
            lv1array[len(lv1array)-1]=count
            break


    for j in range(len(lv1array)-1):
        arr=[lv1array[j],lv1array[j+1]]
        lines_indexes.append(arr)

    for interval in lines_indexes:
      current_data = rows[interval[0]:interval[1]]
      split_data.append(current_data)
  
    count = 1
    for data in split_data:
      sys.stdout.flush()
      relative_path = '/tmp/' + str(uuid.uuid4()) + file_name.split('.')[0] + '_' + str(count) + '.' + file_name.split('.')[1]
      path = os.getcwd() + relative_path
      f = open(path, 'w')
      writer = csv.writer(f, delimiter = ',')
    #   data is a two d array or it is supposed to be
      writer.writerows(data)
      file_paths.append(relative_path)  
    
    sys.stdout.flush()
    print(file_paths)  
    