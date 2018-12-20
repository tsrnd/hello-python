import sys
sys.path.append('../modules')
import exam_module_functions as modFunc

check = modFunc.checkUser('Quang Tuan')

if check:
    info = modFunc.getCarInfoByName('Turbo')
    if info == '':
        print('Can\'t search car info')
    else:
        print('car info:', info)
else:
    print('login fail. Program will end.')