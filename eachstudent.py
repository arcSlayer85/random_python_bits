import csv;

x = open('grades.csv');

rdr = csv.reader(x);

data = list(rdr);

dataLen = len(data) - 1;

lst = [];

for i in range(0, len(data), 100):
    if rdr.line_num == 1:
        continue;
    else:
        chunks = data[i:i + 18];
        

print(chunks);
            
                    
                    
                    
                        





    


    
