import csv

with open("sample.csv") as f:
    content = csv.reader(f)
    read_line_in_file = []
    for each_line in content:
        read_line_in_file += each_line

print (read_line_in_file)

print ("read each content ")
print (read_line_in_file[1])


with open("sample.csv", "w", newline="") as f:
    data_handler = csv.writer(f, delimiter=",")