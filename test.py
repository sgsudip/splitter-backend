import csv
import os


path=r"C:\Users\Sudip Modi\Desktop\PROJECTS\REACT-NATIVE-PROJECTS\SOFTGENICS-WORK\CSV File Splitter\CSV File Splitter\Backend\TESTDATA\\3 rows csv - Sheet1.csv"

with open(path,'r') as file:
    reader = csv.reader(file)
    print(list(reader))
    for row in reader:
        print(row)

# with open(os.cwd()+file_path, dialect='excel') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)