import csv;
from tkinter import *;

f = open('grades.csv');

rdr = csv.reader(f);

data = list(rdr);

# print(data);

names = [];
ucaspnts = [];
fingrd = [];
totals = [];
grdcnt = 0;

count = 0


# for each list (d) in data...
for d in data:
    # skip the top line of the file (the headings)...
    if d == data[0]:
        continue;
    else:
        # put the names of each student into a list(names) then
        # translate and calculate their final UCAS points, for each
        # grade the variable grdcnt is incremented by the value of
        # the grade...
        names.append(d[0] + ' ' + d[1]);
        for i in d:
            if i == 'P':
                grdcnt += 7;
            if i == 'M':
                grdcnt += 8;
            if i == 'D':
                grdcnt += 9;
    ucaspnts.append(grdcnt * 10);
    grdcnt = 0

# check their totals and give them their final grade...
for u in ucaspnts:
    if u <= 1299:
        fingrd.append('FAIL?')
    elif u >= 1300 and u <= 1339:
        fingrd.append('MPP');
    elif u >= 1340 and u <= 1379:
        fingrd.append('MMP');
    elif u >= 1380 and u <= 1419:
        fingrd.append('MMM');
    elif u >= 1420 and u <= 1459:
        fingrd.append('DMM');
    elif u >= 1460 and u <= 1499:
        fingrd.append('DDM');
    elif u >= 1500 and u <= 1529:
        fingrd.append('DDD');
    elif u >= 1530 and u <= 1559:
        fingrd.append('D*DD');
    elif u >= 1560 and u <= 1589:
        fingrd.append('D*D*D');
    elif u >= 1590:
        fingrd.append('D*D*D*');

# print(len(ucaspnts));
# print(len(names));
# print(len(fingrd));
# print(ucaspnts);
# print(names);
# print(fingrd);

# print Name, UCAS points and Final Grade...                
for x in range(0, 7):
    n = count;
    # print(n);
    totals.append(names[n] + ' ' + str(ucaspnts[n]) + ' ' + fingrd[n]);
    # print(names[n], 'total UCAS points :', ucaspnts[n], 'Final Grade :', fingrd[n]);
    count += 1;

print(totals);