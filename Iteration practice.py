_list = ['1', '2', '3', '4'];



for x in _list:
    print(x);


_inp = str(input("Would you like to append()?"));

if _inp == 'Yes' or _inp == 'yes':
    _list.append('5')
    print(_list, 'this shoud stop at five');
else:
    print(_list, 'this should stop at four...');


