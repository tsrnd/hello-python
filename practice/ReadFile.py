
with open('output.txt', 'r') as fr:
    for line in fr:
        arr = line.rstrip().split(' ')
        print(arr)
    fr.close()

try:
    fin = open('bad_file')
    for line in fin:
        print(line)
    fin.close()
except:
    print('Something went wrong')
