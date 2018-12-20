import sys
sys.path.append('../modules')
import exam_module_functions as modFunc

print('Are you want to open file? (y/n) : ')
str = input()

if str == 'y':
    status = True
else:
    status = False

print(status)

if status:
    print('please input file want to open:')
    strFile = input()
    modFunc.readAndDisplay(strFile)
else:
    print('please input file want to write:')
    strFile = input()
    modFunc.writeFile(strFile)